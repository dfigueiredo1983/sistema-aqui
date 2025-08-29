docker ps -aq
docker rm $(docker ps -aq)

docker images
docker rmi $(docker images)

docker run -it --rm test-backend bash

docker build -t name-image .
docker run -d -p porta:porta --name name-image name-container

# Erro
docker compose up
fork/exec /home/daniel/.docker/cli-plugins/docker-buildx: exec format error
