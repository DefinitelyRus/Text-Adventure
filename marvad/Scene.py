'''
Created on 19 Oct 2021
@author: DefinitelyRus
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
    def __init__(self, level, type, maxTurns = 10, location = None, players = [], event = None, entities = []):
        self.sceneLevel = level
        self.sceneType = type
        self.sceneTurn = 0
        self.sceneMaxTurns = maxTurns
        self.sceneLocation = location
        self.playerList = players
        self.sceneEvent = event

    #Scene Level INT: A required parameter. This will serve as the level counter.
    #This can also be internally referred to as Scene ID.
    def setSceneLevel(self, level): self.sceneLevel = level
    def getSceneLevel(self): return self.sceneLevel

    #Scene Type STRING: A required parameter. This indicated what kind of scene this object is, whether it's "combat", "scripted", "shop", "dialogue", or "minigame".
    #Each one will determine what set of ExecutableAction cards will be available to the player. For example, a combat scene would only allow usage of CombatCards by default, while a shop scene would only allow ShopCards.
    def setSceneType(self, type): self.sceneType = type
    def getSceneType(self): return self.sceneType

    #Player OBJECT List: List of playable characters.
    def setPlayerList(self, players): self.playerList = players
    def addPlayer(self, player): self.playerList.append(player)
    def getPlayerList(self): return self.playerList
    def getPlayer(self):
        if (entityList.size() == 1): return self.__entityList[0]

    #Location OBJECT: Location where the scene is taking place.
    def setLocation(self, location): self.sceneLocation = location
    def getLocation(self): return self.sceneLocation

    #Event STRING: The event in the scene. (e.g. Battle, Loot, Puzzle, Store, Talk)
    def setEvent(self, event): self.sceneEvent = event
    def getEvent(self): return self.sceneEvent

    #Max Turn INT: The max number of turns before proceeding to the next turn.
    def setMaxTurns(self, maxTurns): self.sceneMaxTurns = maxTurns
    def getMaxTurns(self): return self.sceneMaxTurns

    #INT: The current turn the scene is on.
    def turnPlusOne(self): self.sceneTurn += 1
    def setTurnCount(self, turn): self.sceneTurn = turn
    def getTurnCount(self): return self.sceneTurn
    def nextTurn(self, targetList):
        for target in targetList:
            target.executeEffects()
            #NOTE: Might want to add more stuff here.

        self.turnPlusOne()
        if (self.sceneTurn >= self.sceneMaxTurns):
            return false
        else: return true
