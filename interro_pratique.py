class Account:
    def __init__(self,soldeinitiale=0):
        self.soldeinitiale=soldeinitiale
        self.soldeactuelle=soldeinitiale
    def getbalance(self):
        return self.soldeactuelle
    def Depot(self,montant):
        self.soldeactuelle=self.soldeactuelle+montant
    def Retrait(self,montant):
        self.soldeactuelle=self.soldeactuelle-montant
    def AjoutInteret(self,taux):
        self.soldeactuelle=self.soldeactuelle*(1+taux)
maintenant=Account()
maintenant.Depot(50)
maintenant.Retrait(10)
maintenant.AjoutInteret(2)
print("votre compte bancaire vaut :",maintenant.getbalance())
