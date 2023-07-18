from datetime import datetime

class Note():
    def __init__(self, id, header, body, dateTime):
        self._id = id
        self._header = header
        self._body = body
        self._dateTime = dateTime

    @property
    def id(self):
        return self._id
    
    @property
    def header(self):
        return self._header
    
    @property
    def body(self):
        return self._body
    
    @property
    def dateTime(self):
        return self._dateTime
    
    @property
    def printNote(self):
        return "ID: " + str(self.id) + "\n" + "Заголовок: " + str(self.header) + "\n" + "Содержание: " + str(self.body) + "\n" + "Последнее изменение: " + str(self.dateTime) + "\n"

    @header.setter
    def header(self, newHeader):
        self._header = newHeader

    @body.setter
    def body(self, newBody):
        self._body = newBody

    @dateTime.setter
    def dateTime(self):
        self._dateTime = datetime.now()
