import wroles
votes = [1,1,5,2,3]
if votes.count(max(votes)) == 1:
    voteres = 'p'+str(votes.index(max(votes))+1)+'dead'
    print(voteres.encode('utf-8'))
else:
    print('tie')

rolesend = 'doctor seer hunter villager alpha '
rolesplit = rolesend.strip(' ').split(' ',4)
r1 = 1
for r in rolesplit:
    if r == 'villager':
        wroles.role[r1] = wroles.villager
    elif r == 'doctor':
        wroles.role[r1] = wroles.doctor
    elif r == 'seer':
        wroles.role[r1] = wroles.seer
    elif r == 'hunter':
        wroles.role[r1] = wroles.hunter
    elif r == 'fool':
        wroles.role[r1] = wroles.fool
    elif r == 'wolf':
        wroles.role[r1] = wroles.wolf
    elif r == 'alpha':
        wroles.role[r1] = wroles.alpha
    elif r == 'wolftrickster':
        wroles.role[r1] = wroles.wolftrickster
    r1 += 1
print(wroles.role)