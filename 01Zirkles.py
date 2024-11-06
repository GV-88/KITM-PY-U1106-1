import random

names = {
    'a': 'akmuo',
    'p': 'popierius',
    'z': 'zirkles'
}

winConditions = {
    'a': 'z',
    'p': 'a',
    'z': 'p'
}

# keys = names.keys
keys = ['a','p','z']

playerVal = ''

while playerVal != 'n' and (not (playerVal in keys)):
    playerVal = input('[a]kmuo, [p]opierius, [z]irkles, [n]ebežaidžiam?...')
    if playerVal == 'n':
        print('viso gero')
        break
    
    computerVal = random.choice(keys)

    print(f'žaidėjas: {names[playerVal]}, kompiuteris: {names[computerVal]}')
    if winConditions[playerVal] == computerVal:
        print('laimėjo žaidėjas')
    elif winConditions[computerVal] == playerVal:
        print('laimėjo kompiuteris')
    else:
        print('lygiosios (?)')
    playerVal = '' # reset at the end of round

