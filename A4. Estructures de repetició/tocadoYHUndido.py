# Configuració del joc
configuracio = [
    ['x', 'x', '0', '0', '0', '0', 'x'],
    ['0', '0', 'x', '0', '0', '0', 'x'],
    ['0', '0', '0', '0', '0', '0', 'x'],
    ['0', 'x', 'x', 'x', '0', '0', 'x'],
    ['0', '0', '0', '0', 'x', '0', '0'],
    ['0', '0', '0', '0', 'x', '0', '0'],
    ['x', '0', '0', '0', '0', '0', '0']
]

# Coordenades d'entrada
x, y = map(int, input().split())  # Si vols provar-ho amb les coordenades del teu exemple, introdueix 1 1

# Accedir a les coordenades i determinar el contingut
contingut = configuracio[x][y]

# Determina el resultat basant-te en el contingut trobat
if contingut == '0':
    print('aigua')
elif contingut == 'x':
    print('vaixell')
else:
    print('Coordenades fora de límit')
