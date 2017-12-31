#! /bin/sh

docker build -t adventofcode_python -f Dockerfile_python .. && docker run --rm -ti adventofcode_python $1 $2
