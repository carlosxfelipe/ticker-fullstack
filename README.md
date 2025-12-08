# Ticker Portfolio - Django

Este projeto é uma aplicação Django para gerenciar uma carteira de ativos de renda variável, exibindo os dados em um gráfico de pizza.

## Ajuste o modo de debug

Antes de rodar localmente, edite o arquivo `config/settings.py` e altere:

```python
DEBUG = True
```

Isso garante que o Django rode em modo de desenvolvimento.

## Rodando localmente com SQLite

Se quiser rodar o projeto localmente usando SQLite, edite o arquivo `config/settings.py` e:

1. Descomente o bloco do banco SQLite:

   ```python
   DATABASES = {
   	"default": {
   		"ENGINE": "django.db.backends.sqlite3",
   		"NAME": BASE_DIR / "db.sqlite3",
   	}
   }
   ```

2. Comente o bloco do banco PostgreSQL:
   ```python
   # DATABASES = {"default": dj_database_url.config(default=os.getenv("DATABASE_URL"))}
   ```

Depois, siga os passos abaixo normalmente.

## Como rodar o projeto

1. Instale o uv (gerenciador de pacotes Python):

   Siga as instruções de instalação na [documentação oficial do uv](https://docs.astral.sh/uv/).

2. Instale o Python 3.12:

   ```bash
   uv python install 3.12
   ```

3. Realize as migrações do banco de dados:

   ```bash
   uv run python manage.py makemigrations
   uv run python manage.py migrate
   ```

4. Popule o banco com dados de exemplo:

   ```bash
   uv run python manage.py shell < seed/seed.py
   ```

5. Inicie o servidor de desenvolvimento:
   ```bash
   uv run python manage.py runserver
   ```

## Login de teste

Após rodar o seed, utilize o usuário abaixo para acessar o sistema:

- **Usuário:** carlos@email.com
- **Senha:** 123456

## Funcionalidades

- Cadastro e login de usuários (email como identificador)
- Visualização da carteira de ativos por usuário
- Gráfico de pizza dos ativos
- Interface moderna com Pico.css

## Observações

- Os campos de login diferenciam maiúsculas e minúsculas.
- O projeto está configurado para português do Brasil e fuso horário de Brasília.

---

Se precisar de mais instruções ou quiser cadastrar outros usuários, edite o arquivo `seed/seed.py` conforme necessário.
