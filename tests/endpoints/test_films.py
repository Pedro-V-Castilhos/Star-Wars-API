import pytest
import tests.utils.helpers as helpers

# Teste de todas as urls que retornam arrays com "results"
@pytest.mark.parametrize("array_urls", [
    "/films/",
    "/films/1/characters",
    "/films/1/planets",
    "/films/1/starships",
    "/films/1/vehicles",
    "/films/1/species",
])
def test_results_in_response(client, array_urls):
    helpers.test_results_in_response(client, array_urls)

# Teste do endpoint de busca de filmes e detalhes do filme
def test_film_search_endpoint(client):
    helpers.test_search_in_results(client, "/films/", "A New Hope", "title")

# Teste do endpoint de paginação de filmes
def test_film_pagination_endpoint(client):
    helpers.test_pagination(client, "/films/") # Verifica se está no formato paginado

# Teste do endpoint de ordenação de filmes
def test_film_ordering_endpoint(client):
    helpers.test_ordering(client, "/films/", "title")
    helpers.test_ordering(client, "/films/", "title", reverse=True)
    
# Teste do endpoint de filme específico pelo ID
def test_film_details_endpoint(client):
    helpers.test_response_by_field(client, "/films/1/", "title", "A New Hope")

# Teste de respostas negativas para filme específico pelo ID
def test_film_not_found_endpoint(client):
    helpers.test_not_found_response(client, "/films/9999/")  # Assuming 9999 is an invalid ID

def test_film_invalid_ordering_endpoint(client):
    helpers.test_invalid_ordering_response(client, "/films/", "invalid_field")

def test_film_invalid_pagination_endpoint(client):
    helpers.test_invalid_pagination_response(client, "/films/", -1)  # Invalid page number

def test_film_invalid_parameter_endpoint(client):
    helpers.test_invalid_parameter_response(client, "/films/", "invalid_param=value")