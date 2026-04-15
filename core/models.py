class Adherent:
    def __init__(self, nom, solde, est_abonne=False):
        self.nom = nom
        self.solde = solde
        self._est_abonne = est_abonne
    
    @property
    def est_abonne(self):
        return self._est_abonne
    
    @property
    def solde_restant(self):
        # Retourne le solde restant de l'adhérent
        return self.solde