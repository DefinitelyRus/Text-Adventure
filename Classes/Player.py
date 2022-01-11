from classes.Targetable import Targetable
from classes.CombatCard import CombatCard
from classes.PlayerActions import ExecutableAction
from classes.EntityClass import EntityClass

#The default dicitonary of stats.
standardStat = {
    "Money" : 0,
    "Composure" : 1,
    "Charisma" : 1,
    "Empathy" : 3
}

#The default dictionary of action card objects.
standardActions = {
    "Use Item" : "useItemAction",
    "Skip Turn" : "skipTurnAction"
}

class Player(Targetable):
    from classes.presets.PremadeObjects import randomName
    def __init__(self, name = randomName("character"), playerClass = None, inventory = None):
        self.playerClass = playerClass
        self.playerCombatCards = self.playerClass.getCombatCards()
        self.playerInventory = inventory
        self.playerStat = standardStat
        super().__init__(name, self.playerClass.getMaxHealth())

    #STRING: Player Name
    def setName(self, name): self.entityName = name
    def getName(self): return self.entityName

    #PlayerClass OBJECT: Player Class
    def setClass(self, playerClass): self.playerClass = playerClass
    def getClass(self): return self.playerClass

    #CombatCard LIST (e.g. Attacks, Defends, Heals)
    def setCombatCards(self, cardsList): self.playerCombatCards = cardsList
    def getCombatCards(self): return self.playerCombatCards
    def addCombatCard(self, combatCard): self.playerCombatCards.append(combatCard)
    def removeCombatCard(self, combatCard): self.playerCombatCards.remove(combatCard)
    def getCombatCardByName(self, name):
        for card in self.playerCombatCards:
            if card.getName() == name: return card

    #PlayerInventory OBJECT (i.e. A container for items)
    def setInventory(self, inventory): self.playerInventory = inventory
    def getInventory(self): return self.playerInventory

    #Item OBJECT from PlayerInventory
    def addInventoryItem(self, item): self.playerInventory.addItem(item) #Todo: Create PlayerInventory object & create addItem() method
    def getInventoryItem(self, name): self.playerInventory.getItemByName(name) #create getItemByName() method

    #INT: Maximum Player Health
    def setMaxHealth(self, maxHealth): self.entityMaxHealth = maxHealth
    def getMaxHealth(self): return self.entityMaxHealth

    #INT: Current Player Health
    def setHealth(self, health): self.entityHealth = health
    def getHealth(self): return self.entityHealth

    #Player Stat DICTIONARY (e.g. Charisma, Composure, Empathy)
    def setStats(self, stats): self.playerStat = stats
    def getStats(self): return self.playerStat
    def setStat(self, name, value): self.playerStat[name] = value
    def getStat(self, name): return self.playerStat[name]
