import notebook
import note

def menu(notebookObj):
    menuFlag = True
    while menuFlag:
        print("\n-----Записная книжка-----")
        print("--------- Меню ----------")
        print("- 1 - показать записи")
        print("- 2 - добавить запись")
        print("- 3 - изменить запись")
        print("- 4 - удалить запись")
        print("- 5 - сохранить в файл")
        print("- 6 - считать из файла")
        print("- 0 - завершить работу")

        user_operation = input("\nУкажите пункт меню: ")
        if user_operation.isdigit():
            user_operation = int(user_operation)
            if user_operation == 1:
                notebookObj.sortByDateTime
                print(notebookObj.printNotebook)
            elif user_operation == 2:
                newNote = notebookObj.buildNote
                notebookObj.addNote(newNote)
                notebookObj.sortByDateTime
            elif user_operation == 3:
                notebookObj.editNote
            elif user_operation == 4:
                notebookObj.removeNote
            elif user_operation == 5:
                notebookObj.writeNotebook
            elif user_operation == 6:
                notebookObj.readNotebook
            elif user_operation == 0:
                menuFlag = False
            else:
                print("\nНеверный ввод.")
        else:
            print("\nНеверный ввод.")