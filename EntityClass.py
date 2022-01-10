class EntityClass:
    """
    This object is used to store what cards and attributes an entity can have.
    All combat entities are required to have a class.
    """
    def __init__(self, className = "Unnamed Class", maxHealth = 5, combatCards = []):
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
