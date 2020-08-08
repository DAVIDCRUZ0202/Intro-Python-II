class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    #readable print statement
    def print_item_name(self):
        for name in self.name:
            print(name)
        print()
        