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
    def __init__(self, level = 1, maxTurns = 10, location = None, players = [], event = None):
        self.sceneLevel = level
        self.sceneMaxLevel = 20
        self.sceneTurn = 0
        self.sceneMaxTurns = maxTurns
        self.sceneLocation = location
        self.playerList = players
        self.sceneEvent = event

    #Player OBJECT List: List of playable characters.
    def setPlayerList(self, players): self.playerList = players
    def addPlayer(self, player): self.playerList.append(player)
    def getPlayerList(self): return self.playerList
    def getPlayer(self):
        if (entityList.size() == 1): return self.__entityList[0]

    #Location OBJECT: Location where the scene is taking place.
    def setLocation(self, location): self.sceneLocation = location
    def getLocation(self): return self.sceneLocation

    #INT: The current level# the scene is at.
    def setLevel(self, level): self.sceneLevel = level
    def getLevel(self): return self.sceneLevel
    def nextLevel(self, game):
        self.sceneLevel += 1
        if (self.sceneLevel >= self.sceneMaxLevel):
            #NOTE: Might wanna insert some stuff here.
            game.nextScene()

    #STRING: The event in the scene. (e.g. Battle, Loot, Puzzle, Store, Talk)
    def setEvent(self, event): self.sceneEvent = event
    def getEvent(self): return self.sceneEvent

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
            self.nextLevel()


if __name__ == "__main__":
    #Everything here is temporary and is to be deleted before release.
    from main.PremadeObjects import randomName
    from Location import Location
    scene = Scene()
    scene.setLocation(Location(randomName("location")))

    from Player import Player, PlayerClass
    from CombatCard import CombatCard
    from PlayerActions import ExecutableAction
    from Enemy import Enemy, EnemyClass

    playerClass1 = PlayerClass("custom", 30)
    exeAct1 = ExecutableAction("Attack")
    cc1 = CombatCard("Basic Attack", [], exeAct1, 15)
    playerClass1.addCombatCard(cc1)
    player1 = Player("Rus", playerClass1, None)

    scene.addPlayer(player1)
    scene.setLevel(1)
    scene.setEvent("Nice event")

    print(f"Location: {scene.getLocation().getName()}")
    print(f"Player list: {scene.getPlayerList()[0].getName()}")
    print(f"Level: {scene.getLevel()}")
    print(f"Event: {scene.getEvent()}\n")

    enemyClass1 = EnemyClass("custom", 40)
    enemy1 = Enemy("Cunt", enemyClass1, None)
    print(f"\nEnemy: {enemy1.getName()}")

    cc2 = CombatCard("Basic Attack", [], exeAct1, 15)
    enemy1.addCombatCard(cc2)
    cc1.addTarget(enemy1)
    cc1.queue()

    print(f"Health: {enemy1.getHealth()}/{enemy1.getMaxHealth()}")
    enemy1.executeEffects()
    print(f"Health: {enemy1.getHealth()}/{enemy1.getMaxHealth()}")
