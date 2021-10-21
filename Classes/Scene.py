'''
Created on 19 Oct 2021

@author: Rus1
'''

"""
Scene
- Player(s)
-- Type/class
--- Special ability

-- Inventory
--- Item
---- Type
----- ¹

-- Numerical stats (Health, Mana, etc)
--- Current stat value
--- Max stat value
--- Stat modifiers*
---- Stat multiplier*²
---- Stat booster*³

- Location
-- Character(s)⁴
--- Relation to player(s)
--- Numerical stats⁵
--- Inventory⁵
-- Weather*

* To be added later
¹ Each type of item has a different set of info. For example, the type is a weapon, it'll have a damage stat. If it's a consumable, it'll have a heal stat.
⁴ The character that the players will encounter in a given location.
⁵ Same contents as the player's.
"""
class Scene:
    """
    """
    def __init__(self, level = 1, location = None, players = [], event = None):
        self.sceneLevel = level
        self.sceneLocation = location
        self.playerList = players
        self.sceneEvent = event

    #List of playable characters.
    def setPlayerList(self, players): self.playerList = players
    def addPlayer(self, player): self.playerList.append(player)
    def getPlayerList(self): return self.playerList
    def getPlayer(self):
        if (entityList.size() == 1): return self.__entityList[0]

    #Location where the scene is taking place.
    def setLocation(self, location): self.sceneLocation = location
    def getLocation(self): return self.sceneLocation

    #The current level# the scene is at. (unsigned integer)
    def setLevel(self, level): self.sceneLevel = level
    def getLevel(self): return self.sceneLevel

    #The event in the scene. (string) (e.g. Battle, Loot, Puzzle, Store, Talk)
    def setEvent(self, event): self.sceneEvent = event
    def getEvent(self): return self.sceneEvent

if __name__ == "__main__":
    from main.PremadeObjects import randomName
    from Location import Location
    scene = Scene()
    scene.setLocation(Location(randomName("location")))
    scene.setPlayerList([randomName("character"), randomName("character"), randomName("character")])
    scene.setLevel(1)
    scene.setEvent("Nice event")

    print(f"Location: {scene.getLocation().getName()}\nPlayer list: {scene.getPlayerList()}\nLevel: {scene.getLevel()}\nEvent: {scene.getEvent()}")
