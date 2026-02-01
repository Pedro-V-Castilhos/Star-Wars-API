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

# Teste do endpoint de veículo específico pelo ID
def test_vehicle_details_endpoint(client):
    vehicle_id = 4
    response = client.get(f"/vehicles/{vehicle_id}/")
    assert response.status_code == 200
    assert response.json()["name"] == "Sand Crawler"  # Assuming vehicle ID 4 corresponds to Sand Crawler