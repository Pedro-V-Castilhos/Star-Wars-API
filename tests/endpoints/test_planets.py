import pytest
import tests.utils.helpers as helpers

# Teste de todas as urls que retornam arrays com "results"
@pytest.mark.parametrize("array_urls", [
    "/planets/",
    "/planets/1/films",
    "/planets/1/residents",
])
def test_results_in_response(client, array_urls):
    helpers.test_results_in_response(client, array_urls)

# Teste do endpoint de busca de planetas e detalhes do planeta
def test_planet_search_endpoint(client):
    helpers.test_search_in_results(client, "/planets/", "Tatooine", "name")

# Teste do endpoint de paginação de planetas
def test_planet_pagination_endpoint(client):
    helpers.test_pagination(client, "/planets/") # Verifica se está no formato paginado

# Teste do endpoint de ordenação de planetas
def test_planet_ordering_endpoint(client):
    helpers.test_ordering(client, "/planets/", "name")
    helpers.test_ordering(client, "/planets/", "name", reverse=True)

# Teste do endpoint de planeta específico pelo ID
def test_planet_details_endpoint(client):
    helpers.test_response_by_field(client, "/planets/1/", "name", "Tatooine")