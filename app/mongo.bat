docker rm --force mongo
docker run --publish 27017:27017 -d --name mongo mvertes/alpine-mongo:3.6.1-1