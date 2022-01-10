'''
Created on 19 Oct 2021

@author: Rus1
'''

class Location:
    """
    A location is an object that holds a set of entities that a player can find only in a specific location.
    * This can have an expanded purpose later on.
    """
    def __init__(self, name = "Unnamed Location", entities = []):
        self.__name = name
        self.__entityList = entities

    def setName(self, name): self.__name = name
    def getName(self): return self.__name

    def setEntities(self, entities): self.__entityList = entities
    def addEntity(self, entity): self.__entityList.append(entity)
    def getEntity(self):
        if (entityList.size() == 1): return self.__entityList[0]
    def getEntityList(self): return self.__entityList

#Test code
if __name__ == "__main__":
    from main.PremadeObjects import randomName
    venue = Location()
    venue.setName(randomName("location"))
    venue.setEntities([randomName("character"), randomName("character"), randomName("character")])
    print(venue.getName())
    print(venue.getEntityList())
