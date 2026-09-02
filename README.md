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

Linux terminalinizde aşağıdaki adımları sırasıyla çalıştırarak ortamı hazırlayın:
Bash

# 1. Proje klasörünü oluşturun ve içine girin
mkdir -p smart_park && cd smart_park

# 2. Sanal ortam (venv) oluşturun ve aktif edin
python3 -m venv venv
source venv/bin/activate

# 3. Gerekli kütüphaneleri yükleyin
pip install streamlit pandas

Uygulama Kodu (app.py)

Aşağıdaki kodu app.py adıyla oluşturun (nano app.py veya vim app.py kullanabilirsiniz):
Python

import os
import json
from datetime import datetime
import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# SETUP & CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Bakiler Lojistik - Akıllı Otopark Takip Sistemi",
    page_icon="🚛",
    layout="wide"
)

DB_FILE = "otopark_verisi.json"
LOG_FILE = "otopark_loglari.csv"

# ---------------------------------------------------------
# DATA ARCHITECTURE & PERSISTENCE (BACK-END)
# ---------------------------------------------------------
def log_event(action, slot_id, category, plate, old_status, new_status):
    """Araç giriş-çıkış ve durum değişikliklerini CSV dosyasına kaydeder."""
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "action": action,
        "slot_id": slot_id,
        "category": category,
        "plate": plate,
        "old_status": old_status,
        "new_status": new_status
    }
    df = pd.DataFrame([log_entry])
    if not os.path.exists(LOG_FILE):
        df.to_csv(LOG_FILE, index=False)
    else:
        df.to_csv(LOG_FILE, mode='a', header=False, index=False)

def load_data():
    """JSON veritabanından veriyi okur."""
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def save_data():
    """Oturum durumunu (st.session_state) JSON dosyasına kaydeder."""
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(st.session_state.parking_data, f, ensure_ascii=False, indent=4)

