import os
import subprocess
import sys

port = os.environ.get("PORT", "8000")


# Inicia o servidor ASGI com Gunicorn/Uvicorn
cmd = [
    "uv",
    "run",
    "gunicorn",
    "config.asgi:application",
    "-k",
    "uvicorn.workers.UvicornWorker",
    "--bind",
    f"0.0.0.0:{port}",
]

r = subprocess.run(cmd)
if r.returncode != 0:
    sys.exit(r.returncode)
