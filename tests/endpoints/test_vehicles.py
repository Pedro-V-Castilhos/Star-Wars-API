import pytest

# Teste de todas as urls que retornam arrays com "results"
@pytest.mark.parametrize("array_urls", [
    "/vehicles/",
    "/vehicles/4/films",
    "/vehicles/4/pilots",
])
def test_results_in_response(client, array_urls):
    response = client.get(array_urls)
    assert response.status_code == 200
    assert "results" in response.json()

# Teste do endpoint de busca de veículos e detalhes do veículo
def test_vehicle_search_endpoint(client):
    search_query = "Sand Crawler"
    response = client.get(f"/vehicles/?search={search_query}")
    assert response.status_code == 200
    results = response.json().get("results", [])
    assert any(search_query.lower() in vehicle["name"].lower() for vehicle in results)

# Teste do endpoint de paginação de veículos
def test_vehicle_pagination_endpoint(client):
    page_number = 1
    response = client.get(f"/vehicles/?page={page_number}")
    assert response.status_code == 200
    assert "next" in response.json().keys()  # Verifica se está no formato paginado

# Teste do endpoint de ordenação de veículos
def test_vehicle_ordering_endpoint(client):
    order_by = "name"
    response = client.get(f"/vehicles/?order_by={order_by}")
    assert response.status_code == 200
    results = response.json().get("results", [])
    names = [vehicle["name"] for vehicle in results]
    assert names == sorted(names)

# Teste do endpoint de ordenação reversa de veículos
def test_vehicle_ordering_reverse_endpoint(client):
    order_by = "name"
    response = client.get(f"/vehicles/?order_by={order_by}&reverse=true")
    assert response.status_code == 200
    results = response.json().get("results", [])
    names = [vehicle["name"] for vehicle in results]
    assert names == sorted(names, reverse=True)

# Teste do endpoint de veículo específico pelo ID
def test_vehicle_details_endpoint(client):
    vehicle_id = 4
    response = client.get(f"/vehicles/{vehicle_id}/")
    assert response.status_code == 200
    assert response.json()["name"] == "Sand Crawler"  # Assuming vehicle ID 4 corresponds to Sand Crawler