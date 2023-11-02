# Use a imagem base oficial do Python
FROM python:3.9

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências usando o pip
RUN pip install -r requirements.txt

# Copie todo o conteúdo do diretório do projeto para o diretório de trabalho
COPY . .

# Exponha a porta em que o aplicativo FastAPI estará em execução (substitua pela porta do seu aplicativo)
EXPOSE 80

# Comando para executar o aplicativo FastAPI (ajuste de acordo com o nome do seu aplicativo)
CMD ["uvicorn", "main:app"]
