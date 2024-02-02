firstYear=int(input("Lütfen şehrin şimdiki nüfusunu giriniz:  "))
increaseRate=float(input("Lütfen nüfus artış oranını giriniz: "))
wantedPop=int(input("Lütfen hedef nüfusu giriniz: "))
counter=0
# bu counter while icin degil, kac yil gectigini bulmak icin.
if increaseRate>=0: #artan nüfus için
    while firstYear<=wantedPop:
        firstYear=firstYear+(firstYear*increaseRate/100)
        counter=counter+1
    print(counter , " yıl sonunda hedefe ulaşır.")
else:  #azalan nüfus için
    while firstYear>=wantedPop:
        firstYear=firstYear+(firstYear*increaseRate/100)
        counter=counter+1
    print(counter , " yıl sonunda hedefe ulaşır.")
input()