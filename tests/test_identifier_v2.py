import pytest
from src.identifier.identifier import Identifier


class Test_Identifier():

    def setUp(self):
        print("Inside of setUp")
        pass

    def tearDown(self):
        print("Inside of tearDown")
        pass

    def test_D1_class_2_5_invalid(self):
        print("Inside of test_D1_class_2_5_invalid")
        id_obj = Identifier()
        dadoDeTeste = " "
        resultado_esperado = False
        resultado_obtido = id_obj.Identificador(dadoDeTeste)

        assert resultado_obtido == resultado_esperado

    def test_D2_class_1_4_6_valid(self):
        print("Inside of test_D2_class_1_4_6_valid")
        id_obj = Identifier()
        dadoDeTeste = "a"
        resultado_esperado = True
        resultado_obtido = id_obj.Identificador(dadoDeTeste)

        assert resultado_obtido == resultado_esperado

    def test_D3_class_1_4_6_valid(self):
        print("Inside of test_D3_class_1_4_6_valid")
        id_obj = Identifier()
        dadoDeTeste = "a12345"
        resultado_esperado = True
        resultado_obtido = id_obj.Identificador(dadoDeTeste)

        assert resultado_obtido == resultado_esperado

    def test_D4_class_3_invalid(self):
        print("Inside of test_D4_class_3_invalid")
        id_obj = Identifier()
        dadoDeTeste = "a123456"
        resultado_esperado = False
        resultado_obtido = id_obj.Identificador(dadoDeTeste)

        assert resultado_obtido == resultado_esperado

    def test_D5_class_5_invalid(self):
        print("Inside of test_D5_class_5_invalid")
        id_obj = Identifier()
        dadoDeTeste = "2"
        resultado_esperado = False
        resultado_obtido = id_obj.Identificador(dadoDeTeste)

        assert resultado_obtido == resultado_esperado

    def test_D6_class_7_invalid(self):
        print("Inside of test_D6_class_7_invalid")
        id_obj = Identifier()
        dadoDeTeste = "A#$12"
        resultado_esperado = False
        resultado_obtido = id_obj.Identificador(dadoDeTeste)

        assert resultado_obtido == resultado_esperado
