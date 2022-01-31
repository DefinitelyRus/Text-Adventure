class EntityClass:
    """
    This object is used to store what cards and attributes an entity can have.
    All combat entities are required to have a class.

    Note: The word "class" refers to a type of entity object, not a Python class.
    """
    def __init__(self, className = "empty", maxHealth = 5, combatCards = []):
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

        self.className = className
        self.classMaxHealth = maxHealth
        self.classCombatCards = combatCards

    #Class Name STRING: The class name. Doubles as a preset name.
    def setName(self, name): self.className = className
    def getName(self): return self.className

    #Max Health INT: Maximum health an entity can have.
    def setMaxHealth(self, maxHealth): self.classMaxHealth = maxHealth
    def getMaxHealth(self): return self.classMaxHealth

    #Combat Card OBJECT LIST: A list of combat cards.
    def setCombatCards(self, combatCards): self.classCombatCards = combatCards
    def getCombatCards(self): return self.classCombatCards
    def addCombatCard(self, combatCard): self.classCombatCards.append(combatCard)
    def getCombatCard(self, combatCardName):
        for card in self.classCombatCards:
            if card.getName() == combatCardName: return card

    def getCardsPreset(self, presetName):
        cardList = []
        match presetName:
            #TODO: Add cards. (Needs further game design before this can be implemented.)
            case "empty":
                return cardList

            case "test":
                return cardList

            case "tutorial":
                return cardList

            case "damage":
                return cardList

            case "tank":
                return cardList

            case "support":
                return cardList
