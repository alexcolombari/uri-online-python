# https://www.urionlinejudge.com.br/judge/pt/problems/view/1020

x = int(input())

ano = int(x / 365)
mes = int(x % 365 / 30)
dia = (x % 365 % 30)

print('%d ano(s)\n%d mes(es)\n%d dia(s)' %(ano, mes, dia))
