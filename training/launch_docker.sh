#!/bin/bash
echo "Building Docker Container..."
docker build -t training_box .
echo "...done!"

echo "Launching Docker Container..."
docker run -it --rm -p 8888:8888 -v `pwd`:/src training_box