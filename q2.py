import math
import numpy as np

vetor = [(3**i+7*math.factorial(i)) if i%2==0 else (2**i+math.log(i)) for i in range(0,10)]
vetor = np.array(vetor)

i, = np.where(vetor == max(vetor))

print("O valor máximo encontra-se na posição {0}.".format(i))
print("A média dos valores do vetor é {0}.".format(round(np.mean(vetor),2)))
#print("O desvio padrão do vetor é {0}.".format(round(np.std(vetor),2)))
