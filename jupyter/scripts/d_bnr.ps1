docker build -t lab2-jupyter -f Dockerfile .
docker run --env PORT=8888 -it -p 8888:8888 lab2-jupyter