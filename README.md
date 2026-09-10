## 🚛 Lojistik – Akıllı Otopark Takip Sistemi

![ornek](ornek.png)


Lojistik için geliştirilmiş, Streamlit tabanlı Akıllı Otopark Takip ve Analiz Sistemi.

Uygulama üzerinden tır ve otomobil park alanlarının kapasitesi takip edilebilir, park yerlerinin durumu değiştirilebilir, araç plakaları kaydedilebilir ve yapılan işlemler hareket loglarına aktarılabilir.

## 📌 Özellikler
- 🚛 Tır park alanlarının takibi
- 🚗 Otomobil park alanlarının takibi
- 🟢 Boş / 🔴 Dolu / 🟡 Bakımda-Rezerve durumları
- 🪪 Araç plakası kaydetme
- 📊 Anlık otopark istatistikleri
- 🚨 Tır otoparkı tamamen dolduğunda alarm
- ⚙️ Dinamik park kapasitesi belirleme
- 📋 Araç giriş/çıkış ve durum değişikliği logları
- 💾 JSON dosyasında kalıcı veri saklama
- 📑 CSV formatında işlem geçmişi
- 🖥️ Linux üzerinde çalıştırılabilir
- 🌐 Web tarayıcısı üzerinden kullanılabilir
- 🏗️ Proje Yapısı

otopark_verisi.json ve otopark_loglari.csv uygulama ilk çalıştırıldığında otomatik olarak oluşturulabilir. Başlangıçta bu dosyaların bulunması zorunlu değildir.

## 💻 Sistem Gereksinimleri

Linux üzerinde aşağıdaki yazılımların bulunması önerilir:

Python 3.9 veya üzeri
pip
Python virtual environment (venv)
Modern bir web tarayıcısı

Ubuntu / Debian tabanlı sistemlerde:
```
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

Python sürümünü kontrol etmek için:
```
python3 --version
```

Örnek:
```
Python 3.12.3
```
## 🚀 Kurulum
### 1. Projeyi bilgisayara alın

Proje klasörünü oluşturun:
```
mkdir -p ~/lojistik-otopark
cd ~/lojistik-otopark
```

Eğer proje Git üzerinden alınacaksa:
```
git clone <PROJE_GIT_ADRESI>
cd <PROJE_KLASORU>
```
### 2. Python sanal ortamı oluşturun

Linux üzerinde önerilen yöntem:
```
python3 -m venv venv
```

Sanal ortamı aktif edin:
```
source venv/bin/activate
```

Başarılı olduğunda terminal satırının başında genellikle şu şekilde görünür:
```
(venv) user@server:~/lojistik-otopark$
```
### 3. Bağımlılıkları yükleyin

requirements.txt dosyası oluşturun:
```
streamlit
pandas
```

Daha sonra:
```
pip install -r requirements.txt
```

İsterseniz doğrudan da yükleyebilirsiniz:
```
pip install streamlit pandas
```

Kurulumları kontrol etmek için:
```
pip list
```
## ▶️ Uygulamayı Çalıştırma

Proje klasöründeyken:
```
streamlit run app.py
```

Streamlit uygulaması varsayılan olarak:
```
http://localhost:8501
```

adresinde çalışır.

Linux sunucusuna uzaktan bağlanıyorsanız uygulamayı ağ üzerinden erişilebilir hale getirmek için:
```
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

Ardından başka bir bilgisayardan:
```
http://SUNUCU_IP_ADRESI:8501
```

adresine erişebilirsiniz.

Örneğin:
```
http://192.168.1.100:8501
```
## ⚙️ Kapasite Ayarları

Uygulamanın sol tarafındaki Kapasite Ayarları bölümünden:
```
Tır park kapasitesi
Otomobil park kapasitesi
```
belirlenebilir.

Örneğin:
```
Tır Park Kapasitesi:       20
Otomobil Park Kapasitesi:  15
```

Bu durumda sistem:
```
TIR-01
TIR-02
...
TIR-20
```

ve
```
OTO-01
OTO-02
...
OTO-15
```

slotlarını oluşturur.

Kapasite artırıldığında yeni slotlar otomatik olarak eklenir.

Kapasite azaltıldığında ilgili slotlar sistemden kaldırılır.

Önemli: Kapasite azaltılırken kaldırılacak slotlarda kayıtlı araç bulunup bulunmadığına dikkat edilmelidir. Üretim ortamında kapasite azaltma işlemi öncesinde yedek alınması önerilir.

## 🚛 Tır Park Alanı

