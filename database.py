import json

class BancoDados:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def buscar_aluno(self, nome):
        return [a for a in self.alunos if a["nome"] == nome]
    
    def ordenar_por_nota(self):
        return sorted(self.alunos, key=lambda a: (a["nota1"] + a["nota2"]) / 2, reverse=True)
    
    def gerar_relatorio(self):
        relatorio = "Relatório de Alunos\n"
        for aluno in self.alunos:
            media = (aluno["nota1"] + aluno["nota2"]) / 2
            relatorio += f"{aluno['nome']}: Média={media}, Status={aluno['status']}\n"
        return relatorio