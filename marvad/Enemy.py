from marvad.Targetable import Targetable
from marvad.EntityClass import EntityClass

class Enemy(Targetable):
    """
    An enemy object - this is a targetable object.
    Players can choose to use CombatCard objects against these entities.
    Other Enemy objects can interact with this to use their own CombatCard objects. (For game design; not included here.)
    """
    def __init__(self, turnLimit = 10, name = "Unnamed Enemy", enemyClass = EntityClass(), lootTable = None):
        self.enemyTurnLimit = turnLimit
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

    #Turn Limit INT: Number of turns enemies will take before escaping.
    def setTurnLimit(self, turnLimit): self.turnLimit = turnLimit
    def getTurnLimit(self): return self.turnLimit

    #Loot Table DICTIONARY (i.e. Likelihood of dropping certain items)
    #COMBAK: Decide whether this is better left as a ITEM:CHANCE% dictionary or a hashtable.
    #def setLootTable(self, lootTable): self.enemyLootTable = lootTable
    #def getLootTable(self): return self.enemyLootTable
