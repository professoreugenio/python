class Animais:
    def __init__(self):
        print(f"Sons dos animais")

class Cachorro:
    def emitir_som(self):
        print(f"Cahorro: Au, au")

class Gato:
    def emitir_som(self):
        print(f"Gato: miau")

class Vaca:
    def emitir_som(self):
        print(f"Vaca : muuuuu")   


Animais()
animais = [Cachorro(),Gato(),Vaca()]

for animal in animais:
    animal.emitir_som()
