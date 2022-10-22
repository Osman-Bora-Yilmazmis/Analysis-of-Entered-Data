import string #NOKTALAMA ISARETLERI BULUNMAKTADIR

def noktalama_isaretleri_ve_gereksiz_kelimeleri_ayiklama(metin): #METININ NOKTALAMA ISARETLERI VE GEREKSIZ KELIMELERDEN ARINDIRILDIGI FONKSIYONDUR
    yeni_metin=""
    stop_words_listesi=[]  #LISTE VE KULLANDIGIM SABITLER BURADA BULUNMAKTADIR
    yenilenmis_metin=""
    metnin_son_hali=""

    for i in metin:
        if i not in string.punctuation:
            yeni_metin += i #NOKTALAMA ISARETLERINDEN ARINDIRILMIS METIN
    try:
        dosyayi_ac = open("stop_words_turkish.txt", "r",encoding="utf8")  # Dosyayi acar.

        while True:
            stop_word = dosyayi_ac.readline()
            yeni_stop_word=stop_word.rstrip()
            if stop_word=="":
                break
            stop_words_listesi.append(yeni_stop_word)#STOP WORDLERIN HEPSININ TEK BIR LISTEDE TOPLANDIGI YER

        dosyayi_ac.close()#Dosyayı kapatır

    except IOError:#dosyada bir hata olma durumunda etkinlesmektedir
        print("HATA: Dosya açılamadı. Dosya tipi bozuk veya hatali olabilir.")

    aktarma=yeni_metin.replace('I','ı')  # PYTHON "I" YI KUCULUNCE "i" ye DONUSTURMEKTEDIR BURASI ONU "ı" ya CEVIRIR
    metnin_son_hali = aktarma.lower()  # Metni kucuk harflerle yazdirir

    x=metnin_son_hali.split() #KELIMELERI TEK TEK BOLMEK ICIN KULLANDIGIM LISTE
    for i in x:
        if i not in stop_words_listesi:
            yenilenmis_metin+= i
            yenilenmis_metin+=" "

    return yenilenmis_metin

def kalan_metine_ait_kelimeler_ve_tekrar_say(tertemiz_cikti): #KELİMELER VE TEKRAR SAYILARI BU FONKSIYONDA HESAPLANIR (1. TABLONUN ISTATISTIKLERININ HESAPLANDIGI YER)
    butun_kelimeler={}
    her_bir_kelime=tertemiz_cikti.split()#HER BIR KELIMEYI TEK TEK INCELEMEMIZI SAGLAR
    for kelime in her_bir_kelime:
        if kelime in butun_kelimeler:
            butun_kelimeler[kelime] += 1
        else:
            butun_kelimeler[kelime] = 1

    return butun_kelimeler

def o_uzunluktaki_kelime_say(tertemiz_cikti): #KELIMELERIN UZUNLUGUNUN HESAPLANDIGI YERDIR(2. TABLONUN ISTATISTIKLERININ HESAPLANDIGI YER)
    butun_kelimelerin_uzunlugu={}
    her_bir_kelime=tertemiz_cikti.split()#HER BIR KELIMEYI TEK TEK AYIRIR
    for kelime in her_bir_kelime:
        kelimenin_uzunlugu=len(kelime)
        if kelimenin_uzunlugu in butun_kelimelerin_uzunlugu:
            butun_kelimelerin_uzunlugu[kelimenin_uzunlugu] += 1
        else:
            butun_kelimelerin_uzunlugu[kelimenin_uzunlugu] = 1

    return butun_kelimelerin_uzunlugu

def cikti_ekrani(tertemiz_cikti,kelimeler_ve_sayisi,kelimelerin_uzunlugu): #TUM HESAPLAMALAR BITTIKTEN SONRA TABLOLARIN CIZDIRILDIGI KISIMDIR
    print("Noktalama isaretleri ve gereksiz kelimeler cikarildiktan sonra kucuk harflerle kalan metin:")
    print(tertemiz_cikti)
    print()
    print("Kalan metindeki kelimeler ve tekrar sayilari:")
    print("Kelime                                                                "," ","Tekrar Say")
    print("----------------------------------------------------------------------"," ","-----------")
    for key in kelimeler_ve_sayisi:
        key_uzunlugu=len(key)
        print(key," " * (76 - key_uzunlugu),kelimeler_ve_sayisi[key])
    print()

    print("Kalan metindeki her uzunluktaki kelime sayilari:")
    print("Uzunluk"," "," Kelime Say")
    print("-------"," "," ----------")
    kucukten_buyuge_siralanmis=sorted(kelimelerin_uzunlugu) #BURADA DICTIONARY KUCUKTEN BUYUGE SIRALANMAKTADIR
    for key in kucukten_buyuge_siralanmis:
        if key>= 10:
            print(key," " * 12 ,kelimelerin_uzunlugu[key])
        else:
            print(key, " " * 13, kelimelerin_uzunlugu[key])


def main():

    metin = input("İslem yapmak istediginiz metni giriniz:") #KULLANICIDAN METNI ALDIGIMIZ KISIM

    tertemiz_cikti=noktalama_isaretleri_ve_gereksiz_kelimeleri_ayiklama(metin)#METININ NOKTALAMA ISARETLERI VE GEREKSIZ KELIMELERDEN ARINDIRILDIGI FONKSIYONDUR

    kelimeler_ve_sayisi=kalan_metine_ait_kelimeler_ve_tekrar_say(tertemiz_cikti)#KELİMELER VE TEKRAR SAYILARI BU FONKSIYONDA HESAPLANIR (1. TABLONUN ISTATISTIKLERININ HESAPLANDIGI YER)

    kelimelerin_uzunlugu = o_uzunluktaki_kelime_say(tertemiz_cikti)#KELIMELERIN UZUNLUGUNUN HESAPLANDIGI YERDIR(2. TABLONUN ISTATISTIKLERININ HESAPLANDIGI YER)

    cikti_ekrani(tertemiz_cikti,kelimeler_ve_sayisi,kelimelerin_uzunlugu)#TUM HESAPLAMALAR BITTIKTEN SONRA TABLOLARIN CIZDIRILDIGI KISIMDIR

main() #ANA FONKSIYONUMUZUN CALISMASINI SAGLAR
