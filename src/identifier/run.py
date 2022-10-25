import re

from identifier.identifier import Identifier

# import identifier


def main():
    # id = identifier.TestIdentifier()
    id = Identifier()

    dado = "a5"

    if id.Identificador(dado):
        print("A string " + dado + " é um identificador válido.")
    else:
        print("A string " + dado + " não é um identificador válido.")

main()
