
import requests

value = int(input("Enter the EUR amount: "))

r = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
#print(r.json())

eurCurr = 0

for elem in r.json():
    #print(f" Currency {elem['cc']} with Rate {elem['rate']}")
    if (elem['cc'] == 'EUR'):
        eurCurr = elem['rate']

print(eurCurr)

print(f"Result of {value} in USD to UAH = {eurCurr*value}")
