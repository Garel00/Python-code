favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for friends in favorite_languages.keys():
    print(f"{friends.title()}, thank you for taking the poll.")

all_friends = []
for friends in favorite_languages.keys():
    all_friends.append(friends)

all_friends.append('luis')
all_friends.append('hetor')

for people in all_friends:
    if people not in favorite_languages.keys():
        print(f"{people.title()}, please take the poll.")