'''
Created on 19 Oct 2021

@author: Rus1
'''

class Game:
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
    
class Scene:
    levelName = None
    levelId = None
    sceneLocation = None
    playerList = []
    
    
    def __init__(self, location, players):
        self.sceneLocation = location
        self.playerList = players
        
class Location:
    locationName = None
    locationId = None
    entityList = []
    
    def __init__(self, name, entities):