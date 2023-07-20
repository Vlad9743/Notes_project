import note
from datetime import datetime
import json
from time import sleep

class Notebook():
    def __init__(self):
        self._list = []

    def addNote(self, newNote):
        self._list.append(newNote)
        print("\nЗаметка добавлена.\n")

    @property
    def buildNote(self):
        max_id = 0
        for i in range(len(self._list)):
            if max_id < int(self._list[i].id):
                max_id = int(self._list[i].id)
        next_id = max_id + 1

        inputHeader = str(input("Введите заголовок заметки: "))
        inputBody = str(input("Введите содержание заметки: "))
        currentDateTime = datetime.now()
        newNote = note.Note(next_id, inputHeader, inputBody, currentDateTime)

        return newNote
    
    @property
    def removeNote(self):
        idToDelete = input("Введите id заметки для удаления: ")
        if idToDelete.isdigit():
            idToDelete = int(idToDelete)
            i = 0
            foundFlag = False
            while i < len(self._list) and foundFlag == False:
                if idToDelete == int(self._list[i].id):
                    self._list.pop(i)
                    foundFlag = True
                i += 1
            if foundFlag == True:
                print("Заметка удалена.\n")
            else:
                print("Заметка не найдена.\n")
        else:
            print("\nНеверный ввод.")

    @property    
    def editNote(self):
        idToEdit = input("Введите id заметки для редактирования: ")
        if idToEdit.isdigit():
            idToEdit = int(idToEdit)
            i = 0
            foundFlag = False
            while i < len(self._list) and foundFlag == False:
                if idToEdit == int(self._list[i].id):
                    foundFlag = True
                    print("Текущий заголовок: " + str(self._list[i].header))
                    self._list[i].header = input("Введите новый заголовок: ")
                    print("Текущее содержание: " + str(self._list[i].body))
                    self._list[i].body = input("Введите новое содержание: ")
                    self._list[i].dateTime = datetime.now()
                i += 1
            if foundFlag == True:
                print("Заметка изменена.\n")
            else:
                print("Заметка не найдена.\n")
        else:
            print("\nНеверный ввод.")

    @property
    def readNotebook(self):
        filename = str(input("Введите имя файла для чтения: "))
        try:
            file = open(filename + ".txt", "r", encoding="utf-8")
            self._list.clear()
            for line in file:
                noteDic = json.loads(line)
                self.addNote(note.Note(int(noteDic["id"]), noteDic["header"], noteDic["body"], datetime.strptime(noteDic["dateTime"], '%Y-%m-%d %H:%M:%S.%f')))
            file.close()
        except:
            print("Файл не найден.\n")

    @property
    def writeNotebook(self):
        filename = input("Введите имя файла для сохранения: ")
        file = open(filename + ".txt", "w", encoding="utf-8")
        for i in range(len(self._list)):
            stringJSON = "{"
            stringJSON += ('"id" : "' + str(self._list[i].id) + '", ')
            stringJSON += ('"header" : "' + str(self._list[i].header) + '", ')
            stringJSON += ('"body" : "' + str(self._list[i].body) + '", ')
            stringJSON += ('"dateTime" : "' + str(self._list[i].dateTime) + '"}')

            file.write(stringJSON)
            file.write("\n")

        file.close()

    @property
    def sortByDateTime(self):
        swapped = True
        while swapped:
            swapped =False
            for i in range(len(self._list) - 1):
                if self._list[i].dateTime < self._list[i+1].dateTime:
                    self._list[i], self._list[i+1] = self._list[i+1], self._list[i]
                    swapped = True

    @property
    def printNotebook(self):
        print("\n У вас " + str(self.numberOfNotes()) + " заметок:\n")
        returnString = ""
        for i in range(len(self._list)):
            returnString += self._list[i].printNote + "------------------------------------------\n"
        return returnString
    
    @property
    def basicNotebookGen(self):
        for i in range(5):
            noteTemp = note.Note(i+1, "Дело " + str(i+1), "Сделать дело " + str(i+1), datetime.now())
            self._list.append(noteTemp)
            sleep(0.01)
        return self._list
    
    def numberOfNotes(self):
        return len(self._list)