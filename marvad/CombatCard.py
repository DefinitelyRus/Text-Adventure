class CombatCard:
    def __init__(self, name = "Unnamed Combat Card", action = None, value = None):
        self.cardName = name
        self.targetList = []
        self.cardAction = action
        self.cardAction.setValue(value)

    #STRING: Card Name
    def setName(self, name): self.cardName = name
    def getName(self): return self.cardName

    #Targetable LIST (i.e. Objects like Enemies or Players that can be targetted)
    def setTargets(self, targets): self.cardAction.targetList = targets
    def getTargets(self): return self.cardAction.targetList

    #Targetable OBJECT (i.e. Objects like Enemies or Players that can be targetted)
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
