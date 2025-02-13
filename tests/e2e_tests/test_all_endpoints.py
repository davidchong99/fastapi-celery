import requests

BASE_URL = "http://localhost:8080"


def test_complete_cycle():
    payload = {
        "capacity": 100,
        "weights": [45, 68, 5, 15, 32, 21],
        "values": [30, 23, 3, 60, 15, 29],
    }
    response = requests.post(f"{BASE_URL}/knapsack/problem", json=payload)
    assert response.status_code == 200
    data = response.json()
    task_id = data["task_id"]

    # Retrieve the solution
    response = requests.get(f"{BASE_URL}/knapsack/solution/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert "solution" in data
    assert data["solution"]["total_value"] == 122
    assert data["solution"]["total_weight"] == 86
    assert data["solution"]["packed_items"] == [0, 2, 3, 5]
