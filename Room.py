from Item_and_Subclasses import Item
class Room:

    north: 'Room'
    south: 'Room'
    east: 'Room'
    west: 'Room'
    name: str
    lightLevel: str

    #// TODO entities: EntityList
    #ItemList: Item[]
    # roomDescriptions: a dictionary with descriptions for the 3 light levels


    def __init__(self, roomDescriptions, EntityList, name = None, north = None, south = None, east = None, west = None, lightLevel = None):
        self.roomDescriptions = roomDescriptions
        self.EntityList = EntityList
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.lightLevel = lightLevel

        # if direction is not entered, make that direction point to self
        # else make sure the rooms point at each other
        if north == None:
            self.north = self
        else:
            north.south = self

        if south == None:
            self.south = self
        else:
            south.north = self

        if east == None:
            self.east = self
        else:
            east.west = self

        if west == None:
            self.west = self
        else:
            west.east = self

    #Returns the room that is in the direction the player chose
    def go_direction(self, direction):
        direction = direction.lower()
        validDirections = ["north", "south", "east", "west"]
        if direction in validDirections:
            return getattr(self, direction)
        else:
            return None
    