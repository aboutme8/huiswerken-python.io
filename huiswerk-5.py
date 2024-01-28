menu= {'maandag': 'spagety',
       'dinsdag': 'reist met groenten en kip',
       'woensdag': 'fritten met stoofvlees',
       'donderdag': 'pataten met bufstek en bonen',
       'vrijdag': 'paela',
       'zaterdag': 'coucous',
       'zondag': 'tajine'}
print(menu)

try:
    menu=int(input('Welke dag wil je komen?  '))
    menu= -1
    print('Gereserveerd.')
except ValueError:
    print('Geef enkel een dag aan.')
finally:
    print('Enkel reserveren op de maand zelf. Dank u.')
