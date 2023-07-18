import note

class Notebook():
    def __init__(self):
        self._list = []


    def addNote(self, newNote):
        self._list.append(newNote)

    @property
    def printNotebook(self):
        returnString = ""
        for i in range(len(self._list)):
            returnString += self._list[i].printNote + "------------------------------------------\n"
        return returnString