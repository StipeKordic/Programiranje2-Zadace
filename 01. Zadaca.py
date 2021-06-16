
import random

imena = ['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko', 'Dario', 'Mihael',
'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon', 'Ivan', 'Ante', 'Ivan',
'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip', 'Tomislav', 'Luka', 'Ivan',
'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka', 'Ana', 'Emanuel',
'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante', 'Marijan', 'Mario',
'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan', 'Freda', 'Kristina',
'Josip', 'Lucija']


brojImena = {}


for ime in imena:
           brojImena[ime] = 0



ukupno_studenata = len(imena)
           
for ime in imena:
  if ime in brojImena:
    brojImena[ime] += 1
  else:
    brojImena[ime] = 1



imena_pojedinacno = []
kljucevi = brojImena.keys()
for ime in kljucevi:
           imena_pojedinacno.append(ime)


ocjene = {}
pozitivne_ocjene = 0
jedinice = 0
dvice = 0                           
trice = 0
cetvrtice = 0                       
petice = 0
for ime in imena_pojedinacno:
           for i in range(brojImena[ime]):
                      ocjene[ime+str(i+1)] = random.randint(1,5)
                      if ocjene[ime+str(i+1)] > 1:
                                 pozitivne_ocjene +=1
                      if ocjene[ime+str(i+1)] == 1:
                                 jedinice += 1
                      elif ocjene[ime+str(i+1)] == 2:
                                 dvice += 1
                      elif ocjene[ime+str(i+1)] == 3:
                                 trice += 1
                      elif ocjene[ime+str(i+1)] == 4:
                                 cetvrtice += 1
                      else:
                                 petice += 1
                      
                                 



parovi = ocjene.items()
for student, ocjena in parovi:
           print(student, ":", ocjena)


print("Prolaznost je:", (pozitivne_ocjene/ukupno_studenata)*100, "%")
print("Broj jedinica je:", jedinice)
print("Broj dvica je:", dvice)
print("Broj trica je:", trice)
print("Broj cetvrtica je:", cetvrtice)
print("Broj petica je:", petice)














