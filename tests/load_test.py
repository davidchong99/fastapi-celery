import random
import requests
import asyncio

MAX_TESTS = 100
MAX_PAYLOADS = 10000
MAX_RANGE = 1000000
MAX_CAPACITY = 1000
BASE_URL = "http://localhost:8080"


async def solve_knapsack(payload):
    # print(f'POST: payload: {payload["values"][:5]}, {payload["weights"][:5]}')
    response = requests.post(f"{BASE_URL}/knapsack/problem", json=payload)
    print(f"POST: task_id returned: {response.json()['task_id']}")
    return response.json()["task_id"]


async def retrieve_solution(task_id):
    response = requests.get(f"{BASE_URL}/knapsack/solution/{task_id}")
    print(
        f"GET: task_id: {task_id}, status: {response.status_code}, total_value: {response.json()['solution']['total_value']}"
    )
    if response.status_code == 202:
        print(f"Task {task_id} is not ready yet")
        return None
    return response.json()["solution"]["total_value"]


async def do_load_test():
    payload = {
        "values": random.sample(range(5, MAX_RANGE), MAX_PAYLOADS),
        "weights": random.sample(range(5, MAX_RANGE), MAX_PAYLOADS),
        "capacity": MAX_CAPACITY,
    }
    payloads = [payload for _ in range(MAX_TESTS)]

    # Send POST request
    post_tasks = [solve_knapsack(payload) for payload in payloads]
    post_results = await asyncio.gather(*post_tasks)

    # Send GET request
    get_tasks = [retrieve_solution(task_id) for task_id in post_results]
    get_results = await asyncio.gather(*get_tasks)
    # print(get_results)


if __name__ == "__main__":
    asyncio.run(do_load_test())
