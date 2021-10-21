from Superclasses import Targettable
from PlayerActions import *

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

dummy = Targettable("Dummy", 40)
class Player(Targettable):
    from presets.PremadeObjects import randomName
    def __init__(self, name = randomName("character"), playerClass = None, inventory = None):
        self.entityName = name
        self.playerClass = playerClass
        self.playerCombatCards = self.playerClass.getCombatCards()
        self.playerInventory = inventory
        self.entityMaxHealth = self.playerClass.getMaxHealth()
        self.entityHealth = self.playerClass.getMaxHealth()
        self.playerStat = standardStat

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


class PlayerClass:
    def __init__(self, className, maxHealth = 5, combatCards = []):
        match className:
            case "custom":
                self.classMaxHealth = maxHealth
                self.classCombatCards = combatCards #A list of actionable combat cards
            case "damage":
                self.classMaxHealth = 25
                self.classCombatCards = self.getCardsPreset(className)
            case "tank":
                self.classMaxHealth = 40
                self.classCombatCards = self.getCardsPreset(className)
            case "support":
                self.classMaxHealth = 15
                self.classCombatCards = self.getCardsPreset(className)

    def setMaxHealth(self, maxHealth): self.classMaxHealth = maxHealth
    def getMaxHealth(self): return self.classMaxHealth

    def setCombatCards(self, combatCards): self.classCombatCards = combatCards
    def getCombatCards(self): return self.classCombatCards
    def addCombatCard(self, combatCard): self.classCombatCards.append(combatCard)
    def getCombatCard(self, combatCardName):
        for card in self.classCombatCards:
            if card.getName() == combatCardName: return card

    def getCardsPreset(self, presetName):
        cardList = []
        match presetName:
            case "default":
                return cardList

            case "tutorial":
                #Todo: add cards
                return cardList

            case "damage":
                #Todo: add cards
                return cardList

            case "tank":
                #Todo: add cards
                return cardList

            case "support":
                #Todo: add cards
                cardList.append(CombatCard("Test Card", [dummy], ExecutableAction("Attack"))) #Temp
                return cardList


class CombatCard:
    def __init__(self, name = "Unnamed Combat Card", targets = [], action = None, value = None):
        self.cardName = name
        self.targetList = targets
        self.cardAction = action
        self.cardAction.setValue(value)

    #STRING: Card Name
    def setName(self, name): self.cardName = name
    def getName(self): return self.cardName

    #Targettable LIST (i.e. Objects like Enemies or Players that can be targetted)
    def setTargets(self, targets): self.cardAction.targetList = targets
    def getTargets(self): return self.cardAction.targetList

    #Targettable OBJECT (i.e. Objects like Enemies or Players that can be targetted)
    def addTarget(self, target): self.cardAction.targetList.append(target)
    def removeTarget(self, target):
        """Throws ValueError if target doesn't exist in list."""
        for t in self.targetList:
            if t == target:
                self.targetList.remove(target)
                break

    #ExecutableAction OBJECT (e.g. Attack, Defend, Heal)
    def setAction(self, action): self.cardAction = action
    def getAction(self): return self.cardAction
    def queue(self):
        self.cardAction.queue()

    def setValue(self, value): self.cardAction.setValue(value)
    def getValue(self): return self.cardAction.getValue()



#Creating a new player object
player = Player("Rus", PlayerClass("support"))
print(f"Player: {player.getName()}")
print(f"Target: {dummy.getName()}")

#Changes the health to be 5 less than before.
print(f"HP Before: {dummy.getHealth()}/{dummy.getMaxHealth()}")
card = player.getCombatCardByName('Test Card')
card.setValue(15)
card.addTarget(dummy)
card.queue()
dummy.executeEffects()
print(f"HP After: {dummy.getHealth()}/{dummy.getMaxHealth()}")
