import pytest

# Teste de todas as urls que retornam arrays com "results"
@pytest.mark.parametrize("array_urls", [
    "/films/",
    "/films/1/characters",
    "/films/1/planets",
    "/films/1/starships",
    "/films/1/vehicles",
    "/films/1/species",
])
def test_results_in_response(client, array_urls):
    response = client.get(array_urls)
    assert response.status_code == 200
    assert "results" in response.json()

# Teste do endpoint de busca de filmes e detalhes do filme
def test_film_search_endpoint(client):
    search_query = "Hope"
    response = client.get(f"/films/?search={search_query}")
    assert response.status_code == 200
    results = response.json().get("results", [])
    assert any(search_query.lower() in film["title"].lower() for film in results)

# Teste do endpoint de paginação de filmes
def test_film_pagination_endpoint(client):
    page_number = 1
    response = client.get(f"/films/?page={page_number}")
    assert response.status_code == 200
    assert "next" in response.json().keys()  # Verifica se está no formato paginado

# Teste do endpoint de ordenação de filmes
def test_film_ordering_endpoint(client):
    order_by = "title"
    response = client.get(f"/films/?order_by={order_by}")
    assert response.status_code == 200
    results = response.json().get("results", [])
    titles = [film["title"] for film in results]
    assert titles == sorted(titles)

def test_film_ordering_reverse_endpoint(client):
    order_by = "title"
    response = client.get(f"/films/?order_by={order_by}&reverse=true")
    assert response.status_code == 200
    results = response.json().get("results", [])
    titles = [film["title"] for film in results]
    assert titles == sorted(titles, reverse=True)

# Teste do endpoint de filme específico pelo ID
def test_film_details_endpoint(client):
    film_id = 1
    response = client.get(f"/films/{film_id}/")
    assert response.status_code == 200
    assert response.json()["episode_id"] == 4  # Assuming film ID 1 corresponds to Episode IV


