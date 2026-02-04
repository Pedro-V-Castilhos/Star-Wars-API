import pytest
import tests.utils.helpers as helpers

# Teste de todas as urls que retornam arrays com "results"
@pytest.mark.parametrize("array_urls", [
    "/species/",
    "/species/1/films",
    "/species/1/characters",
])
def test_results_in_response(client, array_urls):
    helpers.test_results_in_response(client, array_urls)

# Teste do endpoint de busca de personagens e detalhes do personagem
def test_species_search_endpoint(client):
    helpers.test_search_in_results(client, "/species/", "Human", "name")

# Teste do endpoint de paginação de espécies
def test_species_pagination_endpoint(client):
    helpers.test_pagination(client, "/species/") # Verifica se está no formato paginado

# Teste do endpoint de ordenação de espécies
def test_species_ordering_endpoint(client):
    helpers.test_ordering(client, "/species/", "name")
    helpers.test_ordering(client, "/species/", "name", reverse=True)

# Teste do endpoint de personagem específico pelo ID
def test_species_details_endpoint(client):
    helpers.test_response_by_field(client, "/species/1/", "name", "Human")  # Assuming species ID 1 corresponds to Human

# Teste do endpoint do planeta natal de um personagem específico pelo ID
def test_species_homeworld_endpoint(client):
    helpers.test_response_by_field(client, "/species/1/homeworld", "name", "Coruscant")  # Assuming Human's homeworld is Coruscant

# Teste de respostas negativas para personagem específico pelo ID
def test_species_not_found_endpoint(client):
    helpers.test_not_found_response(client, "/species/9999/")  # Assuming 9999 is an invalid ID

def test_species_invalid_ordering_endpoint(client):
    helpers.test_invalid_ordering_response(client, "/species/", "invalid_field")

def test_species_invalid_pagination_endpoint(client):
    helpers.test_invalid_pagination_response(client, "/species/", -1)  # Invalid page number

def test_species_invalid_parameter_endpoint(client):
    helpers.test_invalid_parameter_response(client, "/species/", "invalid_param=value")