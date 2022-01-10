from Targetable import Targetable
from EntityClass import EntityClass

class Enemy(Targetable):
    def __init__(self, name = "Unnamed Enemy", enemyClass = None, lootTable = None):
        self.enemyClass = enemyClass
        self.enemyCombatCards = self.enemyClass.getCombatCards()
        self.enemyLootTable = lootTable
        super().__init__(name, self.enemyClass.getMaxHealth())

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
