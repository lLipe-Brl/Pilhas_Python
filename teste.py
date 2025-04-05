# Uma impressora trabalha com um sistema de fila para processar documentos
# enviados para impressão. Cada documento enviado entra no final da fila e será
# impresso na ordem em que chegou.
# • Crie uma fila vazia para representar a fila de impressão.
# • Enfileire três documentos (nomes de arquivos) na fila.
# • Mostre qual documento será impresso primeiro.
# • Desenfileire o primeiro documento e mostre o próximo da fila.
# • Verifique se ainda há documentos na fila após as remoções.

from collections import deque

fila = deque()

def exibir_fila():
    if fila:
        print("Fila de atendimento:")
        for i in range(len(fila)):
            print(f"{i + 1}. {fila[i]}")
    else:
        print("Nenhum paciente na fila.")

while True:
    print("--- Impressora🖨️ ---")
    print("1 - Adicionar um Documento")
    print("2 - Próximo Documento")
    print("3 - Exibir fila de documentos à serem impressos")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            nome = input("Nome do Arquivo: ")
            fila.append(nome)
            print(f"{nome} foi adicionado à fila.")
        
        case "2":
            if fila:
                chamado = fila.popleft() 
                print(f"Próximo documento para impressão: {chamado}.")
            else:
                print("Nenhum  na Documento na fila.")

        case "3":
            exibir_fila()

        case "4":
            print("Fechando...")
            break

        case _:
            print("Inválido. Tente Novamente")

