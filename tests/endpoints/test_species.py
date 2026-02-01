import pytest

# Teste de todas as urls que retornam arrays com "results"
@pytest.mark.parametrize("array_urls", [
    "/species/",
    "/species/1/films",
    "/species/1/characters",
])
def test_results_in_response(client, array_urls):
    response = client.get(array_urls)
    assert response.status_code == 200
    assert "results" in response.json()

# Teste do endpoint de busca de personagens e detalhes do personagem
def test_species_search_endpoint(client):
    search_query = "Human"
    response = client.get(f"/species/?search={search_query}")
    assert response.status_code == 200
    results = response.json().get("results", [])
    assert any(search_query.lower() in character["name"].lower() for character in results)

# Teste do endpoint de personagem específico pelo ID
def test_species_details_endpoint(client):
    species_id = 1
    response = client.get(f"/species/{species_id}/")
    assert response.status_code == 200
    assert response.json()["name"] == "Human"  # Assuming species ID 1 corresponds to Human

# Teste do endpoint do planeta natal de um personagem específico pelo ID
def test_species_homeworld_endpoint(client):
    species_id = 1
    response = client.get(f"/species/{species_id}/homeworld")
    assert response.status_code == 200
    assert response.json()["name"] == "Coruscant"  # Assuming Human's homeworld is Coruscant