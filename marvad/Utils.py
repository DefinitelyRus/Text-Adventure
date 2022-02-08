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

#TODO: Add "return self" to all no-return methods.
class SmartRandomChoice: #------------------------------------------------------
    """
    An object that handles stratified selection from lists.
    It takes into consideration one-time selection, any mutually inclusive and/or mutually exclusive options, probability weighing, among others.
    """
    def __init__(self, choiceList = [], algorithm = "simple_random", autoRemove = False, inclusive = False, exclusive = False, enableWeighing = False):
        self.choiceList = choiceList #Contains dictionaries.
        self.choiceCount = 0
        self.choiceAlgorithm = algorithm
        self.isOneTimeSelection = autoRemove
        self.isMutuallyInclusive = inclusive
        self.isMutuallyExclusive = exclusive
        self.isWeighingEnabled = enableWeighing
        self.finalChoiceList = []
        self.isFinal = False

    #Choice OBJECT DICTIONARY LIST: Contains all the objects to choose from.
    def setChoiceList(self, choices):
        self.choiceList = choices
        self.isFinal = False
        return self
    def getChoiceList(self): return self.choiceList
    def addChoice(self, object, autoRemove = False, inclusiveWith = [], exclusiveWith = [], weight = 1):
        self.choiceList.append(
            {
                "object" : object,
                "auto_remove" : autoRemove,
                "inclusive_with" : inclusiveWith,
                "exclusive_with" : exclusiveWith,
                "weight" : weight
            }
        )
        self.isFinal = False
        return self

    #Choice Count INT: This determines the length of the finalChoiceList.
    def setChoiceCount(self, count): self.choiceCount = count
    def getName(self): return self.choiceCount

    #Choice Algorithm STRING: This determines how the choices are sorted, which are then chosen from linearly.
    """
    Usable randomizer algorithms:
    simple_random   - Uses Fisher-Yates randomizer algorithm.

    Usable sorter algorithms:
    ascending       - Uses Timsort algorithm.
    descending      - Uses reversed Timsort algorithm.

    IMPORTANT: Using sorter algorithms will cause item weights to be ignored.
    """
    def setAlgorithm(self, algorithm):
        self.algorithm = algorithm
        self.isFinal = False
        return self
    def getAlgorithm(self): return self.algorithm
    def sortChoiceList(self):
        import random
        list = self.choiceList

        #Sorting the choice list.
        match self.choiceAlgorithm:
        case "simple_random":
            #COMBAK: Does this actually not need assigning?
            random.shuffle(list)
        case "ascending":
            #Uses built-in Timsort algorithm.
            list.sort(reverse=False)
        case "descending":
            #Uses built-in Timsort algorithm.
            list.sort(reverse=True)

        self.choiceList = list
        self.isFinal = False
        return self

    #Auto-remove BOOLEAN Override ----------------------------------------------
    def isAutoRemoveOverride(self, autoRemove = None):
        """
        Decides whether the chooser should remove already-selected objects.

        Changing this from the default value (False) will cause the chooser to override the values specified in the choiceList. Leaving the value at default (False) will let the chooser use the specified autoRemove values.
        """
        if (isinstance(autoRemove, None)): return self.isOneTimeSelection
        else:
            self.isOneTimeSelection = autoRemove
            return self

    #Auto-remove BOOLEAN
    #TODO: Add setters and getters by index.
    def setAutoRemoveByObjectName(self, objectName, autoRemove):
        """
        Changes an individual choice's autoRemove value based on the choice's object name. This decides whether the chooser should remove the selected choice after selection.

        This method can also be used to set autoRemove by value if it's a primitive data type (e.g. integers, floats, booleans, strings).
        """
        for dict in self.choiceList:
            object = dict["object"]

            if isinstance(object, str):
                if object == objectName: dict["autoRemove"] = autoRemove
            else:
                if object.getName() == objectName: dict["autoRemove"] = autoRemove
            self.isFinal = False
            return self
        else:
            print(f"[Utils.SmartRandomChoice] No object with name \"{objectName}\" was found in the choiceList.")

    def getAutoRemoveByObjectName(self, objectName):
        """
        Retrieves an individual choice's autoRemove value based on the choice's object name. This decides whether the chooser should remove the selected choice after selection.

        This method can also be used to set autoRemove by value if it's a primitive data type (e.g. integers, floats, booleans, strings).
        """
        for dict in self.choiceList:
            object = dict["object"]

            if isinstance(object, (str, int, float, boolean)):
                if object == objectName: return dict["autoRemove"]
            else:
                if object.getName() == objectName: return dict["autoRemove"]
        else:
            print(f"[Utils.SmartRandomChoice] No object with name \"{objectName}\" was found in the choiceList.")

    #Mutually Inclusive BOOLEAN Override ---------------------------------------
    #TODO: Add setters and getters by index.
    def isMutuallyInclusiveOverride(self, inclusive = None):
        """
        Considers mutually inclusive objects. This means that any chosen object will have their mutually included object be guaranteed to be chosen.

        isMutuallyInclusive is required to be set to TRUE for the specified inclusiveWith values from the choiceList to be applied.
        Leaving this value at default (False) will let the chooser ignore the specified inclusiveWith values.
        Inputting no arguments will simply return the current isMutuallyInclusive value.
        """
        if (isinstance(inclusive, None)): return self.isMutuallyInclusive
        else:
            self.isMutuallyInclusive = inclusive
            self.isFinal = False
            return self

    #Mutually Exclusive BOOLEAN Override ---------------------------------------
    #TODO: Add setters and getters by index.
    def isMutuallyExclusiveOverride(self, exclusive = None):
        """
        Considers mutually exclusive objects. This prevents certain choices from being chosen when the other is already present.

        isMutuallyExclusive is required to be set to TRUE for the specified exclusiveWith values from the choiceList to be applied.
        Leaving this value at default (False) will let the chooser ignore the specified exclusiveWith values.
        Inputting no arguments will simply return the current isMutuallyExclusive value.
        """
        if (isinstance(exclusive, None)): return self.isMutuallyExclusive
        else:
            self.isMutuallyExclusive = exclusive
            self.isFinal = False
            return self

    #Enable Weights BOOLEAN Override -------------------------------------------
    def isWeighingEnabled(self, enableWeighing = None):
        """
        Considers mutually exclusive objects. This prevents certain choices from being chosen when the other is already present.

        isMutuallyExclusive is required to be set to TRUE for the specified exclusiveWith values from the choiceList to be applied.
        Leaving this value at default (False) will let the chooser ignore the specified exclusiveWith values.
        Inputting no arguments will simply return the current isMutuallyExclusive value.
        """
        if (isinstance(exclusive, None)): print(f"[Utils.SmartRandomChoice] isMutuallyExclusive is {self.isMutuallyExclusive}.")
        else:
            self.isMutuallyExclusive = exclusive
            self.isFinal = False
            return self

    #Weights INTEGER LIST: This determines the likelihood that a choice will be chosen. Higher number = more likely.
    def setWeightByIndex(self, index, weight):
        dict = self.choiceList[index]
        dict["weight"] = weight
        self.isFinal = False
        return self

    def getWeightByIndex(self, index):
        dict = self.choiceList[index]
        return dict["weight"]

    def setWeightByObjectName(self, objectName, weight):
        """
        Modifies the weight (int) of the given object from the choice list. This determines the likelihood that a choice will be chosen. Higher number = more likely.

        This method can also be used to set the weight by value if it's a primitive data type (e.g. integers, floats, booleans, strings).
        """
        for dict in self.choiceList:
            object = dict["object"]

            if isinstance(object, str):
                if object == objectName: dict["weight"] = weight
            else:
                if object.getName() == objectName: dict["weight"] = weight
            self.isFinal = False
            return self
        else:
            print(f"[Utils.SmartRandomChoice] No object with name \"{objectName}\" was found in the choiceList.")

    def getWeightByObjectName(self, objectName):
        """
        Returns the weight (int) of the given object from the choice list. This determines the likelihood that a choice will be chosen. Higher number = more likely.

        This method can also be used to get the weight by value if it's a primitive data type (e.g. integers, floats, booleans, strings).
        """
        for dict in self.choiceList:
            object = dict["object"]

            if isinstance(object, str):
                if object == objectName: dict["weight"]
            else:
                if object.getName() == objectName: dict["weight"]
            return
        else:
            print(f"[Utils.SmartRandomChoice] No object with name \"{objectName}\" was found in the choiceList.")

    #Choice METHOD -------------------------------------------------------------
    def choose(self):
        """
        Returns the first item in the choice list, then modifies the list based on the attributes set on the chooser class.

        This is method is called when the choice list has already been modified to fit the user's needs.
        """
        choiceList = self.finalChoiceList
        weightedList = []
        totalWeight = 0
        choice = choiceList[0]

        #TODO: Make finalChoiceList generator
        if not self.isFinal:
            choiceList.clear()
            for item in self.choiceList:
                itemWeight = item["weight"]
                weightedList.append(
                    {
                        "object" : item,
                        "weight_floor" : totalWeight + 1,
                        "weight_ceil" : totalWeight + item["weight"]
                    }
                )

            #Trims to fit the choiceCount.
            for item in weightedList:
                itemWeightFloor = item["weight_floor"]
                itemWeightCeil = item["weight_ceil"]
                itemDict = item["object"]

                for exclusion in itemDict["exclusive_with"]:
                    if exclusion in choiceList:
                        pass
                        #TODO: "If an exlusion is already in the choiceList, skip to the next item in the weightedList."

            self.finalChoiceList = choiceList



        #Auto Remove: Removes all copies from the list.
        if self.isOneTimeSelection:
            for obj in choiceList:
                if obj == choice:
                    choiceList.remove(obj)

        #Mutual Inclusivity
        if self.isMutuallyInclusive:
            #TODO: Create attributes "isFinal" & "finalChoiceList".
            #This way, upon calling choose(), the finalChoiceList will only be generated if isFinal is True. However, making any changes to the chooser's attributes (e.g. isMutuallyInclusiveOverride, adding new items, etc.) will set isFinal to False, forcing the finalChoiceList to be generated again upon using choose().
            pass

        #Mutual Exclusivity: Removes all mutually exclusive items from the list.
        if self.isMutuallyExclusive:
            excludedChoices = choice["exclusive_with"]

            for item in choiceList:
                if item["object"] in excludedChoices:
                    choiceList.remove(item)

        self.finalChoiceList = choiceList
        return choice





if __name__ == "__main__":
    addJsonEntry()
    #COMBAK: Delete later.
    # import os
    # print(os.getcwd())
    # filePath = r"..\Text Adventure\marvad\presets\CharacterNames.json"
    # setJson(filePath, characterNames)
    # print(getJson(filePath))
