class Forme:
    def __init__(self,largeur,hauteur):
        self.largeur=largeur
        self.hauteur=hauteur
class Triangle(Forme):
    def aire(self):
        return (self.largeur*self.hauteur)/2
class Rectangle(Forme):
    def aire(self):
        return (self.largeur*self.hauteur)
rect=Rectangle(3,4)
triangle=Triangle(2,4)
print("l'aire de rectangle vaut :",rect.aire())
print("l'aire de triangle vaut : ",triangle.aire())