# Teste de Software com Python - Pytest

## Prof. Raphael Muniz

### Programa: Identifier

### Particionamento em Classes de Equivalência

``implementação: test_identifier.py``

Comprimento (t)
            Válidas      -     Inválidas
         1 <= t <= 6 (1) - t < 1 (2) e t > 6 (3)
Iniciar com uma letra (i)
            Válidas      -     Inválidas
    Inicia com letra (4) - Não inicia com letra (5)
Contém letras ou dígitos (c)
            Válidas                    -     Inválidas
   Contém apenas letras ou dígitos (6) - Não contém apenas letras ou dígitos (7)

Suite de teste: T0 = {(a5, Válido), (“”, Inválido), (665432197, Inválido), (B*ss1, Inválido)}
            Classes:   (1)(4)(6)        (2)               (3)(5)                (7)