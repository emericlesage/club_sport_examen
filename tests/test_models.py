import pytest
from core.models import Adherent

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