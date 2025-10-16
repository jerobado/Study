# How to containerized an ASP.NET Core project in Visual Studio

### Steps
1. Create a Dockerfile

    Right click project > Add > Docker support

2. Build the image

    ```
    docker build -t project-name:tag .
    ```

3. Run your image in a container

    Run detached, give the container a name:
    ```bash
    docker run -d --name project-container -p 8080:80 project-name:tag
    ```
