# Çift Katmanlı Hibrit Filtreleme ile Gürültü Giderme

Bu projede, hem Gauss hem de Tuz-Biber (Salt-and-Pepper) gürültülerini aynı anda azaltmak için Çift Katmanlı Hibrit Filtreleme (Dual Layer Hybrid Filtering) yöntemi uygulanmıştır.  
Projede Python dili ve OpenCV kütüphanesi kullanılmıştır.

---

## İçindekiler
- [Proje Açıklaması](#proje-açıklaması)
- [Gauss Gürültüsü](#gauss-gürültüsü)
- [Tuz-Biber Gürültüsü](#tuz-biber-gürültüsü)
- [Gauss Filtresi](#gauss-filtresi)
- [Medyan Filtresi](#medyan-filtresi)
- [Çift Katmanlı Hibrit Filtreleme](#çift-katmanlı-hibrit-filtreleme)
- [Kullanılan Fonksiyonların Açıklamaları](#kullanılan-fonksiyonların-açıklamaları)
- [Avantajlar ve Dezavantajlar](#avantajlar-ve-dezavantajlar)
- [Kurulum ve Çalıştırma](#kurulum-ve-çalıştırma)
- [Örnek Çıktılar](#örnek-çıktılar)

---

## Proje Açıklaması

Bu proje, farklı türdeki gürültülerin aynı görüntü üzerinde bulunması durumunda hem Gauss hem de Tuz-Biber gürültülerini aynı anda etkili bir şekilde temizlemek amacıyla geliştirilmiştir.  
İlk aşamada Medyan Filtre uygulanarak tuz-biber gürültüsü temizlenir, ardından Gaussian Filtre uygulanarak düşük seviyeli Gauss gürültüsü giderilir.

---

## Gauss Gürültüsü

Gauss gürültüsü, görüntüdeki piksellerin rastgele sapmalar göstermesiyle oluşur.  
- **Mean (Ortalama):** 0'dan farklı olduğunda parlaklık değişir.
- **Sigma (Standart Sapma):** Artarsa gürültü şiddeti artar.

> - Mean genellikle **-30 ile +30** arası
> - Sigma genellikle **5 ile 50** arası değer alır.

**Görseller:**
- ![Orijinal Görsel](Gürültülü%20filtreli%20ve%20orjinal%20resimler/orjinal.png)
- ![Gauss Gürültülü Görsel](Gürültülü%20filtreli%20ve%20orjinal%20resimler/gauss.png)

---

## Tuz-Biber Gürültüsü

Bazı piksellerin tamamen siyah (0) veya beyaz (255) olmasıyla oluşur.  
- **salt_prob** ve **pepper_prob** oranları belirlenerek gürültü yoğunluğu ayarlanır.
- Rastgele seçilen koordinatlar değiştirilir.

**Görseller:**
- ![Tuz-Biber Gürültülü Görsel](Gürültülü%20filtreli%20ve%20orjinal%20resimler/tuz%20biber%20var.png)

---

## Gauss Filtresi

Gaussian filtre, piksellerin ağırlıklı ortalama değerlerini alarak görüntüyü yumuşatır.  
Detay kaybına yol açabilir ancak Gauss gürültüsünü etkin şekilde azaltır.

**Görseller:**
- ![Gaussian Filtre Sonrası](Gürültülü%20filtreli%20ve%20orjinal%20resimler/gauss%20filtresi.png)

---

## Medyan Filtresi

Medyan filtre, küçük bir pencere içindeki pikselleri sıralar ve ortanca (medyan) değeri seçerek gürültüyü azaltır.  
Özellikle Tuz-Biber gürültüsünde oldukça etkilidir.

**Görseller:**
- ![Medyan Filtre Sonrası](Gürültülü%20filtreli%20ve%20orjinal%20resimler/medyan%20filtresi.png)

---

## Çift Katmanlı Hibrit Filtreleme

İlk olarak Medyan Filtre, ardından Gauss Filtre uygulanır.  
Bu sıralama ile hem ani keskin değişimler hem de düşük seviyeli sapmalar giderilir.

**Görseller:**
- ![Çift Katmanlı Hibrit Doğru Uygulama](Gürültülü%20filtreli%20ve%20orjinal%20resimler/dogru%20ikinci.png)
- ![Çift Katmanlı Hibrit Yanlış Uygulama](Gürültülü%20filtreli%20ve%20orjinal%20resimler/yanlis%20ikinci.png)

---

## Kullanılan Fonksiyonların Açıklamaları

- `image.shape`: Resmin yüksekliğini, genişliğini ve kanal sayısını verir.
- `np.clip()`: Piksellerin değerlerini 0-255 arasına sınırlar.
- **Gauss Gürültüsü Ekleme:** Mean ve Sigma değerlerine göre rastgele sapmalar eklenir.
- **Tuz-Biber Gürültüsü Ekleme:** Random koordinatlara 0 veya 255 değeri atanır.
- **GaussianBlur():** Piksellerin ağırlıklı ortalamasını alır, bulanıklaştırır.
- **medianBlur():** Piksellerin medyan değerini alarak keskin gürültüleri yok eder.

---

## Avantajlar ve Dezavantajlar

| Yöntem                       | Avantajlar                                           | Dezavantajlar                                                       |
|:-----------------------------|:-----------------------------------------------------|:--------------------------------------------------------------------|
| **Medyan Filtre**            | Tuz-biber gürültüsünü iyi temizler. Kenarları korur. | Çok kullanılırsa detay kaybı olur.                                  |
| **Gauss Filtre**             | Gauss gürültüsünü azaltır, hesaplaması basittir.     | Tuz-biber gürültüsüne etkisizdir. Kenarları bulanıklaştırır.        |
| **Çift Katmanlı Hibrit**     | Her iki gürültüyü aynı anda temizler.                | Yanlış sıralamada sonuç kötüleşir. Hesaplama maliyeti biraz artar.  |

---
## Kurulum ve Çalıştırma

**Gerekenler:**

```
pip install opencv-python numpy matplotlib

```

Çalıştırmak için:

Bu projede .ipynb uzantılı bir Jupyter Notebook kullanılmıştır.

Jupyter Notebook'u açmak için terminal veya komut satırına şu komutu yazın:
```
jupyter notebook
```
Açılan sayfada proje dosyasını (proje.ipynb) açıp adım adım çalıştırabilirsiniz.


Örnek Çıktılar
Tüm çıktı görselleri Gürültülü filtreli ve orjinal resimler/ klasörü içerisinde bulunmaktadır.

## **Dosya Yapısı**
```
Gürültülü filtreli ve orjinal resimler/
├── orijinal.png
├── gauss.png
├── Tuz-Biber var.png
├── medyan filtresi.png
├── gauss filtresi.png
├── dogru ilk katman.png
├── dogru ikinci.png
├── yanlış ilk .png
├── yanlış ikinci.png
```




