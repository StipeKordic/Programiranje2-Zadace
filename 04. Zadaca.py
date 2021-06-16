import re

mail_pattern = "(^[a-z]+)[.]([a-z]+)([@]fpmoz[.]sum[.]ba$)"

while 1:
           mail_unos = input("Unesi mail: ")
           podudaranje = re.match(mail_pattern, mail_unos)
           if podudaranje:
                      print("Uspješno ste unijeli vašu e-mail adresu!")
                      grupe = podudaranje.groups()
                      break
           else:
                      print("Format se ne podudara, pokušajte ponovo!")
#prvo slovo imena
psi = grupe[0][0]
#prezime
p = grupe[1]

eduid_pattern = "^"+psi+p+"(\d*@sum.ba$)"

while 1:
           eduid = input("Unesi eduid: ")
           match = re.match(eduid_pattern, eduid)
           if match:
                      print("Uspješno ste unijeli vaš eduid!")
                      break
           else:
                      print("Format se ne podudara, pokušajte ponovo!")




