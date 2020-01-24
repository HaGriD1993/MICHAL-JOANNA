plik = open('adult.data','r')
zawartosc = plik.readlines()
wszysycy = 0
iloscLudzi = 0
iloscKobiet = 0
iloscMezczyzn = 0

iloscLudziMniej = 0
iloscKobietM = 0
iloscMezczyznMniej = 0


for badani in zawartosc:
    data = badani.split(",")
    if len(data) > 2:
        peopleb = int(data[0])
        if peopleb >=18 and peopleb <=25:
            wszysycy +=1
#print( "Wszysycy Ludzie" + str(wszysycy))



for AllPeople in zawartosc:
    data = AllPeople.split(",")
    if len(data) > 2:
        people = int(data[0])
        if people >= 18 and people <= 25:
            if data[14].strip() == '<=50K':
                iloscLudzi += 1
#print("Ludzie Zarabiający " + str(iloscLudzi))


for kazdaKobieta in zawartosc:
    data = kazdaKobieta.split(",")
    if len(data) > 2:
        kobiety = int(data[0])
        if kobiety >= 18 and kobiety <= 25:
            if data[14].strip() == '<=50K' and data[9].strip() == 'Female':
                iloscKobiet += 1
#print("Kobiety Zarabiajace " + str(iloscKobiet))

for kazdyMezczyzna in zawartosc:
    data = kazdyMezczyzna.split(",")
    if len(data) > 2:
        mezczyzni = int(data[0])
        if mezczyzni >= 18 and mezczyzni <= 25:
            if data[14].strip() == '<=50K' and data[9].strip() == 'Male':
                iloscMezczyzn += 1
#print("Mezczyzni Zarabiajacy " + str(iloscMezczyzn))




for AllPeople in zawartosc:
    data = AllPeople.split(",")
    if len(data) > 2:
        people = int(data[0])
        if people >= 18 and people <= 25:
            if data[14].strip() == '>50K':
                iloscLudziMniej += 1
#print("Ludzie Zarabiający mniej " + str(iloscLudziMniej))

for kazdaKobieta in zawartosc:
    data = kazdaKobieta.split(",")
    if len(data) > 2:
        kobiety = int(data[0])
        if kobiety >= 18 and kobiety <= 25:
            if data[14].strip() == '>50K' and data[9].strip() == 'Female':
                iloscKobietM += 1
#print("Kobiety Zarabiajace mniej " + str(iloscKobietM))

for kazdyMezczyzna in zawartosc:
    data = kazdyMezczyzna.split(",")
    if len(data) > 2:
        mezczyzni = int(data[0])
        if mezczyzni >= 18 and mezczyzni <= 25:
            if data[14].strip() == '>50K' and data[9].strip() == 'Male':
                iloscMezczyznMniej += 1
#print("Mezczyzni Zarabiajacy mniej " + str(iloscMezczyznMniej))
