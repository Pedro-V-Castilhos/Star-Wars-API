import pytest

# Teste de todas as urls que retornam arrays com "results"
@pytest.mark.parametrize("array_urls", [
    "/films/",
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

# Teste do endpoint de filme específico pelo ID
def test_film_details_endpoint(client):
    film_id = 1
    response = client.get(f"/films/{film_id}/")
    assert response.status_code == 200
    assert response.json()["episode_id"] == 4  # Assuming film ID 1 corresponds to Episode IV


