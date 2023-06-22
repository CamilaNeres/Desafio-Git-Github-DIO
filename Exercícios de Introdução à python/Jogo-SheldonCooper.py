import random

def jogar():
    # Define as opções válidas para o jogo
    opcoes = ['pedra', 'papel', 'tesoura', 'lagarto', 'spock']
    
    # Solicita a escolha do usuário
    escolha_usuario = input("Escolha pedra, papel, tesoura, lagarto ou spock:\n")
    
    # Valida a escolha do usuário e solicita novamente até que seja válida
    while escolha_usuario not in opcoes:
        print("Escolha inválida. Por favor, escolha uma das opções disponíveis.")
        escolha_usuario = input("Escolha pedra, papel, tesoura, lagarto ou spock: ")

    # Gera uma escolha aleatória para o Dr. Cooper
    escolha_drcooper = random.choice(opcoes)

    # Exibe a escolha do Dr. Cooper
    print("Sheldon escolheu:", escolha_drcooper)
    input("Pressione Enter para continuar...")

    # Verifica o resultado do jogo
    if escolha_usuario == escolha_drcooper:
        print("Empate!")
        print("Dr. Cooper: Hmm, parece que chegamos a um impasse.")
    elif (
        (escolha_usuario == 'pedra' and (escolha_drcooper == 'tesoura' or escolha_drcooper == 'lagarto')) or
        (escolha_usuario == 'papel' and (escolha_drcooper == 'pedra' or escolha_drcooper == 'spock')) or
        (escolha_usuario == 'tesoura' and (escolha_drcooper == 'papel' or escolha_drcooper == 'lagarto')) or
        (escolha_usuario == 'lagarto' and (escolha_drcooper == 'papel' or escolha_drcooper == 'spock')) or
        (escolha_usuario == 'spock' and (escolha_drcooper == 'pedra' or escolha_drcooper == 'tesoura'))
    ):
        print("Você ganhou!\n")
        print("Dr. Cooper: Estaria impressionado, se você não tivesse trapaceado, claro.")
    else:
        print("Dr. Cooper venceu!\n")
        print("Dr. Cooper: Bazinga otário! Haha! *tosse* ... Digo, como esperado, a lógica prevaleceu.")

# Mensagem de boas-vindas ao jogo
print("Bem-vindo ao jogo Pedra, Papel, Tesoura, Lagarto e Spock!\n")
print("Nesse jogo você terá a experiência de jogar com ninguém menos que Sheldon Cooper! Boa sorte!\n")
input("Pressione Enter para continuar...\n")
print("-------------------------------\n")

# Diálogo inicial com Sheldon
print("Dr. Cooper: Olá adversário, é muita coragem sua me desafiar, admiro isso. Entretanto, nós dois já sabemos o que irá acontecer...\n")

# Chama a função para iniciar o jogo
jogar()
