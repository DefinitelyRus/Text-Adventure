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
    """
    This function requires importing the "json" library.

    Retrieves the contents of the specified JSON files and
    returns a parsed object.
    """
    import json
    file = open(filePath, 'r')
    jsonAsString = json.loads(file.read())
    file.close()
    return jsonAsString

def setJson(filePath, content):
    """
    This function requires importing the "json" library.

    Overwrites the contents of the specified JSON file with the given content.
    """
    import json
    with open(filePath, "w") as file:
        file.write(json.dumps(content, indent=4))
        file.close()

def addToJson(filePath, object, toAppend = True, toSort = False):
    """
    This function requires importing the "json" library.

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

def addJsonEntry():
    """
    This is an easy way to add entries to a JSON file without having to
    edit the file directly using a text editor.
    """
    filePath = ""
    stringList = []
    while True:
        try:
            filePath = input("File directory: ")
            open(filePath, "r").close()
        except:
            print("That's not a valid file directory.\n")
            continue
        print("")
        break

    count = 0

    while True:
        try:
            userInput = input(f"Item({count}): ")

            if userInput == "stop":
                break

            stringList.append(userInput)
            count += 1
        except:
            import traceback
            traceback.print_exc(limit=None, file=None, chain=True)
            while True: pass

    addToList(filePath, stringList, True, True)

if __name__ == "__main__":
    addJsonEntry()
    #COMBAK: Delete later.
    # import os
    # print(os.getcwd())
    # filePath = r"..\Text Adventure\marvad\presets\CharacterNames.json"
    # setJson(filePath, characterNames)
    # print(getJson(filePath))
