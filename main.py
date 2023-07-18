import notebook, note
import menu
from datetime import datetime

notebookOne = notebook.Notebook()

note1 = note.Note(1, "Дело 1", "Сделать дело 1", datetime.now())
note2 = note.Note(2, "Дело 2", "Сделать дело 2", datetime.now())
note3 = note.Note(3, "Дело 3", "Сделать дело 3", datetime.now())


notebookOne.addNote(note1)
notebookOne.addNote(note2)
notebookOne.addNote(note3)

#menu.menu(notebookOne)

print(notebookOne.printNotebook)

notebookOne.removeNote(2)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(notebookOne.printNotebook)
#print(note1.id)
#print(note1.header)
#print(note1.printNote)
