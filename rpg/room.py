class Room:

    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_description(self, description):
        """Sets the description of the room"""
        self.description = description

    def get_description(self):
        """Returns a string containing the description of the room"""
        return self.description

    def set_name(self, name):
        """Sets the name of the room"""
        self.name = name

    def get_name(self):
        """Returns a string containing the name of the room"""
        return self.name

    def set_character(self, character):
        """Sets the character in the room"""
        self.character = character

    def get_character(self):
        """Returns a string containing the character that is in the room"""
        return self.character

    def set_item(self, item):
        """Sets the item  in the room"""
        self.item = item

    def get_item(self):
        """Returns a string containing the item that is in the room"""
        return self.item

    def describe(self):
        """Prints description of the room"""
        print(self.description)

    def link_room(self, room_to_link, direction):
        """Links the room to another in the given direction"""
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        """Prints all the details of the room"""
        print(self.name)
        print('*' * 20)
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f'The {room.get_name()} is {direction}')

    def move(self, direction):
        """Move player to the given direction"""
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
