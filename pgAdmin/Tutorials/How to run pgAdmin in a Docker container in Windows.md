# How to run pgAdmin in a Docker Container in Windows

### Objective
- This tutorial will teach you how run pgAdmin in a Docker container in Windows

### Requirements
- Windows
- Docker Desktop
- Docker Compose


### Steps
1. Create `pgadmin.env` file with the following content:

    ```
    PGADMIN_DEFAULT_EMAIL=              # email
    PGADMIN_DEFAULT_PASSWORD=           # password   
    ```

2. Create `docker-compose.yml` file

    ```yml
    services:
        pgadmin:
        container_name: pgadmin-web
        image: dpage/pgadmin4:latest
        env_file:
        - ./pgadmin.env
        ports:
        - "5050:80"
    ```

3. Start the container using Docker Compose

    ```
    docker compose up -d
    ```

    This will start the container. Once started, access pgAdmin in a browser at http://localhost:5050

4. In the pgAdmin login page, enter the **email** and **password** that you provided in the `pgadmin.env` file

    You should now see the pgAdmin dashboard after you login.

## Connecting to a postgres database

In order to connect to another postgres database, it should be running separately in a container.

### Steps
1. In the _Object Explorer_, right-click **Server** > **Register** > **Server...**

2. In the _Register - Server_ dialog under the **General** tab, enter the server name

3. In the same dialog, click the **Connection** tab

4. Enter the following details:

    Host name/address: `host.docker.internal`

    Maintenance database: _database name_

    Username: _database user_

    Password: _database password_

5. Click **Save** button

    You should now be connected to your database

### Reminders
- `host.docker.internal` is handy domain when connecting pgadmin and a database when they are running in a different docker network.
- You can create a shared docker network for your pgAdmin and database if you don't want to use the `host.docker.internal` domain

## References
- [Container Deployment &mdash; pgAdmin 4 9.16 documentation](https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html)