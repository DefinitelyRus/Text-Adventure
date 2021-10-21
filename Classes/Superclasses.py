class Targettable:
    def __init__(self, name, maxHealth):
        self.entityName = name
        self.entityMaxHealth = maxHealth
        self.entityHealth = self.entityMaxHealth
        self.effectsQueue = []

    #STRING: Entity Name
    def setName(self, name): self.entityName = name
    def getName(self): return self.entityName

    #INT: Maximum Entity Health
    def setMaxHealth(self, maxHealth): self.entityMaxHealth = maxHealth
    def getMaxHealth(self): return self.entityMaxHealth

    #INT: Current Entity Health
    def setHealth(self, health): self.entityHealth = health
    def getHealth(self): return self.entityHealth

    def receiveAction(self, effect): self.effectsQueue.append(effect)
    def removeActionFromQueue(self, effect): self.effectsQueue.remove(effect)
    def getReceivedActions(self): return self.effectsQueue
    def executeEffects(self):
        from PlayerActions import ExecutableAction
        from PlayerActions import DamageAction
        queue = self.effectsQueue
        totalDamage = 0
        accumulatedDamage = 0
        defense = 0
        damageMultiplier = 1

        #Accumulation of effects
        for effect in queue:
            if not isInstance(effect, ExecutableAction): pass
            actionType = effect.getActionType()

            #Health-based effects
            if actionType == "Attack": accumulatedDamage += effect.getValue() #Usually from opponent
            elif actionType == "Defend": defense += effect.getValue() #Usually from teammate
            elif actionType == "Enrage": damageMultiplier += effect.getValue() #Usually from opponent
            elif actionType == "Absorb": damageMultiplier -= effects.getValue() #Usually from teammate

        #Execution of effects
        totalDamage = (totalDamage - defense) * damageMultiplier
        self.setHealth(self.getHealth() - totalDamage)