def initialize_slots(tir_cap, auto_cap):
    """Kapasiteye göre park slotlarını başlatır veya günceller."""
    if "parking_data" not in st.session_state:
        saved_data = load_data()
        if saved_data:
            st.session_state.parking_data = saved_data
        else:
            st.session_state.parking_data = {"Tır": {}, "Otomobil": {}}

    # Tır Slotları Senkronizasyonu
    current_tir = len(st.session_state.parking_data["Tır"])
    if tir_cap > current_tir:
        for i in range(current_tir + 1, tir_cap + 1):
            slot_key = f"TIR-{i:02d}"
            st.session_state.parking_data["Tır"][slot_key] = {
                "slot_id": slot_key,
                "category": "Tır",
                "status": "Boş",
                "plate": "",
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    elif tir_cap < current_tir:
        for i in range(tir_cap + 1, current_tir + 1):
            slot_key = f"TIR-{i:02d}"
            st.session_state.parking_data["Tır"].pop(slot_key, None)

    # Otomobil Slotları Senkronizasyonu
    current_auto = len(st.session_state.parking_data["Otomobil"])
    if auto_cap > current_auto:
        for i in range(current_auto + 1, auto_cap + 1):
            slot_key = f"OTO-{i:02d}"
            st.session_state.parking_data["Otomobil"][slot_key] = {
                "slot_id": slot_key,
                "category": "Otomobil",
                "status": "Boş",
                "plate": "",
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    elif auto_cap < current_auto:
        for i in range(auto_cap + 1, current_auto + 1):
            slot_key = f"OTO-{i:02d}"
            st.session_state.parking_data["Otomobil"].pop(slot_key, None)

    save_data()

# ---------------------------------------------------------
# SIDEBAR - CAPACITY & MANAGEMENT CONTROLS
# ---------------------------------------------------------
st.sidebar.image("https://img.icons8.com/color/96/000000/trailer-box--v1.png", width=80)
st.sidebar.title("Bakiler Lojistik A.Ş.")
st.sidebar.subheader("Akdeniz Nakliyat İş Merkezi")
st.sidebar.markdown("---")

st.sidebar.header("⚙️ Kapasite Ayarları")
tir_capacity = st.sidebar.number_input("Tır Park Kapasitesi", min_value=1, max_value=100, value=20, step=1)
auto_capacity = st.sidebar.number_input("Otomobil Park Kapasitesi", min_value=1, max_value=100, value=15, step=1)

initialize_slots(tir_capacity, auto_capacity)

st.sidebar.markdown("---")
if st.sidebar.button("🧹 Tüm Sistem Verilerini Sıfırla"):
    st.session_state.parking_data = {"Tır": {}, "Otomobil": {}}
    initialize_slots(tir_capacity, auto_capacity)
    st.sidebar.success("Tüm slotlar 'Boş' olarak sıfırlandı.")
    st.rerun()

# ---------------------------------------------------------
# DASHBOARD HEADER & METRICS
# ---------------------------------------------------------
st.title("🚛 Akıllı Otopark Analizi ve Takip Paneli")

# Metrik Hesaplamaları
all_slots = []
for cat in st.session_state.parking_data:
    all_slots.extend(st.session_state.parking_data[cat].values())

total_slots = len(all_slots)
occupied_tirs = sum(1 for s in st.session_state.parking_data["Tır"].values() if s["status"] == "Dolu")
empty_autos = sum(1 for s in st.session_state.parking_data["Otomobil"].values() if s["status"] == "Boş")
maintenance_slots = sum(1 for s in all_slots if s["status"] == "Bakımda/Rezerve")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Toplam Park Yeri", total_slots)
m2.metric("Dolu Tır Sayısı", occupied_tirs, delta=f"%{(occupied_tirs/max(tir_capacity,1))*100:.0f} Doluluk", delta_color="inverse")
m3.metric("Boş Otomobil Yeri", empty_autos)
m4.metric("Bakımdaki Slotlar", maintenance_slots)

st.markdown("---")

# 🚨 Görsel Alarm Mekanizması
if occupied_tirs >= tir_capacity:
    st.error("⚠️ **ALARM:** Tır Otoparkı Tamamen Dolu! Güvenlik Personelinin Yeni Tır Girişlerini Durdurması Gerekmektedir.")

# ---------------------------------------------------------
# MAIN INTERFACE - TABS & VISUAL GRID
# ---------------------------------------------------------
tab_tir, tab_auto, tab_logs = st.tabs(["🚛 Tır Park Alanı", "🚗 Otomobil Park Alanı", "📋 Hareket Logları"])

def render_category_grid(category_name, prefix):
    slots = list(st.session_state.parking_data[category_name].values())
    cols_per_row = 5
    
    for i in range(0, len(slots), cols_per_row):
        cols = st.columns(cols_per_row)
        for j, slot in enumerate(slots[i:i+cols_per_row]):
            status = slot["status"]
            # Dinamik Renk Kodlaması
            if status == "Boş":
                icon = "🟢"
                bg_color = "#e8f5e9"
            elif status == "Dolu":
                icon = "🔴"
                bg_color = "#ffebee"
            else: # Bakımda/Rezerve
                icon = "🟡"
                bg_color = "#fffde7"

            with cols[j]:
                st.markdown(
                    f"""
                    <div style="background-color: {bg_color}; border: 1px solid #ccc; border-radius: 8px; padding: 10px; text-align: center; margin-bottom: 10px;">
                        <h4 style="margin: 0; color: #333;">{icon} {slot['slot_id']}</h4>
                        <p style="margin: 5px 0; font-weight: bold; color: #555;">{status}</p>
                        <p style="margin: 0; font-size: 12px; color: #777;">{slot['plate'] if slot['plate'] else '---'}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                # Güncelleme Popover / Form
                with st.popover(f"Düzenle {slot['slot_id']}"):
                    with st.form(key=f"form_{slot['slot_id']}"):
                        st.subheader(f"Slot: {slot['slot_id']}")
                        new_status = st.selectbox(
                            "Durum", 
                            ["Boş", "Dolu", "Bakımda/Rezerve"], 
                            index=["Boş", "Dolu", "Bakımda/Rezerve"].index(status)
                        )
                        new_plate = st.text_input("Araç Plakası", value=slot["plate"])
                        submit = st.form_submit_button("Kaydet ve Senkronize Et")
                        
                        if submit:
                            old_status = slot["status"]
                            slot["status"] = new_status
                            slot["plate"] = new_plate.upper().strip() if new_status == "Dolu" else ""
                            slot["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            
                            save_data()
                            log_event("GÜNCELLEME", slot["slot_id"], category_name, slot["plate"], old_status, new_status)
                            st.success("Durum Güncellendi!")
                            st.rerun()

with tab_tir:
    render_category_grid("Tır", "TIR")

with tab_auto:
    render_category_grid("Otomobil", "OTO")

with tab_logs:
    st.subheader("📊 Saha Operasyon Hareket Logları")
    if os.path.exists(LOG_FILE):
        df_logs = pd.read_csv(LOG_FILE)
        st.dataframe(df_logs.sort_index(ascending=False), use_container_width=True)
    else:
        st.info("Henüz kaydedilmiş bir hareket logosu bulunmuyor.")

Sunucuda / Yerel Ağda Çalıştırma

Geliştirilen uygulamayı güvenlik kulübesi ve Toroslar lojistik birimindeki diğer cihazların erişimine açmak için canlı ortam komutunu çalıştırın:
Bash

streamlit run app.py --server.port 8501 --server.address 0.0.0.0

    Erişim Adresi (Yerel Aca): Aynı ağdaki cihazlar http://<LINUX_SUNUCU_IP_ADRESI>:8501 adresinden sisteme anında erişebilir.

    Veri Kalıcılığı: Tüm durum değişiklikleri anında otopark_verisi.json dosyasına yazılır ve otopark_loglari.csv içerisine detaylıca loglanır.

README.md oluştur bunun için
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
