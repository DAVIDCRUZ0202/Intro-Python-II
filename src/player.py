# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, location):
        self.location = location
    #readable print statement
    def __str__(self):
        return f"Location: {self.location}"