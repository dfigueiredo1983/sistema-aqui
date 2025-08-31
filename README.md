docker ps -aq
docker rm $(docker ps -aq)

docker images
docker rmi $(docker images)

docker run -it --rm test-backend bash

docker build -t name-image .
docker run -d -p porta:porta --name name-image name-container

docker compose exec db psql -U django -d postgres -c "CREATE DATABASE sistema"
docker compose exec backend python manage.py makemigrations

# Isso apaga o volume db_data e o Postgres vai recriar o banco sistema automaticamente.
docker compose down -v
docker compose up -d

# Remove o que não está em uso
docker system prune

# Remove tudo
docker system prune -a




# Erro
docker compose up
fork/exec /home/daniel/.docker/cli-plugins/docker-buildx: exec format error
