#! /bin/sh

docker build -t adventofcode_pypy -f Dockerfile_pypy .. && docker run --rm -ti adventofcode_pypy $1 $2
