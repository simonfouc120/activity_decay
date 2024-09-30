import csv
import os

def get_all_half_life_data():
    """
    Retourne toutes les données de demi-vie.
    :return: dictionnaire contenant toutes les demi-vies
    """
    data = {}
    file_path = os.path.join(os.path.dirname(__file__), '../data/half_life.csv')
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            isotope = row['symbol']
            number = int(row['z']) + int(row['n'])
            half_life_str = row['half_life']
            try:
                half_life = float(half_life_str)
                data[isotope + str(number)] = half_life
            except ValueError:
                print(f"Warning: Could not convert half-life value '{half_life_str}' for isotope '{isotope}' to float.")
    return data

def get_half_life(isotope):
    """
    Retourne la demi-vie de l'isotope en années, si elle est disponible.
    :param isotope: nom de l'isotope (string)
    :return: demi-vie en années (float) ou None si l'isotope n'est pas trouvé
    """
    data = get_all_half_life_data()
    return data.get(isotope)
    