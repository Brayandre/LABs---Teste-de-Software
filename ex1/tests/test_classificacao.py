from classificacao import classificar_aluno

def test_aprovado():
    assert classificar_aluno(8.0, 80) == "Aprovado"

def test_reprovado():
    assert classificar_aluno(3.0, 90) == "Reprovado"