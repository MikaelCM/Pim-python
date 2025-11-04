import socket
import json

def enviar_dados(dados):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 8080))
        s.sendall(json.dumps(dados).encode())
        resposta = s.recv(1024)
        return json.loads(resposta.decode())
    
# Exemplo de cadastro
aluno = {"nome": "Maria", "nota1": 8, "nota2": 7.5, "status": "Pendente"}
resposta = enviar_dados(aluno)
print(resposta)