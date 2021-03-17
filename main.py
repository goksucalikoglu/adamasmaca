# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

kelimeler = ["yönetim" , "bilişim" , "sistem" , "akustik" , "istasyon" , "köpek" , "kedi" , "yengeç" , "karpuz" , "kiraz"]
kelime = random.choice(kelimeler) #rastgele bir kelime seçtik
tahminSayisi = 5
harfler = [] #kullanicinin girdigi tum harfleri bu listeye ekleyerek tekrar ayni harf girilirse uyari verecegiz
x = len(kelime)
z = list('_' * x)
print(' '.join(z), end='\n')
while tahminSayisi > 0:
    y = input("Bir harf tahmin edin : ")
    if y in harfler:
        print("Lutfen daha once tahmin ettiginiz harfleri tekrar tahmin etmeyin...")
        continue

    elif len(y) > 1:
        print("Lutfen sadece bir harf girin.")
        continue

    elif y not in kelime:   #girilen harf kelime icinde yoksa eger
        tahminSayisi -= 1
        print("yanlis tahmin!. {} tane tahmin hakkiniz kaldi.".format(tahminSayisi))

    else:
        for i in range(len(kelime)):
            if y == kelime[i]:
                print("Dogru Tahmin")
                z[i] = y
                harfler.append(y)
        print(' '.join(z), end='\n')

    cevap = input("Kelimenin tamamini tahmin etmek istiyor musunuz? ['e' veya 'h'] : ")

    if cevap == "e":
        tahmin = input("Kelimenin tamamini tahmin edebilirsiniz : ")
        if tahmin == kelime:
            print("Tebrikler bildiniz...")
            break
        else:
            tahminSayisi -= 1
            print("Yanlis tahmin ettiniz. {} tane tahmin hakkiniz kaldi.".format(tahminSayisi))


    if tahminSayisi == 0:
        print("Tahmin hakkiniz kalmadi. Kaybettiniz! Adam Asildi.")
        break

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
