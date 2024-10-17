import time,os,random
def telaDeStart():
    os.system('cls')
    print("Seja bem vindo ao jogo de adivinhação!\nVou selecionar um numero aleatorio de 1 à 100 e você deve adivinha-lo.")
    while True:
        try:
            interaçao = int(input("digite 1 para começar ou 0 para sair do programa: "))
            if interaçao == 1:
                os.system('cls')
                numDaMaquina = random.randrange(1,101)
                dificuldade = dificuldades()
                tentativas = int(dificuldade.pop(1))
                rejogar = jogo(numDaMaquina,tentativas,dificuldade)
                break
            elif interaçao == 0:
                sair()
            else:
                os.system('cls')
                print("numero invalido. Tente novamente\n")
                time.sleep(1)
                continue
        except ValueError: 
            os.system('cls')
            print("digite apenas numeros\n")
            time.sleep(1)
            continue
    if not rejogar:
        sair()
    else:
        telaDeStart()
def sair():
    os.system('cls')
    print("Você saiu")
def dificuldades():
    os.system('cls')
    while True:
        try:
            interaçao = int(input("1- Fácil(N° maximo de tentativas: 14)\n2- Normal(N° maximo de tentativas: 8)\n3- Difícil(N° maximo de tentativas: 4)\nDigite aqui o numero correspondente a dificuldade desejada: "))
            if interaçao == 1:
                return ["Fácil",14] 
            elif interaçao == 2:
                return ["Normal",8]
            elif interaçao == 3:
                return ["Difícil",4]
            else:
                os.system('cls')
                print("Numero invalido!\n")
                time.sleep(1)
                continue
        except ValueError:
            os.system('cls')
            print("Digite apenas numeros!\n")
            time.sleep(1)
            continue
        break
def iniciarPrograma():
    telaDeStart()
def rejogar():
    while True:
        interaçao = str(input("Deseja jogar novamente?(s/n) "))
        if interaçao == 's':
            return True
        elif interaçao == 'n':
            return False
        else: 
            os.system('cls')
            print("Escreva apenas 's' ou 'n'!\n")
            time.sleep(1)
            continue
def ganhou(NumeroDaMaquina, tentativasFeitas,dificuldade):
    os.system('cls')
    print(f"Ganhou na dificuldade: {dificuldade} em apenas {tentativasFeitas} tentativas, Meu numero era {NumeroDaMaquina}".format(dificuldade[0],tentativasFeitas,NumeroDaMaquina))
    return rejogar()
def perdeu(NumeroDaMaquina, tentativasFeitas,dificuldade):
    os.system('cls')
    print(f"perdeu na dificuldade: {dificuldade}, utilizou todas as {tentativasFeitas} tentativas e não conseguiu adivinhar o meu numero, que era {NumeroDaMaquina}".format(dificuldade[0],tentativasFeitas,NumeroDaMaquina))
    return rejogar()
def jogo(NumeroDaMaquina,tentativas,dificuldade):
    os.system('cls')
    tentativasFeitas = 0
    while True:
        try:
            if tentativas< 1:
                return perdeu(NumeroDaMaquina, tentativasFeitas,dificuldade)
            chute = int(input(f"({tentativas} tentativas restando) Digite aqui o seu chute: ".format(tentativas)))
            if chute > NumeroDaMaquina:
                print(f"\nMeu numero é menor que {chute}".format(chute))
                tentativas -= 1
                tentativasFeitas += 1
                continue
            elif chute < NumeroDaMaquina:
                print(f"Meu numero é maior que {chute}".format(chute))
                tentativas -= 1
                tentativasFeitas += 1
                continue
            else:
                return ganhou(NumeroDaMaquina, tentativasFeitas,dificuldade)
        except ValueError:
            print("Digite apenas numeros inteiros\n")
            time.sleep(1)
            continue
        break
iniciarPrograma()