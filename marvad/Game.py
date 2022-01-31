from marvad.Player import Player
from marvad.EntityClass import EntityClass
from marvad.Scene import Scene
from marvad.Location import Location
from marvad.Utils import randomName

class Game:
    """
    This contains all the data about any ongoing game of Marvelous Adventures.
    To start a game, a Game object has to be created.
    This will serve as the top-level manager of all major attributes.

    Created on 19 Oct 2021
    @author: DefinitelyRus
    """

    #id = None
    #length = None
    #levelList = []
    #TODO: Remove...?

    def __init__(self):
        self.playerList = []
        self.sceneList = []
        self.id = None
        self.locationList = []
        self.currentSceneIndex = 0

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
    def getSceneById(self, sceneId):
        for scene in self.sceneList:
            if scene.getSceneLevel() == sceneId: return scene

    def endGame(self): print("Game Over") #TODO: Do something

def createGame(playerName = "Player"):
    """
    This creates a standard single-player game of Marvelous Adventures.
    Contains 100 levels divided into 5 locations.

    Created on 21 Jan 2022
    @author: DefinitelyRus
    """
    from marvad.CombatCard import CombatCard
    from marvad.PlayerActions import ExecutableAction
    from marvad import Utils
    import random
    from marvad.Enemy import Enemy
    LEVEL_COUNT = 100 #Effectively a constant
    game = Game()

    #TODO: combatCards List should be based on the player's chosen class.
    #NOTE: The player's class should be set by random only in this game autogenerator and nowhere else.
    combatCards = [CombatCard("Attack Card", ExecutableAction("Attack"), random.randint(10,25)), CombatCard("Defend Card", ExecutableAction("Defend"), random.randint(10,25)), CombatCard("Enrage Card", ExecutableAction("Enrage"), random.randint(5,15))]
    playerClass = EntityClass("custom", random.randint(30,100), combatCards)
    player = Player(playerName, playerClass, None)

    locationList = [Location(Utils.randomName("location")), Location(Utils.randomName("location")), Location(Utils.randomName("location")), Location(Utils.randomName("location")), Location(Utils.randomName("location"))]
    locationListIndex = 0

    for levelCount in range(LEVEL_COUNT):
        print(f"|Creating Scene #{levelCount}...\n")
        event = "Battle" #COMBAK: Change to "Random". Also create random event generator.
        innerLevelCount = (levelCount + 1) % 20

        match innerLevelCount:
            case 1: event = "Scripted"
            case 2: event = "Battle"
            case 5: event = "Battle"
            case 6: event = "Store"
            case 7: event = "Battle"
            case 9: event = "Battle"
            case 12: event = "Battle"
            case 16: event = "Battle"
            case 18: event = "Battle"
            case 19: event = "Store"
            case 20: event = "Battle"

        ENEMY_CLASS_LIST = ["damage", "tank", "support"]
        enemyList = []
        totalTurns = 0
        #Spawns a random number of enemies (between 1-3 enemies).
        for enemyCount in range(random.randint(1,3)):
            print(f"|Creating Enemy #{enemyCount}...")
            enemy = Enemy()
            enemyClass = EntityClass(random.choice(ENEMY_CLASS_LIST))
            #NOTE: Values are set random for now. Values should be scaled based on the number of enemies and the total no. of turns in this scene.

            enemy.setName(Utils.randomName("character"))
            enemy.setClass(enemyClass)
            enemy.setTurnLimit(random.randint(5,15))
            #enemy.setLootTable(lootTable) #TODO: Add loot tables.
            print(f"|Created Enemy with attributes...")
            print(f"    Name: {enemy.getName()}")
            print(f"    Class: {enemy.getClass().getName()}")
            print(f"    Turns: {enemy.getTurnLimit()}")
            print(f"|Adding Enemy to list...")
            enemyList.append(enemy)

            totalTurns += enemy.getTurnLimit()
            print("")

        scene = Scene(levelCount)
        scene.setMaxTurns(totalTurns)
        scene.setLocation(locationList[locationListIndex])
        scene.addPlayer(player)
        scene.setEvent(event)

        print(f"|Created Scene with attributes...")
        print(f"    Turns: {scene.getMaxTurns()}")
        print(f"    Location: {scene.getLocation().getName()} ({locationListIndex})")
        print(f"    Event: {scene.getEvent()}")
        print(f"|Adding Scene #{scene.getSceneLevel()}...")
        game.addScene(scene)

        if (levelCount + 1) % 20 == 0: locationListIndex += 1
        elif (levelCount >= 100): game.endGame()

        print("\n----------------------------------------\n")
    return game
