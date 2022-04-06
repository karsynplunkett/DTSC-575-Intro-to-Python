import sys

relations = {'Darth Vader':'father', 'Leia':'sister', 'Han':'brother in law', 'R2D2':'droid', 'Rey':'Padawan', 'Tatooine':'homeworld'}
def luke(relat):
    if relat == 'Darth Vader':
        print(f'No, I am your {relations["Darth Vader"]}')

    else:
        print(f'Luke, I am your {relations[relat]}')
        
        
luke(sys.argv[1])
