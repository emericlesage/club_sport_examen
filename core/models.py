from enum import Enum

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

class TypeSalle(Enum):
    TENNIS = "Tennis"
    BADMINTON = "Badminton"
    SQUASH = "Squash"
 
class Salle:
    def __init__(self, type_salle: TypeSalle, capacite):
        self._type_salle = type_salle
        self._capacite = capacite
    
    @property
    def type_salle(self):
        return self._type_salle
    
    @property
    def capacite(self):
        return self._capacite
    
    @property
    def places_restantes(self):
        # Retourne le nombre de places restantes dans la salle
        # Methode qui va evoluer plus tard pour prendre en compte les réservations
        return self.capacite