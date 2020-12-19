cont = 0
for i in range(1,5000001):
    if(i%2==0 and i%37==0 and i%49==0):
        cont = cont + 1

print("A quantidade de números que satisfazem tal condição é {0}".format(cont))