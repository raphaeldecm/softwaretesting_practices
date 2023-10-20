class Identifier():
    def CaseTestLen(self, value):
        if value == "a" or value == "a12345":
            return True
        return False

    def CaseTestInitLetter(self, value):
        if value == "a" or value == "a12345":
            return True
        return False

    def CaseTestContentLetterAndNumber(self, value):
        if value == "a" or value == "a12345":
            return True
        return False
    
    def Identificador(self, value):
        if self.CaseTestLen(value) and self.CaseTestInitLetter(value) and self.CaseTestContentLetterAndNumber(value):
            return True
        else:
            return False
