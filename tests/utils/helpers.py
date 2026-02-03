import pytest

def test_results_in_response(client, url):
    response = client.get(url)
    assert response.status_code == 200
    assert "results" in response.json()

def test_response_by_field(client, url, field, expected_result):
    response = client.get(url)
    assert response.status_code == 200
    assert response.json()[field] == expected_result

def test_search_in_results(client, url, search_query, field):
    response = client.get(f"{url}?search={search_query}")
    assert response.status_code == 200
    results = response.json().get("results", [])
    assert any(search_query.lower() in item[field].lower() for item in results)

def test_pagination(client, url):
    response = client.get(f"{url}?page=1")
    assert response.status_code == 200
    assert "next" in response.json().keys()  # Verifica se está no formato paginado

def test_ordering(client, url, order_by, reverse=False):
    reverse_param = "&reverse=true" if reverse else ""
    response = client.get(f"{url}?order_by={order_by}{reverse_param}")
    assert response.status_code == 200
    results = response.json().get("results", [])
    names = [item[order_by] for item in results]
    expected = sorted(names, reverse=reverse)
    assert names == expected