standardStat = {
"Composure" : 1,
"Charisma" : 1
}

standardActions = {
"Use Item" : "useItemAction"
"Skip Turn" : "skipTurnAction"
}

class Player:
    from presets.PremadeObjects import randomName
    def __init__(self, name = randomName("character"), class = None, inventory = None):
        self.playerName = name #String
        self.playerClass = class #PlayerClass object
        self.playerCombat = self.playerClass.getCombatCards() #List of CombatCard objects
        self.playerInventory = inventory #Create object
        self.playerMaxHealth = self.playerClass.getMaxHealth()
        self.playerHealth = self.playerClass.getMaxHealth()
        self.playerStat = standardStat #A dictionary of preset stats

    #STRING: Player Name
    def setName(self, name): self.playerName = name
    def getName(self): return self.playerName

    #PlayerClass OBJECT: Player Class
    def setClass(self, class): self.playerClass = class
    def getClass(self): return self.playerClass

    #CombatCard LIST (e.g. Attacks, Defends, Heals)
    def setCombatCards(self, cardsList): self.playerCombat = cardsList
    def getCombatCards(self): return self.playerCombat
    def addCombatOption(self, combatOption): self.playerCombat.append(combatOption)

    #PlayerInventory OBJECT (i.e. A container for items)
    def setInventory(self, inventory): self.playerInventory = inventory
    def getInventory(self): return self.playerInventory

    #Item OBJECT from PlayerInventory
    def addInventoryItem(self, item): self.playerInventory.addItem(item) #Todo: Create PlayerInventory object & create addItem() method
    def getInventoryItem(self, name): self.playerInventory.getItemByName(name) #create getItemByName() method

    #INT: Maximum Play Health
    def setMaxHealth(self, maxHealth): self.playerMaxHealth = maxHealth
    def getMaxHealth(self): return self.playerMaxHealth

    #INT: Current Player Health
    def setHealth(self, health): self.playerHealth = health
    def getHealth(self): return self.playerHealth

    #Player Stat DICTIONARY (e.g. Charisma, Composure, Empathy)
    def setStats(self, stats): self.playerStat = stats
    def getStats(self): return self.playerStat
    def setStat(self, name, value): self.playerStat[name] = value
    def getStat(self, name): return self.playerStat[name]

class PlayerClass:
    def __init__(self, className = "custom", maxHealth = 5, combatCards = None):
        match className:
            case "custom":
                self.classMaxHealth = maxHealth
                self.classCombatCards = combatCards #A list of actionable combat cards
            case "damage":
                self.classMaxHealth = 25
                self.classCombatCards = __getOptionsPreset(className)
            case "tank":
                self.classMaxHealth = 40
                self.classCombatCards = __getOptionsPreset(className)
            case "support":
                self.classMaxHealth = 15
                self.classCombatCards = __getOptionsPreset(className)

    def setMaxHealth(self, maxHealth): self.classMaxHealth = maxHealth
    def getMaxHealth(self): return self.classMaxHealth

    def setCombatCards(self, combatCards): self.classCombatCards = combatCards
    def getCombatCards(self): return self.classCombatCards
    def addCombatOption(self, combatOption): self.classCombatCards.append(combatOption)
    def getCombatOption(self, combatOptionName):
        for option in self.classCombatCards:
            if option.getName() == combatOptionName: return option

    def getOptionsPreset(presetName):
        optionList = []

        match presetName:
            case "default":
                return optionList

            case "tutorial":
                #Todo: add cards
                return optionList

            case "damage":
                #Todo: add cards
                return optionList

            case "tank":
                #Todo: add cards
                return optionList

            case "support":
                #Todo: add cards
                return optionList

class CombatCard:
    def __init__(self):
