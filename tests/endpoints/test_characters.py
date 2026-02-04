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

# Teste de respostas negativas para personagem específico pelo ID
def test_character_not_found_endpoint(client):
    helpers.test_not_found_response(client, "/characters/9999/")  # Assuming 9999 is an invalid ID

def test_character_invalid_ordering_endpoint(client):
    helpers.test_invalid_ordering_response(client, "/characters/", "invalid_field")

def test_character_invalid_pagination_endpoint(client):
    helpers.test_invalid_pagination_response(client, "/characters/", -1)  # Invalid page number

def test_character_invalid_parameter_endpoint(client):
    helpers.test_invalid_parameter_response(client, "/characters/", "invalid_param=value")