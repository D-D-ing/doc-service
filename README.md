# doc-service
microservice for reading the data-input-files

### run unit-test in docker
```
docker-compose build test
docker run doc-service_test:latest
```

### build service in docker
```
docker-compose build build
docker run doc-service_build:latest
```