dias = int(input())
ano = round(dias / 365 - 0.5)
mes = int((dias % 365) / 30)
dia = (dias % 365) % 30
print(ano, "ano(s)")
print(mes, "mes(es)")
print(dia, "dia(s)")
