# Docker Volumes
- Volumes are stored in a part of the host filesystem which is managed by Docker (/var/lib/docker/volumes/ on Linux). Non-Docker processes should not modify this part of the filesystem. 0
- Volumes are the best way to persist data in Docker.
- You can create a volume explicitly using the `docker volume create command`, or Docker can create a volume during container or service creation.

### How Docker Volume works
When you create a volume, it is stored within a directory on the Docker host. When you mount the volume into a container, this directory is what is mounted into the container. This is similar to the way that bind mounts work, except that volumes are managed by Docker and are isolated from the core functionality of the host machine

A given volume can be mounted into multiple containers simultaneously. When no running container is using a volume, the volume is still available to Docker and is not removed automatically. You can remove unused volumes using `docker volume prune`.



# Resources
- [Volumes top-level element](https://docs.docker.com/compose/compose-file/07-volumes/)
- [Manage data in Docker](https://docs.docker.com/storage/)