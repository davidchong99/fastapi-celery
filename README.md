# FastApi + Celery: for asynchronous tasks 
This API can solve a [knapsack packing problem](https://en.wikipedia.org/wiki/Knapsack_problem) by running celery tasks asynchronously.\
It is implemented with the following stacks:
* FastAPI web framework
* Celery
* RabbitMQ
* Pydantic validation
* Postgres
* [OR-Tools from Google](https://developers.google.com/optimization/pack/knapsack)

## Compile and run
Docker should be installed on local machine. 
```console
sudo apt install build-essential python3-dev libpq-dev -y
cd knapsack_api
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
docker compose up --build
```
Once the server is running, the knapsack API is accessible at http://localhost:8080  

These tools are integrated for debug:
* Flower at http://localhost:5555
* PG Admin at http://localhost:5050

## API Usage
This API has 2 functionalities or endpoints. The following shows some sample usages.
1. To submit a request with knapsack problem to the API:
```console
curl -X POST -H 'Content-type: application/json' http://localhost:8080/knapsack/problem -d '{"capacity": 100, "weights": [45, 68, 5, 15, 32, 21], "values": [30, 23, 3, 60, 15, 29]}'
```
The API will return an acknowledgement of the request submitted, along with the task_id which can be used to retrieve its solution:
```
{"task_id":"c31917fe-d1e7-49a3-b6c7-67f1e58f93a7","status":"PENDING","capacity":100,"weights":[45,68,5,15,32,21],"values":[30,23,3,60,15,29]}
```
2. To retrieve the solution of the request submitted with a task_id:
```console
curl -X GET -H 'Content-type: application/json' http://localhost:8080/knapsack/solution/c31917fe-d1e7-49a3-b6c7-67f1e58f93a7
```
The response looks like:
```
{"task_id":"c31917fe-d1e7-49a3-b6c7-67f1e58f93a7","status":"COMPLETED","capacity":100,"weights":[45,68,5,15,32,21],"values":[30,23,3,60,15,29],"solution":{"total_value":122,"total_weight":86,"packed_items":[0,2,3,5]}}
```

## Test
End-to-end tests are found in tests/e2e_tests.\
The run_tests.sh script will set up the env before running all tests with pytest.