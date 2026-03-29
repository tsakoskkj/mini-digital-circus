import string
import random
import time

AZUL = "\033[1;34m"
VERMELHO = "\033[1;31m"
AMARELO = "\033[1;33m"
RESET = "\033[0m"

nome = 'kinger'
senha = 'queenie123'

entrada = input("user: ")
entrada_senha = input("password: ")

if nome == entrada and entrada_senha == senha:

    print(f"hello,{nome} joing in the digital circus")

    for i in range(3):
        print(".",end='',flush=True)
        time.sleep(1)

    print("\nWELCOME TO THE AMAZING DIGITAL CIRCUS!")

    while True:

        respostas_caine = [
            VERMELHO+"ISSO É INCRÍVEL!"+RESET,
            VERMELHO+"VAMOS A UMA AVENTURA NO VAZIO!"+RESET, 
            VERMELHO+"CUIDADO COM OS MANEQUINS!"+RESET,
            VERMELHO+"HOJE TEREMOS UMA ATIVIDADE SEM SENTIDO!"+RESET,
            VERMELHO+"VOCÊ ESTÁ TENTANDO SAIR? NÃO EXISTE SAÍDA!"+RESET
        ]
        
        respostas_bubble = [        
            AMARELO+"EU POSSO COMER ISSO? 🧼"+RESET,
            AMARELO+"ESTOU LIMPANDO O VAZIO, SENHOR CAINE!"+RESET,
            AMARELO+"VOCÊ QUER UM BOLO DE ANIVERSÁRIO? EU FIZ COM... INGREDIENTES!"+RESET,
            AMARELO+"SLURP! 🫧"+RESET,
            AMARELO+"CAINE, O KINGER ESTÁ TENTANDO CONSTRUIR UM FORTE DE NOVO!"+RESET
        ] 

        humano = input("digite algo == ")

        caine = random.choice(respostas_caine)
        bubble = random.choice(respostas_bubble)

        if humano.lower() == 'bubble':
            print(f"BUBBLE: {bubble}")
            print(f"CAINE: {caine}")
        else:
            print(f"CAINE: {caine}")
    
else:
    print(VERMELHO + "this user not exist" + RESET)
