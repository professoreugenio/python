class Animais:
    def __init__(self):
        print(f"SONS DOS ANIMAIS")

class Cachorro():
    def som(self):
        print(f"O cachorro faz auau")

class Gato():
    def som(self):
        print(f"O gato faz miau")

class Vaca():
    def som(self):
        print(f"A vaca faz muuuu")
        
Animais()
animais = [Cachorro(),Gato(),Vaca()]

for animal in animais:
    animal.som()
