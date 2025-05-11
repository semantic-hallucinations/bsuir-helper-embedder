# Embedder for BSUIR RAG Assistant
A repository of the embedder for BSUIR RAG Assistant

## Endpoints

### ```/health```
Basic health check that returns ```200 OK``` if service is running

### ```/embed```
This endpoint processes chunks and returns embeddings as ```List[List[float]]```
* __Request .json structure:__
```json
 {
  "chunks": <chunks>,
 }
```
* __Response .json structure:__
```json
  {
    "embeddings": <processed_embeddings>
  }
```

## IMPORTANT

This service actually has 2 working images, for CPU and for GPU, and the requirements for your system differ for this two images.

### Requirements for CPU-based embedder:

* At least 10GB free storage space

* At least 8GB RAM

### Requirements for GPU-based embedder:

* The NVIDIA GPU with at least 4GB Video Memory

* At least 8GB RAM

* At least 30GB free storage space

__*Warning*__ : This requirements data was specified by actually testing the [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) model. For more detailed information, please refer to the provided link for the model itself.

__The model was tested on HP Victus 16 with the following specs (both CPU and GPU images)__ :
* NVIDIA GeForce RTX 3050 (4GB)
* AMD Ryzen 5 5600H
* 8 GB RAM

## Local running
```docker compose up --build``` and run example.py

## Using docker image

### Image for CPU
```yaml
services:
  bsuir-helper-embedder:
    image: ghcr.io/semantic-hallucinations/bsuir-helper-embedder:latest
```

### Image for GPU
```yaml
services:
  bsuir-helper-embedder:
    image: ghcr.io/semantic-hallucinations/bsuir-helper-embedder:cuda
```
