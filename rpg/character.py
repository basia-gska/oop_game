class Character():

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None

    def describe(self):
        """Prints description of the character"""
        print(f'{self.name} is here!')
        print(self.description)

    def set_conversation(self, conversation):
        """Sets the conversation with the character"""
        self.conversation = conversation

    def talk(self):
        """The character talks to the player"""
        if self.conversation is not None:
            print(f'[{self.name} says]: {self.conversation}')
        else:
            print(f"{self.name} doesn't want to talk to you")

    def fight(self, combat_item):
        """The character fights with the player"""
        print(f"{self.name} doesn't want to fight with you")
        return True


class Enemy(Character):
    enemies_defeated = 0

    def __init__(self, name, description):
        super().__init__(name, description)
        self.weakness = None
        self.possesion = None

    def set_weakness(self, item):
        """Sets the weakness of the character"""
        self.weakness = item

    def get_weakness(self):
        """Returns a string containing the weakness of the character"""
        return self.weakness

    def set_possesion(self, item):
        """Sets the item that is carried by the character"""
        self.possesion = item

    def get_possesion(self):
        """Returns a string containing the item that is carried by the character"""
        return self.possesion

    def get_enemies_defeated(self):
        """Returns a number of defeated enemies"""
        return Enemy.enemies_defeated

    def fight(self, combat_item):
        """The character fights with the player"""
        if self.weakness == combat_item:
            print(f'You fend {self.name} off with the {combat_item}')
            Enemy.enemies_defeated += 1
            return True
        else:
            print(f'{self.name} crushes you, puny adventurer!')
            return False

    def steal(self):
        """The player steals from the character"""
        if self.possesion is not None:
            print(f'You take {self.possesion} from {self.name}.')
            self.possesion = None


class Friend(Character):

    def __init__(self, name, description):
        super().__init__(name, description)
        self.possession = None

    def set_possesion(self, item):
        """Sets the item that is carried by the character"""
        self.possesion = item

    def get_possesion(self):
        """Returns a string containing the item that is carried by the character"""
        return self.possesion

    def hug(self):
        """The player hugs the character """
        print(f'You hugged {self.name}.')
