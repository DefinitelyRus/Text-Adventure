from Targetable import Targetable

class Enemy(Targetable):
    def __init__(self, name = "Unnamed Enemy", enemyClass = None, lootTable = None):
        self.entityName = name
        self.enemyClass = enemyClass
        self.enemyCombatCards = self.enemyClass.getCombatCards()
        self.entityMaxHealth = self.enemyClass.getMaxHealth()
        self.entityHealth = self.enemyClass.getMaxHealth()
        self.enemyLootTable = lootTable

    #STRING: Enemy Name
    def setName(self, name): self.entityName = name
    def getName(self): return self.entityName

    #EnemyClass OBJECT: Enemy Class
    def setClass(self, enemyClass): self.enemyClass = enemyClass
    def getClass(self): return self.enemyClass

    #CombatCard LIST (e.g. Attacks, Defends, Heals)
    def setCombatCards(self, cardsList): self.enemyCombatCards = cardsList
    def getCombatCards(self): return self.enemyCombatCards
    def addCombatCard(self, combatCard): self.enemyCombatCards.append(combatCard)
    def removeCombatCard(self, combatCard): self.enemyCombatCards.remove(combatCard)
    def getCombatCardByName(self, name):
        for card in self.enemyCombatCards:
            if card.getName() == name: return card

    #INT: Maximum Enemy Health
    def setMaxHealth(self, maxHealth): self.entityMaxHealth = maxHealth
    def getMaxHealth(self): return self.entityMaxHealth

    #INT: Current Enemy Health
    def setHealth(self, health): self.entityHealth = health
    def getHealth(self): return self.entityHealth

    #Loot Table DICTIONARY (i.e. Likelihood of dropping certain items)
    #COMBAK: Decide whether this is better left as a ITEM:CHANCE% dictionary or a hashtable.
    #def setLootTable(self, lootTable): self.enemyLootTable = lootTable
    #def getLootTable(self): return self.enemyLootTable

class EnemyClass:
    #COMBAK: Merge with PlayerClass?
    def __init__(self, className = "Unnamed Enemy Class", maxHealth = 5, combatCards = []):
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
                #TODO: add cards
                return cardList

            case "damage":
                #TODO: add cards
                return cardList

            case "tank":
                #TODO: add cards
                return cardList

            case "support":
                #TODO: add cards
                return cardList
