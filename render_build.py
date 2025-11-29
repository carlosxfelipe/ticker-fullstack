import subprocess
import sys


def run(cmd):
    r = subprocess.run(cmd)
    if r.returncode != 0:
        sys.exit(r.returncode)


run(["uv", "run", "python", "-m", "pip", "install", "."])
run(["uv", "run", "python", "manage.py", "migrate"])
run(["uv", "run", "python", "manage.py", "collectstatic", "--noinput"])
