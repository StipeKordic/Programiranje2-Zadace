def obrnuto_rekurzija(x):
           if len(x)==1:
                      return x
           else:
                      return obrnuto_rekurzija(x[1::]) + x[0]



