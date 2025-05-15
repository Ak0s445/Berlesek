import csv

def export_berlesek_csv(adatok, fajlnev):
    with open(fajlnev, 'w', newline='', encoding='utf-8') as f:
        fieldnames = [
            'carId', 'brand', 'model', 'licensePlate', 'year', 'dailyPrice',
            'bookingId', 'startDate', 'endDate', 'totalPrice', 'userUID'
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for adat in adatok:
            auto = adat['auto']
            foglalasok = adat['foglalasok']

            if foglalasok:
                for f in foglalasok:
                    writer.writerow({
                        'carId': auto['id'],
                        'brand': auto['brand'],
                        'model': auto['model'],
                        'licensePlate': auto['licensePlate'],
                        'year': auto['year'],
                        'dailyPrice': auto['dailyPrice'],
                        'bookingId': f['id'],
                        'startDate': f['startDate'],
                        'endDate': f['endDate'],
                        'totalPrice': f['totalPrice'],
                        'userUID': f['userUID']
                    })
            else:
                writer.writerow({
                    'carId': auto['id'],
                    'brand': auto['brand'],
                    'model': auto['model'],
                    'licensePlate': auto['licensePlate'],
                    'year': auto['year'],
                    'dailyPrice': auto['dailyPrice'],
                    'bookingId': '',
                    'startDate': '',
                    'endDate': '',
                    'totalPrice': '',
                    'userUID': ''
                })
