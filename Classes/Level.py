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

class SceneBuilder:
    """
    Used to build custom scenes with specified attributes.
    """

    #List of playable characters.
    playerList = []
    def setPlayerList(self, players): self.playerList = players
    def addPlayer(self, player): self.playerList.append(player)

    #Location where the scene is taking place.
    sceneLocation = None
    def setLocation(self, location): self.sceneLocation = location

    #The current level# the scene is at. (unsigned integer)
    sceneLevel = None
    def setLevel(self, level): self.sceneLevel = level

    #The type of scene. (string) (e.g. Battle, Loot, Puzzle, Store, Talk)
    sceneType = None
    def setType(self, typeOfScene): self.sceneType = typeOfScene


    def build(self):
        """
        The constructor used to create custom scenes.

        Required attributes:
        - sceneLocation
        - sceneLevel
        - sceneType
        """

        #Raises an exception if an attribute is null.
        if self.sceneLocation == None: raise AttributeError
        if self.sceneLevel == None: raise AttributeError
        if self.sceneType == None: raise AttributeError

        scene = Scene()
        scene.location = self.sceneLocation
        scene.playerList = self.playerList
        scene.level = self.level
        scene.event = self.sceneType
        return scene

class Scene:
    level = None
    location = None
    playerList = []
    event = None



class Location:
    name = None
    entityList = []
