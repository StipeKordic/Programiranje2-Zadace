def pozdrav(ime):
           print("Pozdrav", ime + "!")


dobrodošao = lambda ime: print("Dobrodošao", ime + "!")

def treca(funkcija):
           funkcija("Stipe")


treca(pozdrav)
treca(dobrodošao)
