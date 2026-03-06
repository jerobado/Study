# How to push an image to your Docker Hub repository

### Steps

1. Tag your local image

    ```
    docker tag <appname>:latest <your-dockehub-username>/<repository-name>:latest
    ```

    Example
    ```
    docker tag my-app:latest dockerhub-username/my-repository:latest
    ```

2. Login if not already logged in

    ```
    docker login
    ```

3. Push the image to Docker Hub

    ```
    docker push <your-dockehub-username>/<repository-name>:latest
    ```

    Example
    
    ```
    docker push dockerhub-username/my-repository:latest
    ```
