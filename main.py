from decorators import country_capital


@country_capital
def search_country(capital_city=None):
    return 'No es ciudad capital de un pais.'


print(search_country("bogota"))
