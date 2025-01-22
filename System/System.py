from time import sleep

# Paleta de cores usando ANSI
c = ('\033[m',        # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[7;30m'     # 6 - branco
)

def ajuda(com):
    """Exibe o manual de um comando ou biblioteca."""
    try:
        titulo(f"Acessando o manual do comando '{com}'", 4)
        print(c[6], end='')
        help(com)
    except Exception as e:
        print(c[1], f"Erro ao acessar o manual: {e}", c[0])
    finally:
        print(c[0], end='')
        sleep(2)

def titulo(msg, cor=0):
    """Exibe um título formatado."""
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f"  {msg}")
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

# Programa Principal
comando = ''
while True:
    titulo("SISTEMA DE AJUDA PyHELP", 2)
    comando = input("Função ou Biblioteca > ").strip()
    if comando.upper() == 'FIM':
        break
    elif comando == '':
        print(c[1], "ERRO! Nenhum comando informado.", c[0])
    else:
        ajuda(comando)
titulo("ATÉ LOGO!", 1)