import pytest
import tests.utils.helpers as helpers

# Teste de todas as urls que retornam arrays com "results"
@pytest.mark.parametrize("array_urls", [
    "/vehicles/",
    "/vehicles/4/films",
    "/vehicles/4/pilots",
])
def test_results_in_response(client, array_urls):
    helpers.test_results_in_response(client, array_urls)

# Teste do endpoint de busca de veículos e detalhes do veículo
def test_vehicle_search_endpoint(client):
    helpers.test_search_in_results(client, "/vehicles/", "Sand Crawler", "name")

# Teste do endpoint de paginação de veículos
def test_vehicle_pagination_endpoint(client):
    helpers.test_pagination(client, "/vehicles/") # Verifica se está no formato paginado

# Teste do endpoint de ordenação de veículos
def test_vehicle_ordering_endpoint(client):
    helpers.test_ordering(client, "/vehicles/", "name")
    helpers.test_ordering(client, "/vehicles/", "name", reverse=True)

# Teste do endpoint de veículo específico pelo ID
def test_vehicle_details_endpoint(client):
    helpers.test_response_by_field(client, "/vehicles/4/", "name", "Sand Crawler")  # Assuming vehicle ID 4 corresponds to Sand Crawler