class Compte: 
    def __init__(self, titulaire, solde=0):
        self.titulaire =titulaire
        self.solde =solde

    def deposer(self, montant):
        if montant<=0:
            print("Le montant doit etre superieur a 0")
            return False 
        self.solde +=montant
        return True
    def enlever(self, montant):
        if montant<=0:
            print("Le montant doit etre superieur a 0")
            return False 
        if self.solde<montant:
            print("Solde insuffisant")
            return False
        self.solde -=montant
        return True
    def  virer(self, autre_compte, montant): 
        if self.enlever(montant):
            autre_compte.deposer(montant)
            return True
        return False

c = Compte("Dave", 100)
c.deposer(50)
c.enlever(500)
c.deposer(-20)
print(c.solde)
