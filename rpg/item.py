class Item:

    def __init__(self, name):
        self.name = name
        self.description = None

    def set_description(self, description):
        """Sets the description of the item"""
        self.description = description

    def get_description(self):
        """Returns a string containing the description of the item"""
        return self.description

    def set_name(self, name):
        """Sets the name of the item"""
        self.name = name

    def get_name(self):
        """Returns a string containing the name of the item"""
        return self.name

    def describe(self):
        """Prints description of the item"""
        print(f'{self.name} is here. {self.description}')


    def take(self):
        """Player takes the item"""
        print(f'{self.name} was taken')


    def use(self):
        """Player uses the item"""
        print(f'{self.name} can be used now')