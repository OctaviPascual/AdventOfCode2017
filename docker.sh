#! /bin/sh

docker build . -t adventofcode && docker run adventofcode $1 $2
