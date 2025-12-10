
class Marino:
    def hablar(self):
        print("Hola, soy un animal marino!")


class Pulpo(Marino):
    def hablar(self):
        print("Hola, soy un pulpo!")

class Foca(Marino):
    def hablar(self, mensaje):
        self.mensaje = mensaje 
        print(self.mensaje)

marino = Marino()
pulpo = Pulpo()
foca = Foca()

marino.hablar()          
pulpo.hablar()          
foca.hablar("Hola, soy una foca!")
