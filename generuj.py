import os
import json

# Foldery do skanowania
FOLDERY = ['sprawdziany', 'notatki', 'zdjecia', 'inne']

wynik = {}

for folder in FOLDERY:
    if os.path.isdir(folder):
        pliki = []
        for nazwa in sorted(os.listdir(folder)):
            sciezka = os.path.join(folder, nazwa)
            if os.path.isfile(sciezka) and not nazwa.startswith('.'):
                pliki.append(f'{folder}/{nazwa}')
        wynik[folder] = pliki
    else:
        wynik[folder] = []

with open('pliki.json', 'w', encoding='utf-8') as f:
    json.dump(wynik, f, ensure_ascii=False, indent=2)

print('Wygenerowano pliki.json:')
for folder, pliki in wynik.items():
    print(f'  {folder}: {len(pliki)} plik(ów)')
