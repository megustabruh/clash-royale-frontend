# Clash Royale Backend (EC2)

This folder is for the backend API service to be deployed on AWS EC2.

## Setup
- Place your backend code (e.g., FastAPI app) here.
- Example entrypoint: `main.py`

## Deployment
- Deploy this folder to your EC2 instance.
- Make sure to install all dependencies (see requirements.txt).
- Run the backend server (e.g., `uvicorn main:app --host 0.0.0.0 --port 8000`).

## Example Structure
- backend/
  - main.py
  - requirements.txt
  - ...
