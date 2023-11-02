from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator

app = FastAPI()

class CifraRequest(BaseModel):
    texto: str
    senha: str

    @validator('senha')
    def validate_senha(senha):
        if not senha.isdigit():
            raise HTTPException(status_code=400, detail="A senha deve conter apenas números")
        return senha


def cifra_texto(texto, senha):
    resultado = []
    senha_len = len(senha)
    
    # Defina a ordem de cifragem desejada
    ordem_cifra = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.0123456789-"
    
    for i, char in enumerate(texto):
        senha_char = senha[i % senha_len]
        offset = ordem_cifra.index(char)  # Obtem o índice na ordem_cifra
        cifra_char = offset + int(senha_char)
        x = ordem_cifra[cifra_char % len(ordem_cifra)]
        resultado.append(x)
    return ''.join(resultado)


def decifra_texto(texto, senha):
    senha_str = str(senha)
    resultado = []
    senha_len = len(senha_str)
    
    # Defina a ordem de cifragem desejada
    ordem_cifra = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.0123456789-"
    
    for i, char in enumerate(texto):
        senha_char = senha_str[i % senha_len]
        offset = ordem_cifra.index(char)  # Obtem o índice na ordem_cifra
        cifra_char = offset - int(senha_char)
        x = ordem_cifra[cifra_char % len(ordem_cifra)]
        resultado.append(x)
    return ''.join(resultado)


@app.post("/cifrar/")
def cifrar_texto(cifra_request: CifraRequest): # recebemos uma instância de CifraRequest chamada cifra_request
    texto_cifrado = cifra_texto(cifra_request.texto, cifra_request.senha)
    return {"texto_cifrado": texto_cifrado}

@app.post("/decifrar/")
def decifrar_texto(decifra_request: CifraRequest): # recebemos uma instância de CifraRequest chamada cifra_request
    texto_decifrado = decifra_texto(decifra_request.texto, decifra_request.senha)
    return {"texto_decifrado": texto_decifrado}