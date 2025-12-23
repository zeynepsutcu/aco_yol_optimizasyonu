# ACO ile Çoklu Senaryo Rota Optimizasyonu (İstanbul)

Bu proje, **Gezgin Satıcı Problemi'ni (TSP)** çözmek için **Karınca Kolonisi Algoritması (Ant Colony Optimization -ACO)** kullanan, modüler yapıda geliştirilmiş bir Python uygulamasıdır.

Proje, kullanıcıya Streamlit arayüzü üzerinden dinamik olarak senaryo seçme ve farklı coğrafi koşullarda en kısa rotayı hesaplama imkanı sunar.

## 🌍 Desteklenen Senaryolar

### Senaryo: İstanbul Turist Rotası 
* **Amaç:** Bir tur şirketinin, İstanbul'daki 15 tarihi mekanı (Sultanahmet, Galata, Ortaköy, Çamlıca vb.) turistlere en az vakit kaybıyla gezdirmesi.
* **Odak:** Şehir içi karmaşası ve Avrupa-Anadolu yakası geçiş optimizasyonu.

---

## 🚀 Teknik Özellikler

- **Dinamik Senaryo Yönetimi:** Tek bir kod tabanı üzerinden veri setleri (İstanbul) dinamik olarak değiştirilebilir.
- **Hibrit Mesafe Motoru:**
  - 🚦 **Google Maps Distance Matrix API:** İstanbul senaryosunda köprü geçişlerini ve karayolu kısıtlamalarını hesaba katarak *gerçek sürüş mesafesini* hesaplar.
  - 📏 **Haversine (Kuş Uçuşu):** API kotası dolsa bile matematiksel formüllerle sistem çalışmaya devam eder (Fallback mekanizması).
- **Parametrik Kontrol:** Karınca sayısı, $\alpha$, $\beta$ ve buharlaşma oranı ($\rho$) gibi ACO hiperparametreleri arayüzden anlık olarak değiştirilebilir.

## 📂 Proje Klasör Yapısı

```text
aco_yol_optimizasyonu/
│
├── main.py               # Senaryo seçimi ve ana arayüz
├── requirements.txt      # Bağımlılıklar
├── .env                  # Google API Anahtarı (Gizli)
│
├── data/
│   └── istanbul_data.py  # İstanbul verisi (Tarihi mekanlar)
│
├── core/
│   ├── ant_algorithm.py  # ACO Algoritma Sınıfı (Senaryodan bağımsız)
│   ├── matrix_utils.py   # Akıllı mesafe matrisi oluşturucu
│   └── haversine.py      # Yedek hesaplama modülü
│
└── visual/
    └── plotting.py       # Harita ve grafik çizim araçları
