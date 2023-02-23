votes = [1,1,5,2,3]
if votes.count(max(votes)) == 1:
    voteres = 'p'+str(votes.index(max(votes))+1)+'dead'
    print(voteres.encode('utf-8'))
else:
    print('tie')