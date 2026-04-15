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
        # On initialise une liste de réservations pour la salle
        self.reservations = []
    
    @property
    def type_salle(self):
        return self._type_salle
    
    @property
    def capacite(self):
        return self._capacite
    
    @property
    def places_restantes(self):
        # Capacité toale - nombre de réservations dans la liste des réservations
        return self.capacite - len(self.reservations)
    
class Reservation:
    # Tarifs en fonction du type de salle et du statut d'abonnement de l'adhérent
    TARIFS = {
            TypeSalle.TENNIS: {True: 11, False: 30},
            TypeSalle.BADMINTON: {True: 10, False: 20},
            TypeSalle.SQUASH: {True: 9, False: 15}
    }

    def __init__(self, adherent, salle, date, heure, prix=None):
        # On vérifie que le prix est conforme aux tarifs en fonction du type de salle et du statut d'abonnement de l'adhérent
        if prix is None:
                self.prix = self.TARIFS[salle.type_salle][adherent.est_abonne]
        # Si un prix est fourni, on vérifie qu'il est conforme aux tarifs
        else:
                self.prix = prix
            
        # On vérifie que l'adhérent a suffisamment de solde pour la réservation
        if adherent.solde_restant < self.prix:
                raise ValueError("Solde insuffisant")
            
        self.adherent = adherent
        self.salle = salle
        self.date = date
        self.heure = heure
        # On débite le solde de l'adhérent du prix de la réservation
        self.adherent.solde -= self.prix
        self.salle.reservations.append(self)