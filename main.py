import random

# Kullanıcıdan sabit numaraları al
sabit_numaralar = []
for i in range(3):
    numara = int(input(f"{i+1}. Sabit Numarayı Girin: "))
    sabit_numaralar.append(numara)

# Sabit numaralar haricinde; 1 ile 80 sayıları arasında, 7 rastgele sayı seçimi
rastgele_numaralar = random.sample([i for i in range(1, 80) if i not in sabit_numaralar], 7)

# İki listeyi birleştir
final_numbers = sabit_numaralar + rastgele_numaralar

# Küçükten büyüğe listelemek için sorted edebiliriz.
sorted_numbers = sorted(final_numbers)


# Sonuçları yazdır
print("Rastgele Üretilen Sayılar:", sorted_numbers)