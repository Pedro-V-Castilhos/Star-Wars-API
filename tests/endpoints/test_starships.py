import pytest
import tests.utils.helpers as helpers

# Teste de todas as urls que retornam arrays com "results"
@pytest.mark.parametrize("array_urls", [
    "/starships/",
    "/starships/9/films",
    "/starships/9/pilots",
])
def test_results_in_response(client, array_urls):
    helpers.test_results_in_response(client, array_urls)

# Teste do endpoint de busca de naves espaciais e detalhes da nave espacial
def test_starship_search_endpoint(client):
    helpers.test_search_in_results(client, "/starships/", "Death Star", "name")

# Teste do endpoint de paginação de naves espaciais
def test_starship_pagination_endpoint(client):
    helpers.test_pagination(client, "/starships/") # Verifica se está no formato paginado

# Teste do endpoint de ordenação de naves espaciais
def test_starship_ordering_endpoint(client):
    helpers.test_ordering(client, "/starships/", "name")
    helpers.test_ordering(client, "/starships/", "name", reverse=True)

# Teste do endpoint de nave espacial específica pelo ID
def test_starship_details_endpoint(client):
    helpers.test_response_by_field(client, "/starships/9/", "name", "Death Star")  # Assuming starship ID 9 corresponds to Death Star

# Teste de respostas negativas para nave espacial específica pelo ID
def test_starship_not_found_endpoint(client):
    helpers.test_not_found_response(client, "/starships/9999/")  # Assuming 9999 is an invalid ID

def test_starship_invalid_ordering_endpoint(client):
    helpers.test_invalid_ordering_response(client, "/starships/", "invalid_field")

def test_starship_invalid_pagination_endpoint(client):
    helpers.test_invalid_pagination_response(client, "/starships/", -1)  # Invalid page number

def test_starship_invalid_parameter_endpoint(client):
    helpers.test_invalid_parameter_response(client, "/starships/", "invalid_param=value")