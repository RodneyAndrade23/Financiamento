vc = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário mensal? '))
financiamento = int(input('Em quantos anos você irá pagar a casa? '))
n = salario - (30/100)
p = vc/financiamento/12
if p <= n:
    print('Você poderá comprar a sua casa com segurança, pagando R${:.2f} mensais durante {} anos!'.format(p, financiamento))

else:
    print('Seu empréstimo foi negado por exceder o limite de 30% da sua renda mensal!')
