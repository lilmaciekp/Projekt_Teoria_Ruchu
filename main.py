import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 6     # średnio 5 zgłoszeń
H_AVG = 3       # średni czas trwania rozmowy
T_TOTAL = 60    # czas trwania symulacji

import numpy as np


def generuj_ruch(lambda_param, h_sredni, t_symulacji):
    momenty_przyjscia = []
    aktualny_czas = 0
    while aktualny_czas < t_symulacji: #Generowanie momentów przyjścia połączeń
        odstep = np.random.exponential(1 / lambda_param)
        aktualny_czas += odstep
        if aktualny_czas < t_symulacji:
            momenty_przyjscia.append(aktualny_czas)

    czasy_trwania = np.random.exponential(h_sredni, len(momenty_przyjscia)) #Losowanie czasu trwania rozmów
    momenty_zakonczenia = [p + t for p, t in zip(momenty_przyjscia, czasy_trwania)] #Wyznaczanie momentów zakończenia

    return momenty_przyjscia, momenty_zakonczenia

przyjscia, zakonczenia = generuj_ruch(LAMBDA, H_AVG, T_TOTAL)
print(f"Wygenerowano {len(przyjscia)} połączeń.")