from datetime import date
import requests
import json
import re
from requests.exceptions import HTTPError


def kwota_walidacja(kwota):
    try:
        float(kwota)
    except ValueError:
        print("Niepoprawny format.")
        return 0
    return 1


def waluta_walidacja(waluta):
    waluty = ['usd', 'eur', 'gbp']

    if waluta in waluty:
        return 1
    else:
        print("Nieobsługiwana waluta.")
        return 0


def data_walidacja(data):
    try:
        date.fromisoformat(data)
        return 1
    except ValueError:
        print("Niepoprawny format daty.")
        return 0


def main():
    # wprowadzanie danych faktury
    print("Wpisz dane do faktury")

    while True:
        fakturaKwota = input("Podaj kwotę: ")
        fakturaKwota = re.sub("\,", ".", fakturaKwota)  # dozwolony jest format z przecinkiem
        with open("faktury.txt", "a") as f:
            f.write(fakturaKwota + "|")

        if kwota_walidacja(fakturaKwota):
            break

    while True:
        fakturaWaluta = input("Podaj walutę [EUR/USD/GBP]: ")
        fakturaWaluta = fakturaWaluta.lower()  # dozwolony jest format z duzych liter
        with open("faktury.txt", "a") as f:
            f.write(fakturaWaluta + "|")

        if waluta_walidacja(fakturaWaluta):
            break

    while True:
        fakturaData = input("Wprowadź datę [rrrr-mm-dd]: ")

        if data_walidacja(fakturaData):
            print("\nPomyślnie wprowadzono dane faktury. \n")
            with open("faktury.txt", "a") as f:
                f.write(fakturaData + "\n")
                f.close()
            break

    # wprowadzanie danych płatności
    print("Podaj dane płatności")

    while True:
        przelewKwota = input("Podaj kwotę: ")

        if kwota_walidacja(przelewKwota):
            with open("przelewy.txt", "a") as f:
                f.write(przelewKwota + "|")
            break

    while True:
        przelewWaluta = input("Podaj walutę [EUR/USD/GBP]: ")

        if waluta_walidacja(przelewWaluta):
            with open("przelewy.txt", "a") as f:
                f.write(przelewWaluta + "|")
            break

    while True:
        przelewData = input("Wprowadź datę [rrrr-mm-dd]: ")

        if data_walidacja(przelewData):
            print("\nPomyślnie wprowadzono dane płatności. \n")
            with open("przelewy.txt", "a") as f:
                f.write(przelewData + "\n")
                f.close()
            break

    # Skorzystamy z NBP API aby pobrać kursy walut
    urlPrzelew = f"http://api.nbp.pl/api/exchangerates/rates/a/{przelewWaluta}/{przelewData}/"
    response = requests.get(urlPrzelew)
    if response.status_code == 200:
        przelewKurs = json.dumps(
            response.json()['rates'][0]['mid'],
            indent=4,
            sort_keys=True)
        print("kurs " + przelewWaluta + " z przelewu w dniu: " + przelewData + " jest rowny:", przelewKurs+" | kwota w PLN:", float(przelewKurs)*float(przelewKwota))
    # pobieramy kurs waluty w dniu wystawienia fakrtury
    urlFaktura = f"http://api.nbp.pl/api/exchangerates/rates/a/{fakturaWaluta}/{fakturaData}/"
    response = requests.get(urlFaktura)
    if response.status_code == 200:
        fakturaKurs = json.dumps(
            response.json()['rates'][0]['mid'],
            indent=4,
            sort_keys=True)
        print("kurs " + fakturaWaluta + " z faktury w dniu: " + fakturaData + " jest rowny: ", fakturaKurs+" | kwota w PLN:", float(fakturaKurs)*float(fakturaKwota))

    # obliczamy różnicę kursów
    roznica = float(przelewKurs)*float(przelewKwota) - float(fakturaKurs)*float(fakturaKwota)
    print("Różnica kursów wynosi: ", round(abs(roznica),2)+" PLN")


if __name__ == "__main__":
    main()
