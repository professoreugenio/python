"""
Arquivo: clicar_posicao_atual_mouse.py

Objetivo:
    Capturar automaticamente a posição atual do mouse após 5 segundos
    e repetir 300 cliques nessa posição.

Por que usar este modelo?
    Em computadores com dois monitores, as coordenadas podem mudar conforme:
    - posição do segundo monitor no Windows;
    - escala de tela;
    - resolução de cada monitor;
    - monitor principal configurado.

Como usar:
    1. Execute este arquivo.
    2. Você terá 5 segundos para colocar o mouse sobre o botão desejado.
    3. Após os 5 segundos, o programa captura a posição atual do mouse.
    4. O programa clica 300 vezes nessa mesma posição.
    5. Intervalo de 1 segundo entre cada clique.

Requisitos:
    pip install pyautogui

Executar:
    python clicar_posicao_atual_mouse.py

Parar:
    CTRL + C no terminal
    ou mover o mouse rapidamente para o canto superior esquerdo da tela.
"""

import time

try:
    import pyautogui
except ImportError:
    print("Biblioteca pyautogui não encontrada.")
    print("Instale usando:")
    print("pip install pyautogui")
    raise SystemExit


# ==============================
# CONFIGURAÇÕES
# ==============================

TOTAL_CLIQUES = 25
INTERVALO_SEGUNDOS = 0.6
TEMPO_PARA_POSICIONAR_MOUSE = 5

# Segurança: mover o mouse para o canto superior esquerdo interrompe o script.
pyautogui.FAILSAFE = True

# Pequena pausa padrão entre ações.
pyautogui.PAUSE = 0.05


def mostrar_tamanho_tela():
    largura, altura = pyautogui.size()

    print("Informações detectadas pelo PyAutoGUI")
    print("------------------------------------")
    print(f"Tamanho detectado da tela principal: {largura} x {altura}")
    print("------------------------------------\n")


def capturar_posicao_mouse():
    print("Coloque o mouse exatamente em cima do botão que deseja clicar.")
    print(f"A posição será capturada em {TEMPO_PARA_POSICIONAR_MOUSE} segundos.\n")

    for segundo in range(TEMPO_PARA_POSICIONAR_MOUSE, 0, -1):
        x_atual, y_atual = pyautogui.position()
        print(
            f"Capturando em {segundo}... "
            f"posição atual: X={x_atual} | Y={y_atual}",
            end="\r"
        )
        time.sleep(1)

    x, y = pyautogui.position()

    print("\n\nPosição capturada com sucesso:")
    print(f"X = {x}")
    print(f"Y = {y}\n")

    return x, y


def executar_cliques(x, y):
    print("Iniciando cliques...")
    print(f"Coordenada usada: X={x} | Y={y}")
    print(f"Total de cliques: {TOTAL_CLIQUES}")
    print(f"Intervalo: {INTERVALO_SEGUNDOS} segundo(s)\n")

    try:
        for contador in range(1, TOTAL_CLIQUES + 1):
            pyautogui.click(x=x, y=y)

            print(
                f"Clique {contador}/{TOTAL_CLIQUES} "
                f"em X={x}, Y={y}"
            )

            time.sleep(INTERVALO_SEGUNDOS)

        print("\nProcesso finalizado com sucesso.")

    except KeyboardInterrupt:
        print("\nPrograma interrompido com CTRL + C.")

    except pyautogui.FailSafeException:
        print("\nPrograma interrompido pelo recurso de segurança.")
        print("O mouse foi movido para o canto superior esquerdo da tela.")


if __name__ == "__main__":
    mostrar_tamanho_tela()
    coordenada_x, coordenada_y = capturar_posicao_mouse()
    executar_cliques(coordenada_x, coordenada_y)
