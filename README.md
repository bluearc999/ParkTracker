# 🚛 Bakiler Lojistik A.Ş. - Akıllı Otopark Takip Sistemi

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?style=for-the-badge&logo=streamlit)
![OS](https://img.shields.io/badge/OS-Linux%20%2F%20Ubuntu-FCC624?style=for-the-badge&logo=linux)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Bakiler Lojistik A.Ş. Akdeniz Nakliyat İş Merkezi sahasındaki tır ve otomobil park alanlarının anlık doluluk/boşluk durumlarını takip etmek, güvenlik ve operasyon birimleri arasında gerçek zamanlı veri senkronizasyonu sağlamak amacıyla geliştirilmiş web tabanlı akıllı otopark otomasyonudur.

---

## 📌 Proje Hakkında ve Gereksinimler

Sahadaki tır ve binek şirket araçlarının giriş-çıkışlarında yaşanan park yeri belirsizliğini gidermek için tasarlanan bu yazılım, **Python** ve **Streamlit** kütüphanesi kullanılarak geliştirilmiştir.

### ✨ Öne Çıkan Özellikler

* **Dinamik Kapasite Yönetimi:** Tır ve Otomobil park kapasitelerinin kenar çubuğu (Sidebar) üzerinden anlık olarak ayarlanabilmesi.
* **Görsel Dashboard ve Renk Kodlaması:**
  * 🟢 **Boş Slotlar:** Yeşil
  * 🔴 **Dolu Slotlar:** Kırmızı
  * 🟡 **Bakımda / Rezerve Slotlar:** Sarı
* **Real-Time Metrik Paneli:** Toplam park alanı, dolu tır sayısı, boş otomobil kapasitesi ve bakımdaki slotların anlık gösterimi.
* **🚨 Otomatik Alarm Mekanizması:** Tır park alanı tam doluluğa ulaştığında güvenlik personeline görsel uyarı ekranı.
* **JSON Veri Senkronizasyonu:** `st.session_state` mimarisi ve JSON veritabanı ile verilerin anında yerel ortama kaydedilmesi.
* **📊 Hareket ve Denetim Logları:** Araç giriş-çıkış ve durum güncellemelerinin zaman damgalı olarak CSV dosyasında saklanması.
* **Çoklu Cihaz ve Yerel Ağ Desteği:** Güvenlik kulübesi ve operasyon merkezinden eş zamanlı erişim (1 saniyenin altında tepki süresi).

---

## 📁 Proje Dosya Yapısı

smart_park/
│
├── app.py                # Streamlit ana uygulama ve arayüz kodu
├── otopark_verisi.json   # Anlık slot durumlarının saklandığı JSON veritabanı
├── otopark_loglari.csv   # Araç hareket ve işlem geçmişi log dosyası
├── requirements.txt      # Gerekli Python paketleri listesi
└── README.md             # Proje dokümantasyonu

## 🚀 Linux Ortamında Kurulum ve Çalıştırma

Aşağıdaki adımları Linux terminalinizde sırasıyla çalıştırarak projeyi kurabilir ve yayına alabilirsiniz:

### 1. Proje Dizinini Oluşturma ve Hazırlık

# Proje klasörünü oluşturun ve içine girin
mkdir -p smart_park && cd smart_park

### 2. Python Sanal Ortamını (venv) Kurma
# Sanal ortamı oluşturun
python3 -m venv venv

# Sanal ortamı aktif edin
source venv/bin/activate

### 3. Bağımlılıkların Yüklenmesi

requirements.txt dosyasını oluşturun veya doğrudan yükleyin:

pip install --upgrade pip
pip install streamlit pandas

## 📡 Canlı Ortamda (Yerel Ağda) Yayına Alma

Uygulamanın güvenlik kulübesi ve Toroslar lojistik yönetim birimindeki diğer bilgisayar/tabletlerden erişilebilir olması için IP dinleme modunda başlatılması gerekir:

streamlit run app.py --server.port 8501 --server.address 0.0.0.0




Akıllı

Otopark Analizi





Bakiler Lojistik A.Ş.'nin Akdeniz nakliyat iş merkezinde tırların

ve binek şirket araçlarının giriş-çıkışlarında yaşanan

park yeri belirsizliğini gidermek amacıyla akıllı bir otopark

takip sistemi projelendirme kararı aldık. sahadaki otopark

alanlarının anlık doluluk/boşluk durumunun hem güvenlik hem de

operasyon birimi tarafından izlenebilmesi ihtiyacı vurgulandı.

Projenin Python dilinde hızlı ve web tabanlı bir arayüz sunanStreamlit kütüphanesi ile geliştirilmesi kararlaştırıldı.

Tır ve otomobil park alanlarının ayrı kategorilerde yönetilmesi,

toplam park yeri sayısının dinamik ayarlanması ve her slotun

durumu (Dolu, Boş, Bakımda) için görsel bir dashboard kurgusu

hazırlandı. Günün kalanında projenin teknik gereksinim analizi

tamamlandı.






Otopark

Veri Mimarisi





Streamlit tabanlı otopark takip uygulamasının veri yapısını ve

arka plan (Back-End) mantığını geliştirmeye başladım. Tunç

Bey’in rehberliğinde uygulamanın anlık durum verisini saklamak

için Python JSON veri yapısı ve

Streamlit’in oturum durumu (st.session_state)

mekanizması kullanıldı. Park alanları için iki ana kategori

tanımlandı: Tır Park Alanı ve Otomobil Park Alanı.

Kullanıcının kenar çubuğu (sidebar) üzerinden dinamik olarak

park alanı kapasitesini (örn. 20 Tır, 15 Otomobil)

belirleyebileceği bir yapı kurgulandı. Her bir park slotu için

slot numarası, araç türü, park durumu (Boş,Dolu, Bakımda/Rezerve),

plakası ve son güncelleme zamanı bilgilerini tutan veri sözlükleri

(dictionary) tasarlandı. İlk test verileriyle uygulamanın veri

işleme mantığı doğrulandı.






Streamlit

Arayüz Tasarımı





Otopark Takip Otomasyonunun kullanıcı arayüzünü (Dashboard)

Streamlit bileşenleri kullanarak tasarladım. Ekranın üst kısmında

toplam park alanı, dolu tır sayısı, boş otomobil yeri ve bakımda

olan slotları anlık gösteren özet metrik kartları (st.metric)

konumlandırdım. Park slotlarını görselleştirmek için

Streamlit’in sütun düzenini (st.columns)

kullandım. Park slotlarının durumuna göre dinamik renk kodlaması

uyguladım: Boş slotlar yeşil (🟢), Dolu slotlar kırmızı (🔴)

ve Bakımdaki slotlar sarı (🟡) simgelerle görselleştirildi.

Kullanıcıların tır ve otomobil sekmeleri (st.tabs)

arasında kolayca geçiş yapabileceği responsive bir layout

oluşturuldu. Arayüz tasarımı tamamlandıktan sonra Sabahat

Hanım’a ön izleme sunumu yapıldı.




Otopark

Yazılım Testi





Geliştirilen Streamlit otopark takip sisteminin Akdeniz nakliyat

merkezindeki güvenlik kulübesi ve Toroslar lojistik yönetim

biriminde canlı ortam testlerini gerçekleştirdim. Uygulama yerel

ağda (Local Network) yayınlanarak (streamlit

run app.py --server.port 8501) birden fazla cihazdan aynı

anda erişim denemeleri yapıldı. Saha güvenlik personeli ile

birlikte 30 tır ve 15 otomobil verisiyle simülasyon yapıldı; park

durum güncellemelerinin 1 saniyenin altında ekrana yansıdığı

doğrulandı. Testler sırasında tespit edilen ufak arayüz hizalama

hataları ve veri sıfırlama butonundaki mantık hatası giderildi.

Yazılım, Akdeniz şubesindeki saha operasyon personelinin

kullanımına sunuldu.



Park

Durum Kodlaması





Dashboard üzerindeki etkileşimli kontrol fonksiyonlarını

kodladım. Güvenlik veya saha personelinin bir park slotuna

tıkladığında araç plakası girebileceği, durumu "Dolu",

"Boş" veya "Bakımda" olarak değiştirebileceği

açılır form pencereleri (st.form vest.selectbox) entegre ettim. Tunç Bey

ile birlikte durum değişikliklerinin anında veritabanına ve JSON

dosyasına kaydedilmesini sağlayan veritabanı senkronizasyon

fonksiyonlarını yazdık. Tır alanı dolduğunda güvenlik

personeline "Tır Otoparkı Dolu!" uyarısı veren görsel

alarm mekanizması eklendi. Ayrıca araç giriş-çıkış saatlerini

kaydeden loglama sistemi kodlanarak saha operasyonlarının geçmişe

dönük izlenebilirliği sağlandı.


⚙️ Sistem Kullanım Kılavuzu

linuxte bunu kodlayalım

Bu projenin tüm teknik isterlerini karşılayan, Linux ortamında sorunsuz çalışacak production-grade bir Python ve Streamlit uygulaması hazırladım.

Projede JSON veritabanı senkronizasyonu, st.session_state mimarisi, loglama altyapısı, dinamik renk kodlaması (🟢/🔴/🟡), anlık metrikler, form bazlı park slot güncellemeleri ve doluluk alarm uyarıları tam olarak entegre edilmiştir.
Proje Kurulumu ve Çalıştırma (Linux Terminal)

📡 Canlı Ortamda (Yerel Ağda) Yayına Alma

Uygulamanın güvenlik kulübesi ve Toroslar lojistik yönetim birimindeki diğer bilgisayar/tabletlerden erişilebilir olması için IP dinleme modunda başlatılması gerekir:
Bash

streamlit run app.py --server.port 8501 --server.address 0.0.0.0

🌐 Erişim Adresleri

    Yerel Sunucu (Local): http://localhost:8501

    Yerel Ağ (LAN Access): http://<LINUX_SUNUCU_IP_ADRESI>:8501

    İpucu: Sunucunuzun IP adresini öğrenmek için Linux terminalinde hostname -I veya ip a komutunu kullanabilirsiniz.

⚙️ Sistem Kullanım Kılavuzu

    Kapasite Ayarlama: Sol taraftaki menüden (Sidebar) güncel Tır ve Otomobil kapasitesini belirleyin.

    Durum Güncelleme:

        İlgili parka ait slot kartının altındaki "Düzenle" butonuna tıklayın.

        Durumu (Boş, Dolu, Bakımda/Rezerve) seçin.

        Araç Dolu ise plaka bilgisini girin ve "Kaydet ve Senkronize Et" butonuna basın.

    Log Takibi: "📋 Hareket Logları" sekmesinden geçmişe dönük tüm araç giriş-çıkış ve durum güncellemelerini inceleyebilirsiniz.

    Sistemi Sıfırlama: Sol menüdeki "Tüm Sistem Verilerini Sıfırla" butonu ile tüm slotları tek tıkla varsayılan "Boş" durumuna getirebilirsiniz.

🛠️ Teknik Özellikler ve Mimari

    Arayüz Framework: Streamlit

    Veri İşleme & Loglama: Pandas

    Veri Depolama Formatı: JSON (Aktif Durum) & CSV (Tarihçe Logları)

    Tepki Süresi: < 1000ms (Ağ içi senkronizasyon)

📄 Lisans

Bu proje Bakiler Lojistik A.Ş. bünyesinde Akdeniz Nakliyat İş Merkezi saha operasyonları için özel olarak tasarlanmıştır. Tüm hakları saklıdır.
"""

with open("README.md", "w", encoding="utf-8") as f:
f.write(readme_content)

print("README.md başarıyla oluşturuldu.")


```text?code_stdout&code_event_index=1
README.md başarıyla oluşturuldu.

Your README.md file is ready
MD icon
README
 MD 

Bakiler Lojistik A.Ş. Akıllı Otopark Takip Sistemi projesi için hazırlanan README.md dosyasının içeriği aşağıda verilmiştir. Proje dizininizde (smart_park/README.md) kullanabilirsiniz.
Markdown

# 🚛 Bakiler Lojistik A.Ş. - Akıllı Otopark Takip Sistemi

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?style=for-the-badge&logo=streamlit)
![OS](https://img.shields.io/badge/OS-Linux%20%2F%20Ubuntu-FCC624?style=for-the-badge&logo=linux)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Bakiler Lojistik A.Ş. Akdeniz Nakliyat İş Merkezi sahasındaki tır ve otomobil park alanlarının anlık doluluk/boşluk durumlarını takip etmek, güvenlik ve operasyon birimleri arasında gerçek zamanlı veri senkronizasyonu sağlamak amacıyla geliştirilmiş web tabanlı akıllı otopark otomasyonudur.

---

## 📌 Proje Hakkında ve Gereksinimler

Sahadaki tır ve binek şirket araçlarının giriş-çıkışlarında yaşanan park yeri belirsizliğini gidermek için tasarlanan bu yazılım, **Python** ve **Streamlit** kütüphanesi kullanılarak geliştirilmiştir.

### ✨ Öne Çıkan Özellikler

* **Dinamik Kapasite Yönetimi:** Tır ve Otomobil park kapasitelerinin kenar çubuğu (Sidebar) üzerinden anlık olarak ayarlanabilmesi.
* **Görsel Dashboard ve Renk Kodlaması:**
  * 🟢 **Boş Slotlar:** Yeşil
  * 🔴 **Dolu Slotlar:** Kırmızı
  * 🟡 **Bakımda / Rezerve Slotlar:** Sarı
* **Real-Time Metrik Paneli:** Toplam park alanı, dolu tır sayısı, boş otomobil kapasitesi ve bakımdaki slotların anlık gösterimi.
* **🚨 Otomatik Alarm Mekanizması:** Tır park alanı tam doluluğa ulaştığında güvenlik personeline görsel uyarı ekranı.
* **JSON Veri Senkronizasyonu:** `st.session_state` mimarisi ve JSON veritabanı ile verilerin anında yerel ortama kaydedilmesi.
* **📊 Hareket ve Denetim Logları:** Araç giriş-çıkış ve durum güncellemelerinin zaman damgalı olarak CSV dosyasında saklanması.
* **Çoklu Cihaz ve Yerel Ağ Desteği:** Güvenlik kulübesi ve operasyon merkezinden eş zamanlı erişim (1 saniyenin altında tepki süresi).

---

## 📁 Proje Dosya Yapısı

```text
smart_park/
│
├── app.py                # Streamlit ana uygulama ve arayüz kodu
├── otopark_verisi.json   # Anlık slot durumlarının saklandığı JSON veritabanı
├── otopark_loglari.csv   # Araç hareket ve işlem geçmişi log dosyası
├── requirements.txt      # Gerekli Python paketleri listesi
└── README.md             # Proje dokümantasyonu

🚀 Linux Ortamında Kurulum ve Çalıştırma

Aşağıdaki adımları Linux terminalinizde sırasıyla çalıştırarak projeyi kurabilir ve yayına alabilirsiniz:
1. Proje Dizinini Oluşturma ve Hazırlık
Bash

# Proje klasörünü oluşturun ve içine girin
mkdir -p smart_park && cd smart_park

2. Python Sanal Ortamını (venv) Kurma
Bash

# Sanal ortamı oluşturun
python3 -m venv venv

# Sanal ortamı aktif edin
source venv/bin/activate

3. Bağımlılıkların Yüklenmesi

requirements.txt dosyasını oluşturun veya doğrudan yükleyin:
Bash

pip install --upgrade pip
pip install streamlit pandas

📡 Canlı Ortamda (Yerel Ağda) Yayına Alma

Uygulamanın güvenlik kulübesi ve Toroslar lojistik yönetim birimindeki diğer bilgisayar/tabletlerden erişilebilir olması için IP dinleme modunda başlatılması gerekir:
Bash

streamlit run app.py --server.port 8501 --server.address 0.0.0.0

🌐 Erişim Adresleri

- Yerel Sunucu (Local): http://localhost:8501
- Yerel Ağ (LAN Access): http://<LINUX_SUNUCU_IP_ADRESI>:8501

İpucu: Sunucunuzun IP adresini öğrenmek için Linux terminalinde hostname -I veya ip a komutunu kullanabilirsiniz.


Kapasite Ayarlama: Sol taraftaki menüden (Sidebar) güncel Tır ve Otomobil kapasitesini belirleyin.

Durum Güncelleme:

- İlgili parka ait slot kartının altındaki "Düzenle" butonuna tıklayın.
- Durumu (Boş, Dolu, Bakımda/Rezerve) seçin.
- Araç Dolu ise plaka bilgisini girin ve "Kaydet ve Senkronize Et" butonuna basın.
- Log Takibi: "📋 Hareket Logları" sekmesinden geçmişe dönük tüm araç giriş-çıkış ve durum güncellemelerini inceleyebilirsiniz.
- Sistemi Sıfırlama: Sol menüdeki "Tüm Sistem Verilerini Sıfırla" butonu ile tüm slotları tek tıkla varsayılan "Boş" durumuna getirebilirsiniz.

🛠️ Teknik Özellikler ve Mimari

Arayüz Framework: Streamlit
Veri İşleme & Loglama: Pandas
Veri Depolama Formatı: JSON (Aktif Durum) & CSV (Tarihçe Logları)
Tepki Süresi: < 1000ms (Ağ içi senkronizasyon)
