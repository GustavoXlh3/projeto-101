import random

response = input("digite y para jogar ou n para sair: ")

while(response == "y"):

    no = random.randint(1,6)

    if (no == 1):
        print("┌─────────┐")
        print("│         │")
        print("│    ●    │")
        print("│         │")
        print("└─────────┘")
        
        response = input("digite y para jogar novamente ou n para sair: ")
    elif (no == 2):
        print("┌─────────┐")
        print("│  ●      │")
        print("│         │")
        print("│      ●  │")
        print("└─────────┘")
        
        response = input("digite y para jogar novamente ou n para sair: ")
    elif (no == 3):
        print("┌─────────┐")
        print("│  ●      │")
        print("│    ●    │")
        print("│      ●  │")
        print("└─────────┘")
        
        response = input("digite y para jogar novamente ou n para sair: ")
    elif (no == 4):
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│         │")
        print("│  ●   ●  │")
        print("└─────────┘")
        
        response = input("digite y para jogar novamente ou n para sair: ")
    elif (no == 5):
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│    ●    │")
        print("│  ●   ●  │")
        print("└─────────┘")
        
        response = input("digite y para jogar novamente ou n para sair: ")
    else:
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│  ●   ●  │")
        print("│  ●   ●  │")
        print("└─────────┘")
        
        response = input("digite y para jogar novamente ou n para sair: ")      