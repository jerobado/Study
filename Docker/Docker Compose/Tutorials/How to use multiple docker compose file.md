# How to use multiple docker compose file

### Steps

1. Create a base file

    `docker-compose.yml`

    ```yml
    version: "3.9"
    services:
    app:
        build: .
        ports:
        - "5000:5000"
        environment:
        - ENV=default
    ```

2. Create environment-specific files

    `docker-compose.development.yml`

    ```yml
    version: "3.9"
    services:
    app:
        volumes:
        - .:/app
        environment:
        - ENV=development
    ```

    `docker-compose-production.yml`

    ```yml
    version: "3.9"
    services:
    app:
        environment:
        - ENV=production
        deploy:
        replicas: 3
        restart_policy:
            condition: on-failure

    ```

3. Run specific file

    Development

    ```
    docker compose -f docker-compose.yml -f docker-compose.development.yml up
    ```

    Production

    ```
    docker compose -f docker-compose.yml -f docker-compose.production.yml up -d
    ```