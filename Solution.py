import csv

autok = []
with open('cars.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for sor in reader:
        sor['id'] = int(sor['id'])
        sor['year'] = int(sor['year'])
        sor['dailyPrice'] = int(sor['dailyPrice'])
        autok.append(sor)

foglalasok = []
with open('bookings.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for sor in reader:
        sor['id'] = int(sor['id'])
        sor['carId'] = int(sor['carId'])
        sor['totalPrice'] = int(sor['totalPrice'])
        foglalasok.append(sor)

adatok = []
for auto in autok:
    auto_foglalasok = [f for f in foglalasok if f['carId'] == auto['id']]
    adatok.append({
        'auto': auto,
        'foglalasok': auto_foglalasok
    })

for adat in adatok:
    auto = adat['auto']
    print(f"Autó: {auto['brand']} {auto['model']} ({auto['licensePlate']})")
    print(f"  Év: {auto['year']}, Napi díj: {auto['dailyPrice']} Ft")
    print("  Foglalások:")
    if adat['foglalasok']:
        for foglalas in adat['foglalasok']:
            print(f"    - ID: {foglalas['id']}, {foglalas['startDate']} - {foglalas['endDate']}, Ár: {foglalas['totalPrice']} Ft, Felhasználó: {foglalas['userUID']}")
    else:
        print("    Nincsenek foglalások az adott autóra.")
    print("-" * 50)

from export import export_berlesek_csv
export_berlesek_csv(adatok, 'exportalt_berlesek.csv')
