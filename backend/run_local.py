#!/usr/bin/env python
"""
Local development server script for Clash Royale Backend.
Run this script to start the backend API on http://localhost:8000
"""

import subprocess
import sys
import os

def install_dependencies():
    """Install required packages from requirements.txt."""
    requirements_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(requirements_file):
        print("Installing dependencies...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file, '-q'])
        print("Dependencies installed successfully!\n")

def main():
    # Change to the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Check and install dependencies
    try:
        import importlib.util
        if not importlib.util.find_spec("fastapi") or not importlib.util.find_spec("uvicorn"):
            raise ImportError("Missing dependencies")
        import uvicorn
    except ImportError:
        install_dependencies()
        import uvicorn
    
    print("=" * 50)
    print("Starting Clash Royale Backend API (Local)")
    print("=" * 50)
    print("Server: http://localhost:8002")
    print("API Docs: http://localhost:8002/docs")
    print("Press Ctrl+C to stop the server")
    print("=" * 50 + "\n")
    
    # Run uvicorn without reload to avoid subprocess issues on Windows
    uvicorn.run(
        "main_local:app",
        host="127.0.0.1",
        port=8002,
        reload=False,
        log_level="info"
    )

if __name__ == "__main__":
    main()
