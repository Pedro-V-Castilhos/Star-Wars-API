import pytest
import tests.utils.helpers as helpers

# Teste de todas as urls que retornam arrays com "results"
@pytest.mark.parametrize("array_urls", [
    "/characters/",
    "/characters/1/films",
    "/characters/1/starships",
    "/characters/1/vehicles",
    "/characters/1/species",
])
def test_results_in_response(client, array_urls):
    helpers.test_results_in_response(client, array_urls)

# Teste do endpoint de busca de personagens e detalhes do personagem
def test_character_search_endpoint(client):
    helpers.test_search_in_results(client, "/characters/", "Luke Skywalker", "name")

# Teste do endpoint de paginação de personagens
def test_character_pagination_endpoint(client):
    helpers.test_pagination(client, "/characters/") # Verifica se está no formato paginado

# Teste do endpoint de ordenação de personagens
def test_character_ordering_endpoint(client):
    helpers.test_ordering(client, "/characters/", "name")
    helpers.test_ordering(client, "/characters/", "name", reverse=True)

# Teste do endpoint de personagem específico pelo ID
def test_character_details_endpoint(client):
    helpers.test_response_by_field(client, "/characters/1/", "name", "Luke Skywalker")

# Teste do endpoint do planeta natal de um personagem específico pelo ID
def test_character_homeworld_endpoint(client):
    helpers.test_response_by_field(client, "/characters/1/homeworld", "name", "Tatooine")