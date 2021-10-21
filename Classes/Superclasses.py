class Targettable:
    def __init__(self, name, maxHealth):
        self.entityName = name
        self.entityMaxHealth = maxHealth
        self.entityHealth = self.entityMaxHealth

    #STRING: Entity Name
    def setName(self, name): self.entityName = name
    def getName(self): return self.entityName

    #INT: Maximum Entity Health
    def setMaxHealth(self, maxHealth): self.entityMaxHealth = maxHealth
    def getMaxHealth(self): return self.entityMaxHealth

    #INT: Current Entity Health
    def setHealth(self, health): self.entityHealth = health
    def getHealth(self): return self.entityHealth
