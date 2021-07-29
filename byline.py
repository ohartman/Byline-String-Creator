from typing import List

example_bylines = {
    'authors': [
        {
            'firstName': 'jonah',
            'middleName': 'Engel',
            'lastName': 'bromwich',
            'block': {
                '__typename': 'Bold'
            }
        },
        {'random': 'node'},
        {},
        {
            'firstName': 'matthew',
            'middleName': '',
            'lastName': 'sChneier',
            'block': {
                '__typename': 'Italics'
            }
        },
        {
            'firstName': 'Niraj',
            'middleName': '',
            'lastName': 'chokshi',
            'block': {}
        }
    ]
}

def create_byline_string(bylines: dict[str, List]) -> str:
    # TODO
    output = 'By '
    conjunction = ', '
    while len(bylines['authors']) != 0:
        if len(bylines['authors'])==1:
            conjunction = ''
            output = output + 'and'
        line = bylines['authors'].pop(0)
        if 'firstName' in line.keys():
            if line['middleName'] != '':
                if line.get('block', {}).get('__typename') == 'Bold':
                    output  = output + '<strong>' + line['firstName'].capitalize() + '/strong> ' + line['middleName'].capitalize() + ' ' + line['lastName'].capitalize() + conjunction
                elif line.get('block', {}).get('__typename') == 'Italics':
                    output  = output + '<em>' + line['firstName'].capitalize() + '/em> ' + line['middleName'].capitalize() + ' ' + line['lastName'].capitalize() + conjunction
                else:
                    output  = output + ' ' + line['firstName'].capitalize() + ' ' + line['middleName'].capitalize() + ' ' + line['lastName'].capitalize() + conjunction
            else:
                if line.get('block', {}).get('__typename') == 'Bold':
                    output  = output + '<strong>' + line['firstName'].capitalize() + '/strong> ' + line['lastName'].capitalize() + conjunction
                elif line.get('block', {}).get('__typename') == 'Italics':
                    output  = output + '<em>' + line['firstName'].capitalize() + '/em> ' + line['lastName'].capitalize() + conjunction
                else:
                    output  = output + ' ' + line['firstName'].capitalize() + ' ' + line['lastName'].capitalize() + conjunction
    return output
                        






                    

print(create_byline_string(example_bylines))
