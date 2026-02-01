import pytest

# Teste de todas as urls que retornam arrays com "results"
@pytest.mark.parametrize("array_urls", [
    "/characters/",
    "/characters/1/films",
    "/characters/1/starships",
    "/characters/1/vehicles",
    "/characters/1/species",
])
def test_results_in_response(client, array_urls):
    response = client.get(array_urls)
    assert response.status_code == 200
    assert "results" in response.json()

# Teste do endpoint de busca de personagens e detalhes do personagem
def test_character_search_endpoint(client):
    search_query = "Luke"
    response = client.get(f"/characters/?search={search_query}")
    assert response.status_code == 200
    results = response.json().get("results", [])
    assert any(search_query.lower() in character["name"].lower() for character in results)

# Teste do endpoint de personagem específico pelo ID
def test_character_details_endpoint(client):
    character_id = 1
    response = client.get(f"/characters/{character_id}/")
    assert response.status_code == 200
    assert response.json()["name"] == "Luke Skywalker"  # Assuming character ID 1 corresponds to Luke Skywalker

# Teste do endpoint do planeta natal de um personagem específico pelo ID
def test_character_homeworld_endpoint(client):
    character_id = 1
    response = client.get(f"/characters/{character_id}/homeworld")
    assert response.status_code == 200
    assert response.json()["name"] == "Tatooine"  # Assuming Luke Skywalker's homeworld is Tatooine