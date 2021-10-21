'''
Created on 11 Mar 2021

@author: Rus

This python module serves as a separated list organizer for all the Names and Events (hence NAE-list) that will be used in adventureGame.py.
I made this separate so we can add more names and events much more easily and also to avoid cluttering the code with loooong lists.
'''

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
