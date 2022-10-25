class Identifier():
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

    def Identificador(self, value):
        if self.CaseTestLen(value) and self.CaseTestInitLetter(value) and self.CaseTestContentLetterAndNumber(value):
            return True
        else:
            return False

# if __name__ == "__main__":
#     main(sys.argv[1:])
