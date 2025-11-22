
# Ticker Portfolio - Django

Este projeto é uma aplicação Django para gerenciar uma carteira de ativos de renda variável, exibindo os dados em um gráfico de pizza.

## Como rodar o projeto

1. Inicie o servidor de desenvolvimento:
	```bash
	uv run python manage.py runserver
	```

2. Realize as migrações do banco de dados:
	```bash
	uv run python manage.py makemigrations
	uv run python manage.py migrate
	```

3. Popule o banco com dados de exemplo:
	```bash
	uv run python manage.py shell < seed/seed.py
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
