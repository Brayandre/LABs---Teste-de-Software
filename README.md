# LABs---Teste-de-Software
Labs das aulas de TS - 6º semestre

# EX 1


src/classificacao.py      12      4     10      4    64%   3, 5, 7, 11
36 mutantes gerados | 6 killed | 30 survived (MS = 16.67%)

b)

* **Linhas não executadas (Falha em Alcançar):** 3, 5, 7, 11 (ValueError de média/presença[cite: 54], "Reprovado por falta"[cite: 54] e "Recuperacao"
* **Demais vivos (Falha em Infectar):** Fronteiras de media (0, 5.0, 7.0, 10) e presenca (0, 75, 100) não testadas pelas entradas 8.0, 3.0, 80, 90

c)

src/classificacao.py      12      0     10      0   100%
36 mutantes gerados | 36 killed | 0 survived | Equivalentes: 0 | MS Final = 100%

d)

Sem match, mutantes que trocam o texto de ValueError sobrevivem (falha em Revelar)

---

# EX 2

a)

src/carrinho.py       7      0      2      0   100%
12 mutantes gerados | 3 killed | 9 survived (MS = 25%)

100% de cobertura só garante alcance, mas o assert > 0 é fraco e não revela os defeitos

b e c)

12 mutantes gerados | 11 killed | 1 survived:
carrinho.x_total_com_desconto__mutmut_12: survived (round(total, 2) -> round(total, 3))

Falhou em **Infectar**: o desconto em [10, 20, 30, 40, 50] dá 141.0 exato, sem 3ª casa decimal para o round diferenciar

d)

12 mutantes gerados | 12 killed | 0 survived | MS Final = 100%

---

3

a e b)

1. ValueError("lista vazia") -> ValueError("XXlista vaziaXX") (nas 2 funções)
   Não equivalente (faltou match="lista vazia" - falha em Revelar).

2. for t in temps[1:]: -> for t in temps[0:]: (em maior)
   Equivalente (comparar temps[0] > temps[0] dá False e não muda m).

3. if t > m: -> if t >= m: (em maior)
   Equivalente (sobrescrever m com valor igual não muda o retorno).

4. range(1, len(temps)) -> range(0, len(temps)) (em dia_do_maior)
   Equivalente (em i=0, temps[0] > temps[0] é False, pos continua 0).

5. if temps[i] > temps[pos]: -> if temps[i] >= temps[pos]: (em dia_do_maior)
   Não equivalente (em caso de empate, troca o índice do primeiro maior pelo último).


c)

MS Antes = 73.9% | MS Depois = 100% (descontando os equivalentes do denominador)

d)

`maior` retorna o valor (empate mantém o mesmo número)[cite: 60]; `dia_do_maior` retorna o índice do **primeiro** maior dia (`>=` muda o retorno para o índice do último empate)
---

# EX 4

a,b,c)

src/parcelamento.py       8      0      4      0   100%
1 survived: parcelamento.x_parcela__mutmut_9 (if n <= 3: -> if n < 3:)

* **Análise do vivo:** **Equivalente**. A decisão só muda para n = 3, onde o else calcula 0.02 * (3 - 3) = 0.0 (mesmo juros = 0 do if)
* **MS Final:** **100%** (descontando 1 equivalente)

d)

if n <= 4:          #mut1       
    juros = 0
else:               #mut2
    juros = 0.02 * (n + 3) 


e)

FAILED tests/test_parcelamento.py::test_quatro_parcelas_com_juros (25.0 != 25.5)