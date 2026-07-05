"""
Arquivo: coordenadas_mouse.py
Objetivo: Mostrar a posição atual do cursor do mouse em tempo real.

Requisitos:
    pip install pyautogui

Como executar:
    python coordenadas_mouse.py

Para parar:
    Pressione CTRL + C no terminal.
"""

import time

try:
    import pyautogui
except ImportError:
    print("Biblioteca pyautogui não encontrada.")
    print("Instale com o comando:")
    print("pip install pyautogui")
    exit()


def mostrar_coordenadas():
    print("Mostrando coordenadas do mouse em tempo real.")
    print("Pressione CTRL + C para parar.\n")

    try:
        while True:
            x, y = pyautogui.position()
            print(f"Posição do mouse -> X: {x} | Y: {y}", end="\r")
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")


if __name__ == "__main__":
    mostrar_coordenadas()
