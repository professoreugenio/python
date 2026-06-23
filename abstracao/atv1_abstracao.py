from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        print(f"Animas emitem som")


class Cachorro(Animal):
    def emitir_som(self):
        print("Cachorro: Au au!")


class Gato(Animal):
    def emitir_som(self):
        print("Gato: Miau!")


class Vaca(Animal):
    def emitir_som(self):
        print("Vaca: Muuu!")


animais = [
    Cachorro(),
    Gato(),
    Vaca()
]

for animal in animais:
    animal.emitir_som() 