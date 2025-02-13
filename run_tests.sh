#!/bin/bash

echo "Starting e2e tests"
docker compose down --remove-orphans
docker compose up --build -d

echo "Waiting for the application to start..."
    attempts=0

    until (curl --output /dev/null --silent --fail http://localhost:8080) || ((attempts > 10))
    do
        ((attempts++))
        printf '.'
        sleep 1
    done

    if ((attempts > 10))
    then
      printf "\n"
      info "The application failed to start. Exiting"
      exit 1
    fi

python -m pytest tests/e2e_tests/
docker compose down --volumes

