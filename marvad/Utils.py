#A list of premade locations.
presetLocations = []

#A list of names of places.
locationNames = ["Zuma", "Delphi", "Neustra", "Colton", "Varona", "Caledonia", "Konoi", "Shenandoah",
                "Nachdicht", "Earsia", "Kamachya", "Zariya", "Cazelle", "Yooto"]

#A list of names of characters.
characterNames = ["Harold", "Gordon", "Kris", "Tin", "Cetteel", "Oxy"]

#Randomly chooses a name from a given list.
def randomName(nameFor):
    import random
    match nameFor:
        case "location":
            return random.choice(locationNames)
        case "character":
            return random.choice(characterNames)
