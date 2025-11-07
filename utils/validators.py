def validar_aluno(aluno):
    obrigatorios = ['Nome', 'Turma', 'Responsavel', 'Fone']
    erros = [c for c in obrigatorios if not aluno.get(c)]
    return erros
