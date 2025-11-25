aliens = []
for alien_no in range (0,10):
    new_alien = {'color': 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

print(aliens)
print("----------------------------------------------------")
for alien in aliens[0:3]:
    alien['color'] = 'yellow'
    alien['points'] = 10
    alien['speed'] = 'medium'

print(aliens)
print("----------------------------------------------------")

for alien in aliens[6:10]:
    alien['color'] = 'red'
    alien['points'] = 15
    alien['speed'] = 'hyperfast'

print(aliens)
print("----------------------------------------------------")