'''
Created on 19 Oct 2021

@author: Rus1
'''

class Location:
    """
    A location is an object that holds a set of entities that a player can find only in a specific location.
    * This can have an expanded purpose later on.
    """
    def __init__(self, name = "Unnamed Location", targetables = []):
        self.locationName = name
        self.locationTargetables = targetables
        self.locationRelations = relations

    #Location Name STRING: Just a simple label to name the location.
    def setName(self, name): self.name = name
    def getName(self): return self.name

    #Targetable OBJECT LIST: A list of Targetables that may appear in this location.
    def setTargetableList(self, targetables): self.targetables = targetables
    def getTargetableList(self): return self.targetables
    def addTargetable(self, targetable): self.targetables.append(targetable)
    def getTargetable(self, name = None):
        from Targetable import Targetable
        if (self.locationTargetables.size() == 1):
            #Automatically returns the only object in the list if the list is only of size one.
            #COMBAK: Implement this in other lists for other objects.
            return self.locationTargetables[0]
        else:
            for targetable in self.locationTargetables:
                if targetable.getName() == name: return targetable
            else:
                print(f"[Location.py] No Targetable named \"{name}\" found in this Location.")
    def removeTargetable(self, name):
        for targetable in self.locationTargetables:
            if targetable.getName() == name: return targetable
        else:
            print(f"[Location.py] No Targetable named \"{name}\" found in this Location.")

    #Relations DICTIONARY (String, String): A dictionary that contains the relationships between this location and the listed locations. (e.g. "AtWar", "Helping", "Tension") If the location isn't listed, it'll be set as neutral by default.
    def setRelationList(self, relations): self.locationRelations = relations
    def getRelationList(self): return self.locationRelations
    def addRelation(self, location, relation):
        self.locationRelations[location.getName()] = relation
    def setRelation(self, location, relation):
        #Identical to addRelation(), but added anyway for consistency.
        self.locationRelations[location.getName()] = relation
    def getRelation(self, location): return self.locationRelations[location.getName()]
    def addRelationByName(self, locationName, relation):
        self.locationRelations[locationName] = relation
    def setRelationByName(self, locationName, relation):
        #Identical to addRelation(), but added anyway for consistency.
        self.locationRelations[locationName] = relation
    def getRelationByName(self, locationName): return self.locationRelations[locationName]
    def autoSetRelations(self, game):
        """
        This method requires the host game object to operate. This way, the method can retrieve all locations automatically by itself.
        """
        from Game import Game
        from Utils import SmartRandomChoice

        chooser = SmartRandomChoice()
        chooser.setChoiceList(game.getLocationList())

        for location in chooser.getList():
            addRelation(location, chooser.choice())
        pass


#Test code
if __name__ == "__main__":
    from main.PremadeObjects import randomName
    venue = Location()
    venue.setName(randomName("location"))
    venue.setEntities([randomName("character"), randomName("character"), randomName("character")])
    print(venue.getName())
    print(venue.getEntityList())
