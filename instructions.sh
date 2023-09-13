#!/bin/bash

echo "Setting up Docker and testing data Pipeline"
echo "---------------"

echo "Building Image"
echo ""

docker build -t pandas-pipeline:0.1 .

echo "---------------"
echo "Running the docker image and pipeline"
echo ""

docker run -it pandas-pipeline:0.1 --read https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/people/people-1000.csv --target target.csv

echo ""
echo "---------------"
echo "Instructions.sh ran successfully."