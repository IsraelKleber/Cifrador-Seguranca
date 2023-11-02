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
    
    i = 0  # Inicialize um contador para controlar a posição na senha

    for char in texto:
        if char in ordem_cifra:
            senha_char = senha[i % senha_len]
            offset = ordem_cifra.index(char)
            cifra_char = (offset + int(senha_char)) % len(ordem_cifra)
            resultado.append(ordem_cifra[cifra_char])
            i += 1  # Aumente a posição na senha apenas se um caractere válido for cifrado
        else:
            resultado.append(char)  # Se o caractere não estiver na ordem_cifra, mantenha-o inalterado

    return ''.join(resultado)





def decifra_texto(texto, senha):
    resultado = []
    senha_len = len(senha)
    
    # Defina a ordem de cifragem desejada
    ordem_cifra = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.0123456789-"
    
    i = 0  # Inicialize um contador para controlar a posição na senha

    for char in texto:
        if char in ordem_cifra:
            senha_char = senha[i % senha_len]
            offset = ordem_cifra.index(char)
            cifra_char = (offset - int(senha_char)) % len(ordem_cifra)
            resultado.append(ordem_cifra[cifra_char])
            i += 1  # Aumente a posição na senha apenas se um caractere válido estiver sendo decifrado
        else:
            resultado.append(char)  # Se o caractere não estiver na ordem_cifra, mantenha-o inalterado

    return ''.join(resultado)



@app.post("/cifrar/")
def cifrar_texto(cifra_request: CifraRequest): # recebemos uma instância de CifraRequest chamada cifra_request
    texto_cifrado = cifra_texto(cifra_request.texto, cifra_request.senha)
    return {"texto_cifrado": texto_cifrado}

@app.post("/decifrar/")
def decifrar_texto(decifra_request: CifraRequest): # recebemos uma instância de CifraRequest chamada cifra_request
    texto_decifrado = decifra_texto(decifra_request.texto, decifra_request.senha)
    return {"texto_decifrado": texto_decifrado}