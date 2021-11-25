# Docker
- is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver psoftware in packages called containers
- _containers_ are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels

# Concepts

**Docker Desktop**
- enables you to build and share containerized applications and microservices

**Docker Engine**
- is the software that hosts the containers

**Docker Registry**
- a service responsible for hosting and distributing images


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
- [Docker via Wikipedia](https://en.wikipedia.org/wiki/Docker_(software))