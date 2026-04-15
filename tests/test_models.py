import pytest
from core.models import Adherent
from core.models import Salle

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
    return Salle("Tennis", 4)

def test_salle_type(salle_test):
    # On vérifie que la salle est bien de type "Tennis"
    assert salle_test.type == "Tennis"

def test_salle_capacite(salle_test):
    # On vérifie que la salle est bien de capacité 4
    assert salle_test.capacite == 4

def test_places_restantes(salle_test):
    # On vérifie que le nombre de places restantes est égal à la capacité initiale
    assert salle_test.places_restantes == 4