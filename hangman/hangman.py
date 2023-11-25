while True: 

    from random import randint
        
    liste =['Adana', 'Adıyaman', 'Afyonkarahisar', 'AğrI', 'Amasya', 'Ankara', 'Antalya', 'Artvin', 'AydIn', 'BalIkesir', 'Bilecik', 'Bingöl', 'Bitlis', 'Bolu', 'Burdur', 'Bursa', 'Çanakkale', 'ÇankIrI', 'Çorum', 'Denizli', 'DiyarbakIr', 'Edirne', 'ElazIğ', 'Erzincan', 'Erzurum', 'Eskişehir', 'Gaziantep', 'Giresun', 'Gümüşhane', 'Hakkari', 'Hatay', 'Isparta', 'Mersin', 'istanbul', 'izmir', 'Kars', 'Kastamonu', 'Kayseri', 'KIrklareli', 'KIrşehir', 'Kocaeli', 'Konya', 'Kütahya', 'Malatya', 'Manisa', 'Kahramanmaraş', 'Mardin', 'Muğla', 'Muş', 'Nevşehir', 'Niğde', 'Ordu', 'Rize', 'Sakarya', 'Samsun', 'Siirt', 'Sinop', 'Sivas', 'Tekirdağ', 'Tokat', 'Trabzon', 'Tunceli', 'ŞanlIurfa', 'Uşak', 'Van', 'Yozgat', 'Zonguldak', 'Aksaray', 'Bayburt', 'Karaman', 'KIrIkkale', 'Batman', 'ŞIrnak', 'BartIn', 'Ardahan', 'IğdIr', 'Yalova', 'Karabük', 'Kilis', 'Osmaniye', 'Düzce']
    sayi = randint(0,len(liste)-1)
    sehir = str(liste[sayi]).upper() #şehri listeden alıp str ye çevirip harflerini küçültme işlemi

    #str ye çevrilmiş harfleri parçalayıp listede tutma işlemi
    parcalanmisHarfler = []
    for i in sehir:
        parcalanmisHarfler.append(i)
    # print(parcalanmisHarfler)
    parcalanmisHarfler2 = parcalanmisHarfler.copy()

    altcizgiListe = []
    # hangman listesi
    hangmanListe = ["        |","        0","       /","       /|","       /|\\","        |","       /","       / \\",]
    hangmanTradeList = []
    count1 = 0

    harfListesi = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]
    secilenHarfler = []
    tahminListesi = []
    print()
    print(25*"*","Hangman Başlıyor",25*"*")
    print()
    print(f"Bulmacanız Türkiye`nin {len(sehir)} harfli illerinden biri: ")
    print("_________",end="")
    print(10*"\n")

    # random getirilen şehir kadar altçizgi oluşturma
    for i in range(0,len(parcalanmisHarfler)):
        altcizgiListe.append(" __ ")


    count = 0
    while True:
        print(*altcizgiListe, sep=" ") # tirelerin silinip harfin eklendiği çıktı
        print()
        control = True
        print("Tahminleriniz: ",*tahminListesi,sep=" - ")
        print()
        tahmin = input("Tahmininizi yazınız: ").upper()
        tahminListesi.append(tahmin.upper())
        print()
        #Dogru veya yanlıs kısmı
        if tahmin == sehir:
            print(15*("*"),"T E B R I K L E R  O Y U N U  K A Z A N D I N I Z !!",15*("*"))
            print()
            print(35*" ",sehir)
            print()
            break
        else: # harf seçimi, seçilen harfleri gösterme ve aynı harf seçim kontrol işlemleri
            print("Yanlış cevap !!!")
            print()
            while control:
                print("Seçmiş olduğunuz harfler: ",*secilenHarfler,sep=" ")
                print()
                harf = input("Harf giriniz: ").upper()
                print()
                if harf in secilenHarfler: # aynı harfi secerse uyarı kodu
                    print(10*("-"),"Aynı harfi daha önce seçtiniz !!!",10*("-"))
                    control = True
                else:
                    harfListesi.remove(harf)
                    secilenHarfler.append(harf)
                    control = False
                print()
                print("Kalan harfleriniz: ",*harfListesi,sep=" ")
                print()
        
        #Bütün harfleri bilme durumu    
        if len(parcalanmisHarfler) == 0: # bütün harfler dogru tahmin edildiginde dongüden cıkma islemi
            print(15*("*"),"T E B R I K L E R  O Y U N U  K A Z A N D I N I Z !!",15*("*"))
            print()
            print(35*" ",sehir)
            print()
            parcalanmisHarfler.clear()
            break

        #Doğru harf ve karsılıgında olusan görsel kısmı
        if harf in parcalanmisHarfler: #girilen harfi tahmin edilen içinde arama işlemi
            print("Tebrikler doğru harf :)")
            print()
            for i in range(0,parcalanmisHarfler.count(harf)): # girilen harf tahmin edilmişse birden fazla var ise
                parcalanmisHarfler.remove(harf) # onu parcalanmisHarflerden silme islemi

            count2 = 0
            listeHarfIndex = []
            for i in parcalanmisHarfler2:
                if harf == i:
                    listeHarfIndex.append(count2)
                count2 += 1

            for i in range(0,(parcalanmisHarfler2.count(harf))):
                altcizgiListe.pop((listeHarfIndex[i])) # indexinde göre tire silindi
                altcizgiListe.insert(listeHarfIndex[i],harf) # yerine aynı index e göre bilinen harf eklendi
            listeHarfIndex.clear()
            
        #Yanlış Harf,harf kalmaması ve Hangman Shape kısmı
        else:
            print("Yanlış harf seçimi !!! ")
            print("_________")
            if count1 != 3 and count1 != 4 and count1 != 7:
                hangmanTradeList.append(hangmanListe[count1]) 
            elif count1 == 3:
                hangmanTradeList.remove("       /")           # silinmesi gereken
                hangmanTradeList.append(hangmanListe[count1]) # yerine eklenmesi gereken (öteleme işlemi)
            elif count1 == 4:                                 # yerine eklenen hemen ardından aşagıda printleniyor
                hangmanTradeList.remove("       /|")
                hangmanTradeList.append(hangmanListe[count1])
            elif count1 == 7 and harf not in parcalanmisHarfler:
                # print("\n")
                hangmanTradeList.remove("       /")
                hangmanTradeList.append(hangmanListe[count1])
                print(*hangmanTradeList,sep="\n")
                print()
                print("O Y U N U  K A Y B E T T I N I Z :(")
                print()
                print(35*" ",sehir)
                print()
                break
            print(*hangmanTradeList,sep="\n")
            print(2*"\n")
            count1 += 1

    # oyunu tekrar ettirme işlemi
    tekrarOyun = input("Tekrar oynamak ister misiniz ? Y / N: ")
    if tekrarOyun.upper() == "N":
        break
    elif tekrarOyun.upper() == "Y" and tekrarOyun.lower() != "N":
        print()
        print("OK !!")        

