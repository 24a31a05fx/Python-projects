# Build a Musical Instrument Inventory
#  Description :
''' 
This program demonstrates how to use classes and objects in Python to create a simple Musical Instrument Inventory. 

It defines a class called MusicalInstrument with attributes like name and instrument_type, and methods such as play() and get_fact().

Each object created from the class represents a different musical instrument, allowing us to store and display information about various instruments and perform actions like "playing" them or getting interesting facts about their type.

'''




# source code:
class MusicalInstrument:
    def __init__(self, name, instrument_type):
        self.name = name
        self.instrument_type = instrument_type

    def play(self):
        print(f'The {self.name} is fun to play!')

    def get_fact(self):
        return f'The {self.name} is part of the {self.instrument_type} family of instruments.'


instrument_1 = MusicalInstrument('Oboe', 'woodwind')
instrument_2 = MusicalInstrument('Trumpet', 'brass')

instrument_1.play()
instrument_2.play()
print(instrument_1.get_fact())
print(instrument_2.get_fact())