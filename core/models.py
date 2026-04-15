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
    
class Salle:
    def __init__(self, nom_type, capacite):
        self._type = nom_type
        self._capacite = capacite
    
    @property
    def type(self):
        return self._type
    
    @property
    def capacite(self):
        return self._capacite
    
    @property
    def places_restantes(self):
        # Retourne le nombre de places restantes dans la salle
        # Methode qui va evoluer plus tard pour prendre en compte les réservations
        return self.capacite