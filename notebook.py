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
        

    def editNote(self, idToEdit):
        #idToEdit = input("Введите id заметки для редактирования: ")
        i = 0
        foundFlag = False
        while i < len(self._list) and foundFlag == False:
            if idToEdit == int(self._list[i].id):
                foundFlag = True
                print("Текущий заголовок: " + str(self._list[i].header))
                self._list[i].header = input("Введите новый заголовок: ")
                print("Текущее содержание: " + str(self._list[i].body))
                self._list[i].body = input("Введите новое содержание: ")
                
            i += 1
        if foundFlag == True:
            print("Заметка изменена.")
        else:
            print("Заметка не найдена.")

    def readNotebook(filename):
        pass

    def writeNotebook(self, filename):
        pass

    @property
    def sortByDateTime(self):
        for j in range(len(self._list) - 1):
            for i in range(j, len(self._list)-1):
                if self._list[i+1].dateTime > self._list[i].dateTime:
                    temp = self._list[i-1]
                    self._list[i-1] = self._list[i]
                    self._list[i] = temp



    @property
    def printNotebook(self):
        print("\n Список заметок: \n")
        returnString = ""
        for i in range(len(self._list)):
            returnString += self._list[i].printNote + "------------------------------------------\n"
        return returnString