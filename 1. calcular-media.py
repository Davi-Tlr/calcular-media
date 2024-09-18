nome = input("Digite o nome do aluno: ")
nota1 = int(input("Digite a primeira nota do aluno: "))
nota2 = int(input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2) /2
if media < 6: situacao = 'Nota Insuficiente'
elif media > 5 and media < 8: situacao = 'Nota Regular'
elif media > 7 and media < 9: situacao = 'Nota Boa'
elif media >= 9: situacao = 'Nota Excelente'
print (f'o aluno {nome} tem média igual à {media}, portanto sua nota é considerada: {situacao}')
