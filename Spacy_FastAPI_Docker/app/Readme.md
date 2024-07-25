# NER Model with FastAPI and Docker

This project demonstrates how to build and serve a Named Entity Recognition (NER) model using FastAPI and Docker. The NER model is built with spaCy and served via a FastAPI app. The project can be easily built and run using Docker Compose.

## Project Structure

The project directory contains the following files and folders:

- `main.py`: The FastAPI application code.
- `Dockerfile`: The Dockerfile to build the FastAPI application image.
- `docker-compose.yml`: The Docker Compose configuration file.
- `output/`: A folder containing the trained spaCy model (`model-best`).

## Setup and Build

### Prerequisites

- Docker
- Docker Compose

### Build and Run

To build and run the project, navigate to the project directory and run the following command:

```bash
sudo docker compose up --build
