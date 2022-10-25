import re


class TestIdentifier():
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
