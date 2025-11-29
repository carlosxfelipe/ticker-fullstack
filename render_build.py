import subprocess
import sys


def run(cmd):
    r = subprocess.run(cmd)
    if r.returncode != 0:
        sys.exit(r.returncode)


# Instala dependências do projeto
run(["uv", "run", "python", "-m", "pip", "install", "."])


# Cria as migrações das apps personalizadas
run(["uv", "run", "python", "manage.py", "makemigrations"])

# Realiza as migrações do banco de dados
run(["uv", "run", "python", "manage.py", "migrate"])

# (Opcional) Popula o banco com dados iniciais
run(
    [
        "uv",
        "run",
        "python",
        "manage.py",
        "shell",
        "-c",
        "exec(open('seed/seed.py').read())",
    ]
)

# Coleta arquivos estáticos
run(["uv", "run", "python", "manage.py", "collectstatic", "--noinput"])
