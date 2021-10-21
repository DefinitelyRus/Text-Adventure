from abc import abstractmethod
class Targettable:
    @abstractmethod
    def __init__(self, name, maxHealth):
        self.entityName = name
        self.entityMaxHealth = maxHealth
        self.entityHealth = self.entityMaxHealth
        self.actionsQueue = []

    #STRING: Entity Name
    def setName(self, name): self.entityName = name
    def getName(self): return self.entityName

    #INT: Maximum Entity Health
    def setMaxHealth(self, maxHealth): self.entityMaxHealth = maxHealth
    def getMaxHealth(self): return self.entityMaxHealth

    #INT: Current Entity Health
    def setHealth(self, health): self.entityHealth = health
    def getHealth(self): return self.entityHealth

    #ExecutableAction LIST: A list of
    def receiveAction(self, action): self.actionsQueue.append(action)
    def removeActionFromQueue(self, action): self.actionsQueue.remove(action)
    def getReceivedActions(self): return self.actionsQueue

    @abstractmethod
    def executeEffects(self):
        from PlayerActions import ExecutableAction
        queue = self.actionsQueue
        totalDamage = 0
        accumulatedDamage = 0
        defense = 0
        damageMultiplier = 1

        #Accumulation of actions
        for action in queue:
            if not isinstance(action, ExecutableAction): pass
            actionType = action.getType()

            #Health-based actions
            if actionType == "Attack":
                accumulatedDamage += action.getValue() #Usually from opponent
            elif actionType == "Defend": defense += action.getValue() #Usually from teammate
            elif actionType == "Enrage": damageMultiplier += action.getValue() #Usually from opponent
            elif actionType == "Absorb": damageMultiplier -= actions.getValue() #Usually from teammate
            else: print("Fail")

        #Execution of actions
        totalDamage = (accumulatedDamage - defense) * damageMultiplier
        self.setHealth(self.getHealth() - totalDamage)
