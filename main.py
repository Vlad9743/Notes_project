import notebook, note
import menu
from datetime import datetime
from time import sleep

notebookOne = notebook.Notebook()

note1 = note.Note(1, "Дело 1", "Сделать дело 1", datetime.now())
sleep(1)
note2 = note.Note(2, "Дело 2", "Сделать дело 2", datetime.now())
sleep(1)
note3 = note.Note(3, "Дело 3", "Сделать дело 3", datetime.now())


notebookOne.addNote(note1)
notebookOne.addNote(note2)
notebookOne.addNote(note3)

#menu.menu(notebookOne)

print(notebookOne.printNotebook)

#notebookOne.sortByDateTime
#print(notebookOne.printNotebook)

#notebookOne.writeNotebook
notebookOne.readNotebook
print(notebookOne.printNotebook)

#notebookOne.removeNote(2)
#print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#print(notebookOne.printNotebook)

#notebookOne.editNote(1)
#print(notebookOne.printNotebook)
#print(note1.id)
#print(note1.header)
#print(note1.printNote)
