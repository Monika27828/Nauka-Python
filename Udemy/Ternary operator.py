itRains = True

if itRains:
    print('We stay at home')
else:
    print('We go out')

lub

print('We stay at home' if itRains else 'We go out')

Zadanie:
musclePain = False
fever = True
weakness = True
print('Suspicion of influenza' if musclePain and fever and weakness else 'The flu is unlikely')

if musclePain and fever and weakness:
    print('Suspicion of influenza!')
elif weakness and not musclePain and fever:
    print('Just take a rest')
else:
    print('You may be cold')

isMan = True
if musclePain and fever and weakness or isMan and(musclePain or fever or weakness):
    print('Suspicion of influenza!')
elif not (musclePain and fever) or weakness:
    print('Just take a rest!')
else:
    print('You may be cold')

