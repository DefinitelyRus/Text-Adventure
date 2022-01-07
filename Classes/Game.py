'''
Created on 19 Oct 2021

@author: Rus1
'''

class Game:
    #TODO: Get Game into a usable state.
    """
    This contains all the data about any ongoing game.
    To start a game, a Game object has to be created, only needing to specify
    how many levels are to be played. The rest is handled automatically upon
    the creation of the Game object (inside __init__).
    """
    id = None
    length = None
    levelList = []

    def __init__(self, gameLength):
        self.id = None
        self.length = gameLength

        for i in range(self.length):
            self.locationList.append(Scene(Location(randomName("location"))))






def randomName(self, nameForWhat):
    import random

    locationNames = ["Test1", "Test2", "Test3"]

    if nameForWhat == "location": return random.choice(locationNames)
