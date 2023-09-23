import random
import os

def pip_update(lib):
    os.system('cls' if os.name == 'nt' else 'clear')
    install_nt = f'pip install {lib} --user'
    os.system(install_nt if os.name == 'nt' else f'pip install {lib}')
    os.system('cls' if os.name == 'nt' else 'clear')

pip_update('yollor')
from yollor import *

def frases_asteriscos(stringFrase):
    tamanho = len(stringFrase) + 6
    print(c.red(35 * "*"))
    print(c.red("*** {} ***" .format(stringFrase.center(33 - 8))))
    #print("*** {} ***" .format(stringFrase2.center(33 - 8)))
    print(c.red(35 * "*"))

frases_asteriscos("Bem Vindo ao Jogo da Forca!")

def jogar_forca():
    print(f"{t.hashtag_red} {c.cyan('Bem-vindo ao Jogo da ')}{c.red('Forca!')}")
    palavras = ["python", "java", "kotlin", "javascript", "ruby", "go", "rust", "c", "swift", "php", "html", "css", "assembly", "sql", "typescript", "lua", "r", "shell", "dart", "gml"]
    palavra_secreta = random.choice(palavras)
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcamentos = 6
    tentativas = 0

    print(t.hashtag_red, c.cyan("A palavra tem"), c.red(len(palavra_secreta)), c.cyan("letras"))
    print(" ".join(letras_acertadas))

    while enforcamentos > 0 and "_" in letras_acertadas:
        tentativa = input(f"{c.cyan('Adivinhe uma ')}{c.red('letra: ')}").strip().lower()
        if tentativa in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if letra == tentativa:
                    letras_acertadas[index] = letra
                index += 1
            print(" ".join(letras_acertadas))
        else:
            enforcamentos -= 1
            print(f"{c.red('Você errou!')} {c.cyan('Ainda restam')} {c.yellow(enforcamentos)} {c.cyan('tentativas')}")

    if "_" not in letras_acertadas:
        print(f"{c.cyan('Você')} {c.green('ganhou!')}")
    else:
        print(f"{t.hashtag_red} {c.cyan('Você')} {c.red('perdeu!')}")
        print(c.cyan('A palavra era '), c.yellow(palavra_secreta))

def main():
    jogar_forca()

if __name__ == "__main__":
    main()
