# from identifier import Identifier
from fake import Identifier

if __name__ == "__main__":
    id = Identifier()

    dado = "a12345"

    if id.Identificador(dado):
        print("A string " + dado + " é um identificador válido.")
    else:
        print("A string " + dado + " não é um identificador válido.")