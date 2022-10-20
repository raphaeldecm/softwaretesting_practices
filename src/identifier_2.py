import re


class TestIdentifier():
    def CaseTestLen(self, value):
        if len(value) >= 1 and len(value) <= 6:
            return True
        return False

    def CaseTestInitLetter(self, value):
        if value[0].isalpha():
            return True
        return False

    def CaseTestContentLetterAndNumber(self, value):
        result = [v for v in value if (v >= 'a' and v <= 'z') or (v >= 'A' and v <= 'Z') or (v >= '0' and v <= '9')]
        if len(result) < len(value):
            return False
        return True
