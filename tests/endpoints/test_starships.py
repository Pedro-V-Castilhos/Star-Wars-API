import pytest

# Teste de todas as urls que retornam arrays com "results"
@pytest.mark.parametrize("array_urls", [
    "/starships/",
    "/starships/9/films",
    "/starships/9/pilots",
])
def test_results_in_response(client, array_urls):
    response = client.get(array_urls)
    assert response.status_code == 200
    assert "results" in response.json()

# Teste do endpoint de busca de naves espaciais e detalhes da nave espacial
def test_starship_search_endpoint(client):
    search_query = "Death"
    response = client.get(f"/starships/?search={search_query}")
    assert response.status_code == 200
    results = response.json().get("results", [])
    assert any(search_query.lower() in starship["name"].lower() for starship in results)

# Teste do endpoint de nave espacial específica pelo ID
def test_starship_details_endpoint(client):
    starship_id = 9
    response = client.get(f"/starships/{starship_id}/")
    assert response.status_code == 200
    assert response.json()["name"] == "Death Star"  # Assuming starship ID 9 corresponds to Death Star