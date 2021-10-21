from abc import ABC, abstractmethod
class ExecutableAction:
    """
    A parent class for ExecutableAction Objects. (e.g. AttackAction, )
    """
    @abstractmethod
    def execute(targets):
        pass

class AttackAction(ExecutableAction):
    def execute(self, targetList, damage = 1):
        for target in targetList:
            target.setHealth(target.getHealth() - damage)
