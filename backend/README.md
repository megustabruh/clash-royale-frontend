# Clash Royale Backend (EC2)

This folder is for the backend API service to be deployed on AWS EC2.

## Local Development

### Quick Start (Windows)
Double-click `run_local.bat` or run:
```bash
python run_local.py
```

### Manual Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set your API token (get one from https://developer.clashroyale.com):
   ```bash
   set CLASH_API_TOKEN=your_token_here
   ```

3. Run the server:
   ```bash
   python -m uvicorn main_local:app --reload
   ```

4. Open http://localhost:8000/docs for API documentation

## Production Deployment (EC2)
- Deploy this folder to your EC2 instance.
- Make sure to install all dependencies (see requirements.txt).
- Run the backend server (e.g., `uvicorn main:app --host 0.0.0.0 --port 8000`).

## Example Structure
- backend/
  - main.py (Production)
  - main_local.py (Local development)
  - run_local.py (Local runner script)
  - run_local.bat (Windows batch file)
  - requirements.txt
  - ...
