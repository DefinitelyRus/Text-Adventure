#A list of names of places.
#TODO: Move contents to LocationNames.json and create a JSON parser here.
locationNames = ["Zuma", "Delphi", "Neustra", "Colton", "Varona", "Caledonia", "Konoi", "Shenandoah", "Nachdicht", "Earsia", "Kamachya", "Zariya", "Cazelle", "Yooto"]

#A list of names of characters.
#TODO: Move contents to CharacterNames.json and create a JSON parser here.
characterNames = ["Harold", "Gordon", "Kris", "Tin", "Cetteel", "Oxy"]

#Randomly chooses a name from a given list.
def randomName(nameFor):
    """
    Random name generator. This will get premade names from various lists and returns a name based on what object needs naming.

    Creation date unknown.
    @author: DefinitelyRus
    """
    import random
    match nameFor:
        #TODO: Create a JSON parser here. Get the list of names then pick randomly from there.
        case "location":
            return random.choice(locationNames)
        case "character":
            return random.choice(characterNames)

def getJson(filePath):
    import json
    file = open(filePath, 'r')
    jsonAsString = json.loads(file.read())
    file.close()
    return jsonAsString

def setJson(filePath, content):
    import json
    with open(filePath, "w") as file:
        file.write(json.dumps(content, indent=4))
        file.close()

def addToJson(filePath, object, toAppend = True, toSort = False):
    """
    Automagically adds the specified object(s) to the JSON file.
    This function will check what kind of object is being appended,
    then either adds the object as an individual entry or
    combines the mutable object with the rest of the JSON contents.

    To add a mutable object as an individual entry, toAppend must be False.
    To combine it with the existing contents, toAppend must be True.
    Additionally, sorting will be disabled by default and all new additions
    will be appended to the end of the list.
    Note that setting toSort to True while the list contains non-sortable
    objects will cause an exception to be raised.
    """
    import json
    with open(filePath, "w") as file:
        #FIXME: Python thinks "list" is a variable rather than a type.
        if isinstance(object, (list, tuple, dict)) and toAppend:
            list = json.loads(file.read()) + object

            #Optional sorting.
            if toSort:
                try: list.sort()
                except:
                    raise Exception("The given mutable object input or the JSON contents contain objects that cannot be sorted.")

            file.write(json.dumps(list, indent=4))
            file.close()
        else:
            list = json.loads(file.read())
            list.append(object)
            file.write(json.dumps(list, indent=4))
            file.close()
if __name__ == "__main__":
    #COMBAK: Delete later.
    import os
    print(os.getcwd())
    filePath = r"..\Text Adventure\marvad\presets\LocationNames.json"
    addToJson(filePath, "Bolognus")
    print(getJson(filePath))
