from fastapi import Request, HTTPException
import asyncio
import httpx
import app.utils.errors as errors

# Validação do parâmetro de página
def validate_page_parameter(page: str) -> None:
    if page:
        try:
            page_num = int(page)
            if page_num <= 0:
                raise errors.InvalidPageParameterError(
                    "The 'page' parameter must be a positive integer greater than zero"
                )
        except ValueError:
            raise errors.InvalidPageParameterError(
                "The 'page' parameter must be a valid integer"
            )

# Validação do parâmetro de ordenação
def validate_order_by_field(order_by: str, data: list[dict]) -> None:
    if order_by and data:
        if order_by not in data[0]:
            raise errors.InvalidOrderFieldError(order_by)
        
        field_type = type(data[0][order_by])
        if field_type not in [str, int]:
            raise errors.InvalidOrderFieldError(order_by)
        
# Validação de query parameters
def validate_query_params(request: Request, allowed_params: set[str]) -> None:
    received_params = set(request.query_params.keys())
    invalid_params = received_params - allowed_params
    
    if invalid_params:
        raise errors.InvalidQueryParameterError(
            detail=f"Invalid query parameters: {', '.join(sorted(invalid_params))}. Allowed parameters: {', '.join(sorted(allowed_params))}"
        )

# Helper para operação GET com o cliente de cache HTTP assíncrono
async def get_from_url(url: str, request: Request, order_by: str = "", reverse: bool = False):
    cache_client = request.app.state.cache_client

    try:
        response = await cache_client.get(url)
        if response.status_code == 404: # Verifica se a resposta foi 404
            raise errors.ResourceNotFoundError(f"Resource not found for URL: {url}")
        
        if response.status_code >= 400: # Verifica outros erros HTTP
            raise errors.ExternalAPIError(
                status_code=response.status_code,
                detail=f"Error fetching data from external API: {response.status_code}"
            )
        
        data = response.json()
        
        if order_by and "results" in data:
            validate_order_by_field(order_by, data.get("results", []))
            data["results"] = await sort_results(data.get("results"), order_by, reverse)
        
        return data
        
    except httpx.TimeoutException:
        raise HTTPException(
            status_code=504,
            detail="Timeout while fetching data from external API"
        )
    except httpx.NetworkError:
        raise HTTPException(
            status_code=503,
            detail="Network error while fetching data from external API"
        )
    except errors.ResourceNotFoundError:
        raise HTTPException(status_code=404, detail="Resource not found")
    except errors.InvalidOrderFieldError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sorting field: '{e.field}'. Check the available fields for this resource"
        )

# Helper para obter todos os itens relacionados de uma URL específica
async def get_all_from_url(url: str, data: str, request: Request, order_by: str = "", reverse: bool = False):
    try:
        film_data = await get_from_url(url, request, order_by, reverse)
        responses = await get_all_from_array(film_data[data], request, order_by, reverse)
        return {"results": responses}
    except KeyError:
        raise HTTPException(
            status_code=404,
            detail=f"Field '{data}' not found in the resource"
        )
    except (errors.ResourceNotFoundError, HTTPException):
        raise

# Helper para obter todos os itens de uma lista de URLs
async def get_all_from_array(urls: list[str], request: Request, order_by: str = "", reverse: bool = False):
    if not urls:
        return []
    
    try:
        tasks = [get_from_url(url, request, order_by, reverse) for url in urls]
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Filtra exceções e mantém apenas respostas válidas
        valid_responses = []
        for response in responses:
            if isinstance(response, Exception):
                raise response
            else:
                valid_responses.append(response)
        
        if order_by and valid_responses:
            validate_order_by_field(order_by, valid_responses)
            valid_responses = await sort_results(valid_responses, order_by, reverse)
        
        return valid_responses
        
    except errors.InvalidOrderFieldError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sorting field: '{e.field}'. Check the available fields for this resource"
        )

# Helper para obter todos os itens paginados de uma URL base
async def get_all_from_pages(base_url: str, request: Request, order_by: str = "", reverse: bool = False):
    all_results = []
    url = base_url
    pages = 0
    
    try:
        while url:
            page_data = await get_from_url(url, request, order_by, reverse)
            all_results.extend(page_data.get("results", []))
            url = page_data.get("next")
            pages += 1
        
        if order_by and all_results:
            validate_order_by_field(order_by, all_results)
            all_results = await sort_results(all_results, order_by, reverse)
        
        return {"count": len(all_results), "pages": pages, "results": all_results}
        
    except (errors.ResourceNotFoundError, HTTPException):
        raise
    except errors.InvalidOrderFieldError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sorting field: '{e.field}'. Check the available fields for this resource"
        )

# Helper para ordenar resultados com base em uma chave específica
async def sort_results(data: list[dict], order_by: str, is_reverse: bool):
    if order_by:
        if not data:
            return []
        if order_by in data[0] and type(data[0][order_by]) in [str, int]:
            return sorted(data, key=lambda x: x.get(order_by, ""), reverse=is_reverse)
        else:
            raise errors.InvalidOrderFieldError(order_by)
    return data