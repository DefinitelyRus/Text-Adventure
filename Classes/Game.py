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

    In a standard game of Marvelous Adventures, there are 5 scenes (known externally as "stages").
    In each stage, there are 20 levels held in a specified Location.

    In each level, there are a list of enemies and a specified number of turns.
    Once the players run out of turns, the enemies will run away with limited or no
    rewards to the players.
    All 1st levels of each stage are scripted. All events in this level are premade.
    Every 6th and 19th level of a stage, there won't be any required combat events.
    Instead, the players will enter a shop where they can buy and/or sell items.
    Every 7th and 14th level of a stage, the enemy encounter will be a guaranteed mini-boss.
    Levels 2, 5, 9, 12, 16, and 18 are all guaranteed regular combat events.
    The rest of the levels are random. Could be a combat event, shop, etc.
    
    In each turn, each player can perform an ExecutableAction by using a CombatCard.
    Essentially, a CombatCard is a preset ExecutableAction that can be used in combat.

    Locations can provide special effects during gameplay. For example,
    an Arctic Tundra location will apply a freezing effect on all entities, including enemies.
    Certain entities are immune to its effects, some aren't. Those who are affected
    will need to prevent it by using certain CombatCards or items.
    """

    id = None
    length = None
    levelList = []

    def __init__(self, gameLength):
        from Player import Player, PlayerClass
        from CombatCard import CombatCard
        from Scene import Scene
        from Location import Location

        self.id = None
        self.length = gameLength
        self.locationList = []
        self.playerList = [Player("Rus", PlayerClass("custom"), None)]
        self.sceneList = []
        self.currentSceneIndex = 0

        for i in range(self.length):
            self.locationList.append(Scene(2, 2, Location(randomName("location")), self.playerList, "Battle"))

    #Player OBJECT LIST: This contains all the player objects in the game.
    def setPlayerList(self, playerList): self.playerList = playerList
    def getPlayerList(self): return self.playerList
    def addPlayer(self, player): self.playerList.append(player)
    def getPlayerByIndex(self, playerIndex): return self.playerList[playerIndex]
    def removePlayerByIndex(self, playerIndex): self.playerList.pop(playerIndex)

    def getPlayerByName(self, playerName):
        for player in self.playerList:
            if player.getName() == playerName: return player

    def removePlayerByName(self, playerName):
        for player in self.playerList:
            if player.getName() == playerName: self.playerList.remove(player)


    #Scene OBJECT LIST: This contains all the scene objects in the game.
    def setSceneList(self, sceneList): self.sceneList = sceneList
    def getSceneList(self): return self.sceneList
    def addScene(self, scene): self.sceneList.append(scene)
    def getSceneByIndex(self, sceneIndex): return self.sceneList[sceneIndex]
    def removeSceneByIndex(self, sceneIndex): self.sceneList.pop(sceneIndex)
    def getCurrentScene(self): return self.sceneList[self.currentSceneIndex]


def randomName(nameForWhat):
    import random

    locationNames = ["Test1", "Test2", "Test3"]

    if nameForWhat == "location": return random.choice(locationNames)

if __name__ == "__main__":
    game = Game(2)
