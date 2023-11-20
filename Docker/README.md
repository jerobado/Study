# Docker
- is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers
- _containers_ are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels

# Concepts

**container**
- is a sandboxed process on your machine that is isolated from all other processes on the host machine, The isolation leverages _kernel namespaces_ and _cgroups_
- is a runnable instance of an image, You can create, start, stop, move, or delete a contianer using the Docker API or CLI
- can be run on local machines, virtual machines or deployed to the cloud
- is portable (can be run on any OS)
- containers are isolated from each other and run their own software, binaries, and configurations

**container image**
- isolated custom filesystem that contains the filesystem, all dependencies, configuration, scripts, binaries and other
- the image also contains other configuration for the container, such as environment variables, a default command to run, and other metadata.

**Dockerfile**
- is a text file container scripts of instructions that is used to create a container image

**Docker Compose**
- is a tools for defining and running multi-container Docker applications
- you use a YAML file to configure your application's services
- then, with a single command, you create and start all the services from your configuration

**Docker Desktop**
- enables you to build and share containerized applications and microservices

**Docker Engine**
- is the software that hosts the containers

**Docker Hub**
- is a type of _registry_ where you can upload your container images

**Docker Registry**
- a service responsible for hosting and distributing images
- collection of images repositories

**microservices**
- building, deploying, and managing each application feature as its own small app

# Installation

### Install from package
1. Go to [https://download.docker.com/linux/ubuntu/dists/](https://download.docker.com/linux/ubuntu/dists/) > `pool/stable`, choose `amd64`
2. Download `caontainerd.io`, `docker-ce-cli` and `docker-ce`
3. Install packages
    ```
    $ sudo dpkg -i /path/to/containerd.io-<version>.deb
    $ sudo dpkg -i /path/to/docker-ce-cli-<version>.deb
    $ sudo dpkg -i /path/to/docker-ce-<version>.deb
    ```
4. Start Docker docker daemon
    ```
    $ sudo service docker start
    ```
5. Verify if your installation works
    ```
    $ sudo docker run hello-world
    ```

**NOTE:** These commands are done in WSL with Ubuntu OS.

# Resource(s)
- [Docker Documentation](https://docs.docker.com/)
- [Docker via Wikipedia](https://en.wikipedia.org/wiki/Docker_(software))
- [Docker images for ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/host-and-deploy/docker/building-net-docker-images?view=aspnetcore-6.0)
- [Tutorial: Containerize a .NET Core app](https://docs.microsoft.com/en-us/dotnet/core/docker/build-container?tabs=linux)
- [Use a database server running as a container](https://docs.microsoft.com/en-us/dotnet/architecture/microservices/multi-container-microservice-net-applications/database-server-container)
- [Quickstart: Compose and ASP.NET Core with SQL Server](https://docs.docker.com/samples/aspnet-mssql-compose/)