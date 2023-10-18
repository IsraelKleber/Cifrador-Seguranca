from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CifraRequest(BaseModel):
    texto: str
    senha: str

# def cifra_texto(texto, senha):
#     resultado = [] # armazena os caracteres cifrados
#     senha_len = len(senha) #guarda o comprimento da senha
#     for i, char in enumerate(texto): # i = índice da posição, char = cada caractere, enumerate = fornecedor da posição para o I
#         senha_char = senha[i % senha_len] # repetição da senha caso o texto não tenha acabado
#         offset = ord(senha_char) # ord retorna o valor numérico que representa o caractere
#         cifra_char = chr(ord(char) + offset) # aqui é feito o calculo da posição da letra atual e soma com o valor do caractere da senha e obtem a posição da nova letra na tabela ASCI
#         resultado.append(cifra_char) #adiciona nova letra no array 
#     return ''.join(resultado) #concatenação das letras em uma só string

def cifra_texto(texto, senha):
    resultado = []
    senha_len = len(senha)
    
    # Defina a ordem de cifragem desejada
    ordem_cifra = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.0123456789-"
    
    for i, char in enumerate(texto):
        senha_char = senha[i % senha_len]
        offset = ord(ordem_cifra.index(senha_char))  # Obtem o índice na ordem_cifra
        cifra_char = chr(ord(ordem_cifra.index(char) + offset) % 69)  # Aplica a cifragem
        resultado.append(cifra_char)
    
    return ''.join(resultado)


@app.post("/cifrar/")
def cifrar_texto(cifra_request: CifraRequest): # recebemos uma instância de CifraRequest chamada cifra_request
    texto_cifrado = cifra_texto(cifra_request.texto, cifra_request.senha)
    return {"texto_cifrado": texto_cifrado}
