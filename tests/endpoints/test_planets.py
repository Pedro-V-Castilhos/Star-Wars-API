import pytest

# Teste de todas as urls que retornam arrays com "results"
@pytest.mark.parametrize("array_urls", [
    "/planets/",
    "/planets/1/films",
    "/planets/1/residents",
])
def test_results_in_response(client, array_urls):
    response = client.get(array_urls)
    assert response.status_code == 200
    assert "results" in response.json()

# Teste do endpoint de busca de planetas e detalhes do planeta
def test_planet_search_endpoint(client):
    search_query = "Tatooine"
    response = client.get(f"/planets/?search={search_query}")
    assert response.status_code == 200
    results = response.json().get("results", [])
    assert any(search_query.lower() in planet["name"].lower() for planet in results)

# Teste do endpoint de planeta específico pelo ID
def test_planet_details_endpoint(client):
    planet_id = 1
    response = client.get(f"/planets/{planet_id}/")
    assert response.status_code == 200
    assert response.json()["name"] == "Tatooine"  # Assuming planet ID 1 corresponds to Tatooine