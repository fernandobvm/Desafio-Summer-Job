dict = {'Aluno' : 0}

for i in range(0,5):
    aluno = input('Insira o nome do aluno:')
    nota = input('Insira a nota do aluno:')
    dict[aluno] = nota

del dict['Aluno']
maior_nota = max(dict.values())
for key, value in dict.items():
    if value == maior_nota:
        print("{0} {1}".format(key,value))