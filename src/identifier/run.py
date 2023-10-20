from identifier import Identifier
from fake import TestIdentifier

if __name__ == "__main__":
    # id = Identifier()
    id = TestIdentifier()

    dado = "a12345"

    if id.Identificador(dado):
        print("A string " + dado + " é um identificador válido.")
    else:
        print("A string " + dado + " não é um identificador válido.")