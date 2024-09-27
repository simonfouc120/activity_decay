
half_life_data = {
    # Isotopes communs
    "Cesium-137": 30.17,  # en années
    "Cobalt-60": 5.27,    # en années
    
    # Isotopes utilisés en médecine
    "Iode-131": 0.021,    # 8 jours (0.021 ans)
    "Technétium-99m": 0.000104,  # 6.01 heures (0.000104 ans)
    "Fluor-18": 0.002,    # 109.7 minutes (0.002 ans)
    
    # Isotopes utilisés pour la datation
    "Carbone-14": 5730,   # en années
    "Uranium-238": 4.468e9,  # 4.468 milliards d'années
    "Uranium-235": 7.04e8,  # 704 millions d'années
    "Thorium-232": 1.405e10,  # 14.05 milliards d'années
    "Potassium-40": 1.248e9,  # 1.248 milliards d'années
    
    # Isotopes de l'industrie
    "Americium-241": 432.2,   # en années
    "Plutonium-239": 24100,   # en années
    "Radium-226": 1600,       # en années
    "Strontium-90": 28.79,    # en années
    
    # Isotopes pour la recherche scientifique
    "Beryllium-10": 1.39e6,   # 1.39 millions d'années
    "Calcium-41": 1.03e5,     # 103,000 ans
    "Chlore-36": 3.01e5,      # 301,000 ans
    
    # Autres isotopes couramment étudiés
    "Tritium (Hydrogène-3)": 12.32,   # en années
    "Polonium-210": 0.3791,  # 138.4 jours (0.3791 ans)
    "Radon-222": 0.000092,   # 3.8 jours (0.000092 ans)
    "Francium-223": 0.000064,  # 22 minutes (0.000064 ans)
    "Plutonium-238": 87.7,    # en années
    "Neptunium-237": 2.144e6, # 2.144 millions d'années
    "Thorium-228": 1.91,      # en années
    "Uranium-234": 245500,    # en années
    "Radium-223": 0.004,      # 11.43 jours (0.004 ans)

    # Autres isotopes utilisés dans la radiothérapie
    "Iode-125": 0.207,        # 59.4 jours (0.207 ans)
    "Iridium-192": 0.213,     # 74 jours (0.213 ans)
    "Palladium-103": 0.034,   # 17 jours (0.034 ans)
    
    # Isotopes pour les générateurs thermiques radio-isotopiques
    "Plutonium-244": 8.08e7,  # 80.8 millions d'années
    "Curium-244": 18.1,       # en années
    "Curium-245": 8500,       # en années
    
    # Isotopes produits artificiellement dans les réacteurs
    "Neptunium-239": 0.00236,  # 2.36 jours (0.00236 ans)
    "Prométhium-147": 2.62,    # en années
    "Einsteinium-252": 1.29,   # en années
    "Fermium-257": 100.5,      # en jours (0.275 ans)

    # Isotopes rares et exotiques
    "Dubnium-268": 0.0037,  # 4.8 heures (0.0037 ans)
    "Livermorium-293": 0.000001,  # 0.0026 secondes (~3e-9 ans)
    "Oganesson-294": 0.000001,  # 0.7 millisecondes (~2e-10 ans)
}

def get_half_life(isotope):
    """
    Retourne la demi-vie de l'isotope en années, si elle est disponible.
    :param isotope: nom de l'isotope (string)
    :return: demi-vie en années (float) ou None si l'isotope n'est pas trouvé
    """
    return half_life_data.get(isotope)

def get_all_half_life_data():
    """
    Retourne toutes les données de demi-vie.
    :return: dictionnaire contenant toutes les demi-vies
    """
    return half_life_data