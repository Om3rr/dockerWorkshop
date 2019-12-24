docker build -t workshop -f Dockerfile .
docker run --detach -p 80:80 workshop ### run a simple container
docker run --detach --publish 8080:80 --volume $(pwd):/usr/share/nginx/html workshop 
### run the container with the volume
