# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, location):
        self.location = location
        self.inventory = []
    #readable print statement
    def __str__(self):
        return f"Location: {self.location}"

    def item_pickup(self, thing):
        self.inventory.append(thing)

    def item_drop(self, thing):
         self.inventory.remove(thing)