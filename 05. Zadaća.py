def parni(n):
           for i in range(n):
                      if i % 2 == 0:
                                 yield i
def neparni(n):
           for i in range(n):
                      if i % 2 == 1:
                                 yield i
                      

broj = int(input("Unesi broj: "))
generator_parnih = parni(broj)
generator_neparnih = neparni(broj)


brojevi = zip(generator_parnih,generator_neparnih)
print("Parni:         Neparni:")
for parni, neparni in brojevi:
           print(" ",parni,"               ", neparni)


