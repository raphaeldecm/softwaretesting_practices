import pytest
from src.identifier.identifier import Identifier


class Test_Identifier():

    def setUp(self):
        print("Inside of setUp")
        pass

    def tearDown(self):
        print("Inside of tearDown")
        pass

    def test_class_1_4_6_valid(self):
        print("Inside of test_class_1_4_6_valid")
        id_obj = Identifier()
        dadoDeTeste = "a5"
        resultado_esperado = True
        resultado_obtido = id_obj.Identificador(dadoDeTeste)

        assert resultado_obtido == resultado_esperado

    def test_class_2_invalid(self):
        print("Inside of test_class_2_invalid")
        id_obj = Identifier()
        dadoDeTeste = " "
        resultado_esperado = False
        resultado_obtido = id_obj.Identificador(dadoDeTeste)

        assert resultado_obtido == resultado_esperado

    def test_class_3_5_invalid(self):
        print("Inside of test_class_3_5_invalid")
        id_obj = Identifier()
        dadoDeTeste = "665432197"
        resultado_esperado = False
        resultado_obtido = id_obj.Identificador(dadoDeTeste)

        assert resultado_obtido == resultado_esperado

    def test_class_7_invalid(self):
        print("Inside of test_class_7_invalid")
        id_obj = Identifier()
        dadoDeTeste = "B*ss1"
        resultado_esperado = False
        resultado_obtido = id_obj.Identificador(dadoDeTeste)

        assert resultado_obtido == resultado_esperado
