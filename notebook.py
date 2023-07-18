import note
from datetime import datetime

class Notebook():
    def __init__(self):
        self._list = []


    def addNote(self, newNote):
        self._list.append(newNote)

    @property
    def buildNote(self):
        max_id = 0
        for i in range(len(self._list)):
            if max_id < int(self._list[i].id):
                max_id = int(self._list[i].id)
        next_id = max_id + 1

        inputHeader = input("Введите заголовок заметки: ")
        inputBody = input("Введите содержание заметки: ")
        currentDateTime = datetime.now()
        newNote = note.Note(next_id, inputHeader, inputBody, currentDateTime)

        return newNote
    

    def removeNote(self, idToDelete):
        #idToDelete = input("Введите id заметки для удаления: ")
        i = 0
        foundFlag = False
        while i < len(self._list) and foundFlag == False:
            if idToDelete == int(self._list[i].id):
                self._list.pop(i)
                foundFlag = True
            i += 1
        if foundFlag == True:
            print("Заметка удалена.")
        else:
            print("Заметка не найдена.")
        

    def editNote(self):
        pass

    def readNotebook(self):
        pass

    def writeNotebook(self):
        pass

    @property
    def printNotebook(self):
        print("Список заметок: \n")
        returnString = ""
        for i in range(len(self._list)):
            returnString += self._list[i].printNote + "------------------------------------------\n"
        return returnString