import half_time_lib
import math
import numpy as np

def calculate_activity(A0, t, half_life):
    """
    Calcule l'activité radioactive actuelle.
    :param A0: activité initiale (float)
    :param t: temps écoulé (en années) (float)
    :param half_life: demi-vie de l'isotope (en années) (float)
    :return: activité radioactive actuelle (float)
    """
    return A0 * (0.5 ** (t / half_life))

# Exemple d'utilisation
if __name__ == "__main__":
    # Demander à l'utilisateur de choisir un isotope
    isotope = input("Entrez le nom de l'isotope (ex. Cesium-137, Cobalt-60) : ")

    # Obtenir la demi-vie de l'isotope
    half_life = half_time_lib.get_half_life(isotope)

    if half_life is not None:
        # Demander l'activité initiale et le temps écoulé
        A0 = float(input("Entrez l'activité initiale (en Bq) : "))
        t = float(input("Entrez le temps écoulé (en années) : "))

        # Calculer l'activité radioactive actuelle
        current_activity = calculate_activity(A0, t, half_life)
        print(f"L'activité radioactive actuelle de {isotope} après {t} ans est de {current_activity} Bq.")
    else:
        print("Isotope non trouvé dans la bibliothèque.")