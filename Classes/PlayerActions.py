from abc import abstractmethod

class ExecutableAction:
    """
    A parent class for ExecutableAction Objects. (e.g. AttackAction, EnrageAction)
    """
    @abstractmethod
    def __init__(self, type, value = None, targets = []):
        self.actionType = type
        self.value = value
        self.targetList = targets

    @abstractmethod
    def execute(self):
        for target in self.targetList:
            target.receiveAction(self)

    #STRING: Action Type. (e.g. Attack, Enrage, Defend)
    @abstractmethod
    def setType(self, type): self.actionType = type
    def getType(self): return self.actionType

    @abstractmethod
    def setValue(self, value): self.value = value
    def getValue(self): return self.value

    @abstractmethod
    def setTargets(self, targets): self.targetList = targets
    def getTargets(self): return self.targetList
