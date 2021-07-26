import catch_exchange as ces
import json

def convert_to_DataTable(period):
    period = int(period)

    data = ces.read_data()
    
    new_format = {
        'cols': [],
        'rows': []
    }

    # columns
    new_format['cols'].append({'id': 'tl', 'label': 'Timeline', 'type': 'date'})

    del data['values']['XDR']
    countries = list(data['values'].keys())
    countries.sort()

    for c in countries:
        new_format['cols'].append({'id': str(c), 'label': str(c), 'type': 'number'})

    # rows
    for c in data['values']:
        data['values'][c] = data['values'][c][-period:]
    data['timeline'] = data['timeline'][-period:]

    i = 0
    for t in data['timeline']:
        cel = {}
        line = {'c': []}
        cel['v'] = f'Date({t*1000})'
        #cel['f'] = '%d/%m/%Y'
        line['c'].append(cel)
        for c in countries:
            cel = {}
            if data['values'][c][i] == 0:
                data['values'][c][i] = 0.001
            cel['v'] = round(data['values'][c][i] / data['values'][c][0], 2)
            line['c'].append(cel)
        i = i + 1
        new_format['rows'].append(line)

    return new_format

def continents():
    continent = {
        "america": ['ANG', 'ARS', 'AWG', 'BBD', 'BMD', 'BOB', 'BRL', 
				'BSD', 'BZD', 'CAD', 'CLP', 'COP', 'CRC', 'CUC', 'CUP', 'DOP', 'FKP', 
				'GTQ', 'GYD', 'HNL', 'HTG', 'JMD', 'KYD', 'MXN', 'NIO', 'PAB', 'PEN', 
				'PYG', 'SRD', 'TTD', 'USD', 'UYU', 'VES', 'XCD'],
		"asia": ['AED', 'AFN', 'AMD', 'AZN', 'BDT', 'BHD', 'BND', 'BTN', 'CNY', 
				'EGP', 'ERN', 'GEL', 'HKD', 'IDR', 'ILS', 'INR', 'IQD', 'IRR', 'JOD', 
				'JPY', 'KGS', 'KHR', 'KRW', 'KWD', 'KZT', 'LAK', 'LBP', 'LKR', 'MMK', 
				'MNT', 'MOP', 'MVR', 'MYR', 'NPR', 'OMR', 'PHP', 'PKR', 'QAR', 'RUB', 
				'SAR', 'SGD', 'SYP', 'THB', 'TJS', 'TMT', 'TWD', 'UZS', 'VND', 'YER'],
		"africa": ['AOA', 'BIF', 'BWP', 'CDF', 'CVE', 'DJF', 'DZD', 'EGP', 'ETB', 
				'GHS', 'GNF', 'KES', 'KMF', 'LRD', 'LSL', 'LYD', 'MAD', 'MGA', 'MRU', 
				'MUR', 'MWK', 'MZN', 'NAD', 'NGN', 'RWF', 'SCR', 'SDG', 'SHP', 'SLL', 
				'SOS', 'SSP', 'STN', 'SZL', 'TND', 'TZS', 'UGX', 'XAF', 'XOF', 'ZAR', 'ZMW'],
		"europe": ['ALL', 'AZN', 'BAM', 'BGN', 'BYN', 'CHF', 'CZK', 'DKK', 'EUR', 
				'FOK', 'GBP', 'GEL', 'GGP', 'GIP', 'GMD', 'HRK', 'HUF', 'IMP', 'ISK', 
				'MDL', 'MKD', 'NOK', 'PLN', 'RON', 'RSD', 'RUB', 'SEK', 'TRY', 'UAH'],
		"oceania": ['AUD', 'FJD', 'KID', 'NZD', 'PGK', 'SBD', 'TOP', 'TVD', 'VUV', 
				'WST', 'XPF']
    }

    return continent


if __name__ == "__main__":
    print("TESTS")
    i = int(input())
    print(convert_to_DataTable(i))
    #print(series())