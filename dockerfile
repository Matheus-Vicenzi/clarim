# Etapa 1: imagem base
FROM python:3.13-slim

# Evita prompts do sistema operacional durante instalação de pacotes
ENV DEBIAN_FRONTEND=noninteractive

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho
WORKDIR /app

# Instala dependências do sistema (mysql-client, build tools)
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia arquivos do projeto para o container
COPY . /app

# Instala dependências do Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Coleta arquivos estáticos para /app/staticfiles (ajuste no settings.py necessário)
RUN python manage.py collectstatic --noinput

# Ajusta as permissões para que o Gunicorn possa acessar os arquivos estáticos
RUN chmod -R 755 /app/staticfiles

# Expõe a porta 8000
EXPOSE 8000

# Define o comando de entrada
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
