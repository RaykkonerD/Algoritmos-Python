# Problema 1131 do Beecrowd -	Grenais

novoGrenal = 1
nGrenais = 0
interVit = 0
gremioVit = 0
empates = 0

while novoGrenal == 1:
    interGols, gremioGols = map(int, input().split())
    print('Novo grenal (1-sim 2-nao)')
    novoGrenal = int(input())
    
    if interGols > gremioGols:
        interVit += 1
    elif interGols < gremioGols:
        gremioVit += 1
    else:
        empates += 1
    
    nGrenais += 1
    
    
print(f'{nGrenais} grenais')
print(f'Inter:{interVit}')
print(f'Gremio:{gremioVit}')
print(f'Empates:{empates}')

if interVit > gremioVit:
    print('Inter venceu mais')
elif interVit < gremioVit:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')