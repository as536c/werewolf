state = ['alive']

print(state)
state.remove('alive')
print(state)
state.append('dead')
print(state)
state.append('alive')
print(state)

if 'dead' in state:
    print('u is dead')
else:
    print('u is alive')