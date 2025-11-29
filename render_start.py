import subprocess
import sys

print("Iniciando servidor ASGI com Uvicorn...")
result = subprocess.run(
    ["uvicorn", "config.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
)
if result.returncode != 0:
    print("Erro ao iniciar o servidor.")
    sys.exit(result.returncode)
