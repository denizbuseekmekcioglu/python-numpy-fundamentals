# numpy_tum_komutlar.py
# Konu: NumPy Temel Komutlar
# Hazırlayan: Deniz Buse Ekmekçioğlu
# Ders: İstatistiksel Programlama

import numpy as np


# ============================================================
# ALIŞTIRMA 1
# 1'den 10'a kadar sayılardan oluşan bir NumPy array'i oluşturunuz.
# Bu array'in boyutunu, eleman sayısını ve veri tipini ekrana yazdırınız.
# ============================================================

array1 = np.arange(1, 11)

print("ALIŞTIRMA 1")
print("Array:", array1)
print("Boyut:", array1.ndim)
print("Eleman sayısı:", array1.size)
print("Veri tipi:", array1.dtype)
print("-" * 50)


# ============================================================
# ALIŞTIRMA 2
# 0 ile 20 arasında 2'şer artan sayılardan oluşan bir array oluşturunuz.
# Bu array'in toplamını, ortalamasını, en büyük ve en küçük değerini bulunuz.
# ============================================================

array2 = np.arange(0, 21, 2)

print("ALIŞTIRMA 2")
print("Array:", array2)
print("Toplam:", np.sum(array2))
print("Ortalama:", np.mean(array2))
print("En büyük değer:", np.max(array2))
print("En küçük değer:", np.min(array2))
print("-" * 50)


# ============================================================
# ALIŞTIRMA 3
# 1'den 12'ye kadar sayılardan oluşan bir array oluşturunuz.
# Bu array'i 3 satır ve 4 sütundan oluşan iki boyutlu bir matrise dönüştürünüz.
# Matrisin satır ve sütun sayısını ekrana yazdırınız.
# ============================================================

array3 = np.arange(1, 13)
matris = array3.reshape(3, 4)

print("ALIŞTIRMA 3")
print("Orijinal array:", array3)
print("3x4 matris:")
print(matris)
print("Matrisin şekli:", matris.shape)
print("Satır sayısı:", matris.shape[0])
print("Sütun sayısı:", matris.shape[1])
print("-" * 50)


# ============================================================
# Array girdi çıktı işlemleri
# ============================================================
# Bu başlıktan sonraki işlemler ayrı konu olarak devam ettirilebilir.
