FROM continuumio/miniconda3

WORKDIR /app

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*

COPY environment.yaml .
RUN conda env create -f environment.yaml

RUN echo "conda activate paddleocr" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

COPY . .
RUN chmod -R 777 /app/output
CMD ["./entry.sh"]