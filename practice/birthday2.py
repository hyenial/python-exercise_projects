import json

birthday = {}
with open('birthdays.json', 'r') as f:
          birthday = json.load(f)

def add_entry():
    name = input('Who do you want to add to the Birthday Dictionnary?\n').title()
    date = input('When is {} born?\n'.format(name))
    birthday[name] = date
    with open('birthdays.json', 'w') as f:
        json.dump(birthday, f)
    print('{} was added to my birthday list\n'.format(name))

def find_date():
    name = input("who's birthday do you want to know?\n").title()
    try :
        if birthday[name]:
            print('{} is born on {}\n'.format(name, birthday[name]))
    except KeyError:
        print('{} is not in the list\n'.format(name))

def list_entries():
    print('The current entries in my birthday list are:\n============================================')
    for key in birthday:
        print(key.ljust(31), ':', birthday[key])
    print()

while True:
    what_next = input('What do you want to do next? you can: Add, Find, List, Quit\n').capitalize()
    if what_next == 'Quit':
        print('Good Bye')
        raise SystemExit(0)
    elif what_next == 'Add':
        add_entry()
    elif what_next == 'Find':
        find_date()
    elif what_next == 'List':
        list_entries()
