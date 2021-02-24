import requests


def country_capital(function):
    def wrapper(capital):
        response = requests.get(f"https://restcountries.eu/rest/v2/capital/{capital}")

        if response.status_code != 404:
            return response.content
        else:
            return function()

    return wrapper
