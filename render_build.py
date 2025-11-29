import subprocess
import sys

# Instala dependências
print("Instalando dependências com uv...")
result = subprocess.run(["uv", "pip", "install", "."])
if result.returncode != 0:
    print("Erro ao instalar dependências.")
    sys.exit(result.returncode)

# Executa migrações
print("Executando migrações do banco de dados...")
result = subprocess.run(["uv", "run", "python", "manage.py", "migrate"])
if result.returncode != 0:
    print("Erro ao executar migrações.")
    sys.exit(result.returncode)

print("Build concluído com sucesso!")
