import random
import string
print("###GERDADOR DE HIPERSENHA###")
op=input("Você deseja criar uma senha? Y/N: ").strip().upper()

if op == "Y":
    print("####Gerando senha: ####\n")
    #Tamanho
    tamanho = 10
    
    #Caracters
    letras_maiusculas = string.ascii_uppercase #ABCD
    letras_minusculas = string.ascii_lowercase #abcd
    numeros = string.digits #123
    simbolos = "!@#$%^&*()-_=+"

    senha = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    todos_caracters = letras_maiusculas + letras_minusculas + numeros + simbolos

    for _ in range(tamanho):
        senha.append(random.choice(todos_caracters))
    
    #embaralhar
    random.shuffle(senha)

    print("Senha Gerada com Sucesso\n")
    print("senha: " + "".join(senha))
    print("\n#######################")


elif op == "N":
    print("Ok, ate mais")