import math
import numpy as np

# Do a function that do a print of "Activity Decay " in the terminal but in very large and with a frame arount 

def print_activity_decay():
    message = "Activity Decay Calculator"
    border = "*" * (len(message) + 16)
    print("\n")
    print(border)
    print(f"******* {message} *******")
    print(border, "\n")
    return


def calculate_activity(A0, t, half_life):
    """
    Calcule l'activité radioactive actuelle.
    :param A0: activité initiale (float)
    :param t: temps écoulé (en années) (float)
    :param half_life: demi-vie de l'isotope (en années) (float)
    :return: activité radioactive actuelle (float)
    """
    return np.float32(A0 * (0.5 ** (t / half_life)))

