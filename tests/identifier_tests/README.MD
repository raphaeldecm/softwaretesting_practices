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

### Análise de Valor Limite

``implementação: test_identifier_v2.py``

### Passo 2: Definição dos casos de teste considerando os limites e as recomendações para o critério.
### Quais dados atentem as classes definidas para o critério (t)?

Comprimento (t): 1 <= t <= 6 (1)  e  t < 1 (2) e t > 6 (3)
D1 = Dado de teste 1
 
 D1 = “” - Inválido (2)(5)
 D2 = a - Válido (1)(4)(6)
 D3 = a12345 - Válido(1)(4)(6)
 D4 = a123456 - Inválido (3)

### Os dados de teste definidos atendem as demais classes dos critérios (i) e (c)?

### (i) Inicia com letra (4) e Não inicia com letra (5)
### (c) Contém apenas letras ou dígitos (6) Contém caracteres diferentes de letras e dígitos (7)

 D5 = 2 - Inválido (5)
 D6 = A#$12 - Inválido (7)
