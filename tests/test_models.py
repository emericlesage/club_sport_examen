import pytest
from core.models import Adherent, Salle, TypeSalle, Reservation

@pytest.fixture
# Crée un adhérent pour les tests
def adherent_test():
    return Adherent("Bob", 50, est_abonne=True)

def test_est_abonne(adherent_test):
    # On vérifie que l'adhérent est bien abonné
    assert adherent_test.est_abonne == True

def test_solde_restant(adherent_test):
    # On vérifie le solde restant de l'adhérent
    assert adherent_test.solde_restant == 50

@pytest.fixture
# Créé une salle de tennis pour 4 personnes
def salle_test():
    return Salle(TypeSalle.TENNIS, 4)

def test_salle_type(salle_test):
    # On vérifie que la salle est bien de type "Tennis"
    assert salle_test.type_salle == TypeSalle.TENNIS

def test_salle_capacite(salle_test):
    # On vérifie que la salle est bien de capacité 4
    assert salle_test.capacite == 4

def test_places_restantes(salle_test):
    # On vérifie que le nombre de places restantes est égal à la capacité initiale
    assert salle_test.places_restantes == 4

def test_creation_reservation_valide(adherent_test, salle_test):
    # On crée une réservation valide pour l'adhérent et la salle
    reservation = Reservation(adherent_test, salle_test, "2026-04-15", "14:00", prix=11)
    assert reservation.prix == 11
    assert reservation.adherent == adherent_test
    assert reservation.salle.type_salle.value == TypeSalle.TENNIS.value

def test_creation_reservation_invalide(adherent_test, salle_test):
    # On tente de créer une réservation avec un prix excessif, ce qui devrait lever une exception
    with pytest.raises(ValueError):
        Reservation(adherent_test, salle_test, "2026-04-15", "14:00", prix=100)

@pytest.mark.parametrize("sport, est_abonne, prix_attendu", [
    (TypeSalle.TENNIS, True, 11),
    (TypeSalle.TENNIS, False, 30),
    (TypeSalle.BADMINTON, True, 10),
    (TypeSalle.BADMINTON, False, 20),
    (TypeSalle.SQUASH, True, 9),
    (TypeSalle.SQUASH, False, 15)
])
def test_prix_reservation(sport, est_abonne, prix_attendu):
    # On créé un adhérent avec le statut d'abonnement
    adherent_test = Adherent("Bob", 50, est_abonne=est_abonne)
    # On créé une salle
    salle_test = Salle(sport, 4)
    # On créé une réservation
    reservation = Reservation(adherent_test, salle_test, "2026-04-15", "14:00")
    # On vérifie que le prix de la réservation correspond au prix attendu
    assert reservation.prix == prix_attendu