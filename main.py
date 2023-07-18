import notebook, note

notebookOne = notebook.Notebook()

note1 = note.Note(1, "hshks", "jskfjljls", 12)
note2 = note.Note(2, "hssgsssss", "jgsgss", 13)

notebookOne.addNote(note1)
notebookOne.addNote(note2)

print(notebookOne.printNotebook)
#print(note1.id)
#print(note1.header)
#print(note1.printNote)
