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

