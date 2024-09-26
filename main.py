from datetime import datetime
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
    return np.float32(A0 * (0.5 ** (t / half_life)))


if __name__ == "__main__":    
    isotope = input("Entrez le nom de l'isotope (ex. Cesium-137, Cobalt-60) : ")
    half_life = half_time_lib.get_half_life(isotope)

    if half_life is not None:
        A0 = float(input("Entrez l'activité initiale (en Bq) : "))
        initial_date_str = input("Entrez la date initiale (YYYY-MM-DD HH:MM:SS) : ")
        current_date_str = input("Entrez la date actuelle (YYYY-MM-DD HH:MM:SS) : ")

        initial_date = datetime.strptime(initial_date_str, "%Y-%m-%d %H:%M:%S")
        current_date = datetime.strptime(current_date_str, "%Y-%m-%d %H:%M:%S")
        t = (current_date - initial_date).total_seconds() / (365.25 * 24 * 3600)  # Convert seconds to years

        current_activity = calculate_activity(A0, t, half_life)
        print(f"L'activité radioactive actuelle de {isotope} après {t:.2f} ans est de {current_activity} Bq.")
    else:
        print("Isotope non trouvé dans la bibliothèque.")
