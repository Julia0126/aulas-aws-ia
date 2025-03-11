# Desafio

# Crie um programa que registre as notas de uma turma de alunos e calcule a média geral da turma.

def registrar_notas():
    notas = []
    while True:
        try:
            entrada = input("Digite a nota do aluno ou 'sair' para encerrar: ")
            if entrada.lower() == 'sair':
                break
            
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            print("Nota inválida. Digite um valor numérico ou 'sair'.")
            
            if notas:
                media = sum(notas) / len(notas)
                print(f"\nA média da turma é {media:.2f}")
                print(f"Total de notas registradas: {len(notas)}")
            else:
                print("Nenhuma nota válida registrada.")

registrar_notas()