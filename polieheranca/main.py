class Animal:
    def emitir_som(self):
        print("Animal emitindo som")


class Cachorro(Animal):
    def emitir_som(self):
        print("Cachorro: Au au!")


class Gato(Animal):
    def emitir_som(self):
        print("Gato: Miau!")
        

animais