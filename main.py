import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 5      # średnio 5 zgłoszeń na minutę
H_AVG = 3       # średni czas trwania rozmowy w minutach
T_TOTAL = 60    # czas trwania symulacji (np. 1 godzina) [cite: 23]

import numpy as np


def generuj_ruch(lambda_param, h_sredni, t_symulacji):
    momenty_przyjscia = []
    aktualny_czas = 0
    while aktualny_czas < t_symulacji:
        odstep = np.random.exponential(1 / lambda_param)
        aktualny_czas += odstep
        if aktualny_czas < t_symulacji:
            momenty_przyjscia.append(aktualny_czas)

    # 2. Losujemy czas trwania każdej rozmowy
    czasy_trwania = np.random.exponential(h_sredni, len(momenty_przyjscia))

    # 3. Wyznaczamy kiedy połączenia się kończą
    momenty_zakonczenia = [p + t for p, t in zip(momenty_przyjscia, czasy_trwania)]

    return momenty_przyjscia, momenty_zakonczenia

przyjscia, zakonczenia = generuj_ruch(LAMBDA, H_AVG, T_TOTAL)
print(f"Wygenerowano {len(przyjscia)} połączeń.")