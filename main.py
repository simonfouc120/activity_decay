from datetime import datetime
import half_time_lib
import math
import numpy as np
import activity_decay_function as activity_func 

if __name__ == "__main__":    
    activity_func.print_activity_decay()
    isotope = input("Entrez le nom de l'isotope (ex. Cesium-137, Cobalt-60) : ")
    half_life = half_time_lib.get_half_life(isotope)

    if half_life is not None:
        A0 = float(input("Entrez l'activité initiale (en Bq) : "))
        initial_date_str = input("Entrez la date initiale (YYYY-MM-DD HH:MM:SS) : ")
        current_date_str = input("Entrez la date actuelle (YYYY-MM-DD HH:MM:SS) : ")

        initial_date = datetime.strptime(initial_date_str, "%Y-%m-%d %H:%M:%S")
        current_date = datetime.strptime(current_date_str, "%Y-%m-%d %H:%M:%S")
        t = (current_date - initial_date).total_seconds() / (365.25 * 24 * 3600)  # Convert seconds to years

        current_activity = activity_func.calculate_activity(A0, t, half_life)
        print(f"L'activité radioactive actuelle de {isotope} après {t:.2f} ans est de {current_activity} Bq.")
    else:
        print("Isotope non trouvé dans la bibliothèque.")
