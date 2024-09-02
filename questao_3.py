import sys
import numpy as np #pip install numpy

faturamento = sys.argv[1].split(',') #rodar python ./questao_3.py n0,n1,n2,n3... (n valores desejados separados apenas por vírgula)
faturamento = [eval(i) for i in faturamento]

print("menor faturamento: {faturamento}".format(faturamento = min(faturamento)))
print("maior faturamento: {faturamento}".format(faturamento = max(faturamento)))

media = sum(faturamento)/np.count_nonzero(faturamento)
dias = 0
for i in faturamento:
    if i > media:
        dias = dias + 1

print ("dias superiores à media mensal: {dias}".format(dias = dias))
