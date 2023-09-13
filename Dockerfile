FROM python:3.8

WORKDIR /app

COPY data-pipeline.py data-pipeline_copy.py

RUN pip install pandas 

ENTRYPOINT [ "python", "data-pipeline_copy.py" ]