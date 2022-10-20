import re

import identifier

# import identifier_2


def main():
    id = identifier.TestIdentifier()

    dado = input("Digite um dados de entrada: ")

    if id.CaseTestLen(dado) and id.CaseTestInitLetter(dado) and id.CaseTestContentLetterAndNumber(dado):
        print("A string " + dado + " é um identificador válido.")
    else:
        print("A string " + dado + " não é um identificador válido.")

main()
