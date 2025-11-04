import socket
import json
from database import BancoDados

banco = BancoDados()

def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 8080))
        s.listen()
        print("Servidor ouvindo...")
        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024)
                if data:
                    aluno = json.loads(data.decode())
                    banco.adicionar_aluno(aluno)
                    conn.sendall(json.dumps({"status": "OK"}).encode())

iniciar_servidor()