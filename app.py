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
