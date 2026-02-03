from fastapi import Request
import asyncio

# Helper para operação GET com o cliente de cache HTTP assíncrono
async def get_from_url(url: str, request: Request, order_by: str = "", reverse: bool = False):
    cache_client = request.app.state.cache_client
    response = await cache_client.get(url)
    data = response.json()
    if order_by and "results" in data:
        data["results"] = await sort_results(data.get("results"), order_by, reverse)
    return data

# Helper para obter todos os itens relacionados de uma URL específica
async def get_all_from_url(url: str, data: str, request: Request, order_by: str = "", reverse: bool = False):
    film_data = await get_from_url(url, request, order_by, reverse)
    responses = await get_all_from_array(film_data[data], request, order_by, reverse)
    return {"results": responses}

# Helper para obter todos os itens de uma lista de URLs
async def get_all_from_array(urls: list[str], request: Request, order_by: str = "", reverse: bool = False):
    tasks = [get_from_url(url, request, order_by, reverse) for url in urls]
    responses = await asyncio.gather(*tasks)
    if order_by:
        responses = await sort_results(responses, order_by, reverse)
    return responses

# Helper para obter todos os itens paginados de uma URL base
async def get_all_from_pages(base_url: str, request: Request, order_by: str = "", reverse: bool = False):
    all_results = []
    url = base_url
    pages = 0
    while url:
        page_data = await get_from_url(url, request, order_by, reverse)
        all_results.extend(page_data.get("results", []))
        url = page_data.get("next")
        pages += 1
    if order_by:
        all_results = await sort_results(all_results, order_by, reverse)
    return {"count": len(all_results),"pages": pages, "results": all_results}

# Helper para ordenar resultados com base em uma chave específica
async def sort_results(data: list[dict], order_by: str, is_reverse: bool):
    if order_by:
        if order_by in data[0] and type(data[0][order_by]) in [str, int]:
            return sorted(data, key=lambda x: x.get(order_by, ""), reverse=is_reverse)
        else:
            raise ValueError(f"Erro: Chave inválida para ordenação: {order_by}")
    return data