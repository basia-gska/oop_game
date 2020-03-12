from room import Room
from character import Enemy, Friend
from item import Item

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining hall")
dining_hall.set_description('A spacious room with paintings on every wall')

ballroom = Room('Ballroom')
ballroom.set_description('An enormous room with three glass chandeliers and mirrors on every wall')

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, 'west')
ballroom.link_room(dining_hall, 'east')

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

catrina = Friend("Catrina", 'A friendly skeleton')
catrina.set_conversation('Oh, hello there.')
ballroom.set_character(catrina)

cheese = Item('cheese')
cheese.set_description('One awfully smelly piece of cheese')
kitchen.set_item(cheese)

current_room = kitchen
backpack = []

while True:
    new_room = False
    print()
    current_room.get_details()

    inhabitant = current_room.get_character()
    thing = current_room.get_item()

    if inhabitant is not None:
        inhabitant.describe()

    if thing is not None:
        thing.describe()

    while not new_room:
        print()
        print('What would you like to do?')
        command = input('>')

        if command in ['north', 'south', 'east', 'west']:
            current_room = current_room.move(command)
            new_room = True
            continue
        elif command == 'talk':
            if inhabitant is not None:
                inhabitant.talk()
        elif command == 'fight':
            if inhabitant is None or isinstance(inhabitant, Friend):
                print('There is no one to fight with.')
            else:
                print('What will you fight with? ')
                weapon = input('>')
                if weapon not in backpack:
                    print(f"Sorry, you don't have {weapon} in your backpack.")
                else:
                    if inhabitant.fight(weapon):
                        print('Good job! You won the fight!')
                        current_room.set_character(None)

                        if inhabitant.get_enemies_defeated() == 3:
                            print('You defeated all enemies. You won the game')
                            quit()
                        else:
                            print(f'Number of enemies defeated so far: {inhabitant.get_enemies_defeated()}')

                    else:
                        print('You die! Game over!')
                        quit()

        elif command == "hug":
            if inhabitant is None:
                print("There is no one here to hug.")
            else:
                if isinstance(inhabitant, Enemy):
                    print("I wouldn't do that if I were you...")
                else:
                    inhabitant.hug()
        elif command == 'take':
            if thing is None:
                print('There is nothing to take.')
            else:
                thing.take()
                backpack.append(thing.name)
                current_room.item = None
        elif command == 'backpack':
            print(backpack)