🚛 Tır Park Alanı sekmesinden tüm tır park yerleri görüntülenebilir.

Her slot üç farklı durumda olabilir:

Durum	Açıklama
🟢 Boş	Park yeri kullanılabilir
🔴 Dolu	Park yerinde araç bulunmaktadır
🟡 Bakımda/Rezerve	Park yeri geçici olarak kullanılamaz

Bir slotun durumunu değiştirmek için:
```
Düzenle TIR-01
```

butonuna tıklanır.

Ardından:

Durum seçilir.
Araç plakası girilir.
Kaydet ve Senkronize Et butonuna basılır.

Araç dolu olarak işaretlenirse plaka otomatik olarak büyük harfe çevrilir.

Örneğin:
```
33 abc 123
```

şu şekilde kaydedilir:
```
33 ABC 123
```

## 🚗 Otomobil Park Alanı

🚗 Otomobil Park Alanı sekmesinde otomobil park alanları görüntülenir.

Tır alanında olduğu gibi her otomobil slotu:

Boş
Dolu
Bakımda/Rezerve

durumlarından birine sahip olabilir.

Araç plakası yalnızca slot Dolu olarak işaretlendiğinde kaydedilir.

## 📊 Dashboard

Ana ekranda aşağıdaki bilgiler gösterilir:

### Toplam Park Yeri

Sistemde bulunan toplam tır + otomobil park yeri sayısını gösterir.

### Dolu Tır Sayısı

Anlık olarak dolu olan tır park yerlerinin sayısını gösterir.

Ayrıca tır park alanındaki doluluk oranını gösteren yüzde değeri bulunur.

### Boş Otomobil Yeri

Kullanılabilir durumdaki otomobil park yerlerinin sayısını gösterir.

### Bakımdaki Slotlar

Bakımda/Rezerve durumundaki toplam park yeri sayısını gösterir.

## 🚨 Doluluk Alarmı

Tır park alanındaki tüm slotlar dolduğunda sistem otomatik olarak uyarı gösterir.

Örneğin:

⚠️ ALARM: Tır Otoparkı Tamamen Dolu!
Güvenlik Personelinin Yeni Tır Girişlerini Durdurması Gerekmektedir.


Bu özellik saha operasyonlarında kapasite aşımının önüne geçmek amacıyla kullanılabilir.

## 📋 Hareket Logları

📋 Hareket Logları sekmesinden yapılan durum değişiklikleri görüntülenebilir.

Her işlem aşağıdaki bilgileri içerir:
```
timestamp
action
slot_id
category
plate
old_status
new_status
```

Örnek kayıt:
```
2026-09-10 11:30:15,
GÜNCELLEME,
TIR-05,
Tır,
33ABC123,
Boş,
Dolu
```


Log dosyası:
```
otopark_loglari.csv
```

olarak saklanır.

## 💾 Veri Saklama

Uygulama iki farklı dosya kullanır.

otopark_verisi.json

Otoparkın mevcut durumunu saklar.

Örneğin:
```
{
    "Tır": {
        "TIR-01": {
            "slot_id": "TIR-01",
            "category": "Tır",
            "status": "Dolu",
            "plate": "33ABC123",
            "last_updated": "2026-09-10 11:30:15"
        }
    },
    "Otomobil": {}
}
```

Uygulama kapatılıp tekrar açıldığında mevcut durum bu dosyadan yüklenir.
```
otopark_loglari.csv
```
Sistemde yapılan işlemlerin geçmişini tutar.

Bu dosya Excel, LibreOffice Calc veya Python/Pandas ile açılabilir.

Örneğin:
```
timestamp,action,slot_id,category,plate,old_status,new_status
2026-09-10 11:30:15,GÜNCELLEME,TIR-01,Tır,33ABC123,Boş,Dolu
```
## 🛠️ Önerilen Üretim Ortamı

Kurumsal kullanımda uygulamanın doğrudan Streamlit portundan internete açılması yerine aşağıdaki yapı önerilir:
```
Kullanıcı
    │
    ▼
Nginx / Reverse Proxy
    │
    ▼
Streamlit
    │
    ├── otopark_verisi.json
    │
    └── otopark_loglari.csv
```

Ek olarak:

- HTTPS kullanılmalı
- Linux kullanıcı izinleri sınırlandırılmalı
- JSON ve CSV dosyaları düzenli olarak yedeklenmeli
- Uygulama systemd servisi olarak çalıştırılabilir
- Kurum dışı erişim gerekiyorsa VPN veya güvenli erişim katmanı kullanılmalı

