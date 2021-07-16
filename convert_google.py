import catch_exchange as ces
import json

def convert_to_DataTable():
    data = ces.read_data()
    
    new_format = {
        'cols': [],
        'rows': []
    }

    # columns
    new_format['cols'].append({'id': 'tl', 'label': 'Timeline', 'type': 'date'})

    for c in data['values']:
        new_format['cols'].append({'id': str(c), 'label': str(c), 'type': 'number'})

    # rows
    i = 0
    for t in data['timeline']:
        cel = {}
        line = {'c': []}
        cel['v'] = f'Date({t*1000})'
        #cel['f'] = '%d/%m/%Y'
        line['c'].append(cel)
        for c in data['values']:
            cel = {}
            if data['values'][c][i] == 0:
                data['values'][c][i] = 0.001
            cel['v'] = round(data['values'][c][i] / data['values'][c][0], 2)
            line['c'].append(cel)
        i = i + 1
        new_format['rows'].append(line)

    with open('dataTable.json', 'w') as writer:
        json.dump(new_format, writer)

    return new_format

if __name__ == "__main__":
    convert_to_DataTable()