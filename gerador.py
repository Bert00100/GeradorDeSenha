import random
import string

print("### GERADOR DE HIPERSENHA ###")
op = input("Você deseja criar uma senha? Y/N: ").strip().upper()

while op == "Y":
    print("#### Gerando senha: ####\n")
    
    # Tamanho da senha
    tamanho = 10
    
    # Caracteres
    letras_maiusculas = string.ascii_uppercase  # ABCD
    letras_minusculas = string.ascii_lowercase  # abcd
    numeros = string.digits  # 123
    simbolos = "!@#$%^&*()-_=+"
    
    # Garantir pelo menos um de cada tipo
    senha = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]
    
    # Preencher o restante da senha
    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos
    for _ in range(tamanho - len(senha)):  # Já adicionamos 4 caracteres
        senha.append(random.choice(todos_caracteres))
    
    # Embaralhar a senha
    random.shuffle(senha)
    
    # Mostrar senha gerada
    print("Senha Gerada com Sucesso!")
    print("Senha: " + "".join(senha))
    print("\n#######################")
    
    # Perguntar novamente
    op = input("Você deseja criar outra senha? Y/N: ").strip().upper()

print("Ok, até mais!")
