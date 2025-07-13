import math
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="EOQ Calculator", page_icon="📦")

# Judul Aplikasi
st.title("📦 Kalkulator Economic Order Quantity (EOQ)")
st.markdown("""
*Aplikasi ini menghitung jumlah pesanan optimal untuk meminimalkan biaya persediaan.*
""")

# Input Pengguna dengan Kolom
col1, col2, col3 = st.columns(3)
with col1:
    D = st.number_input("Permintaan Tahunan (unit)", min_value=1, value=1000)
with col2:
    S = st.number_input("Biaya Pemesanan per Pesanan (Rp)", min_value=1, value=50000)
with col3:
    H = st.number_input("Biaya Penyimpanan per Unit/Tahun (Rp)", min_value=1, value=10000)

# Hitung EOQ
def calculate_eoq(D, S, H):
    eoq = math.sqrt((2 * D * S) / H)
    total_cost = (D / eoq) * S + (eoq / 2) * H
    order_frequency = D / eoq
    return eoq, total_cost, order_frequency

if st.button("Hitung EOQ"):
    eoq, total_cost, order_frequency = calculate_eoq(D, S, H)
    
    # Tampilkan Hasil
    st.success("**Hasil Perhitungan**")
    st.metric("EOQ (Jumlah Pesanan Optimal)", f"{eoq:.2f} unit")
    st.metric("Total Biaya Persediaan Tahunan", f"Rp {total_cost:,.2f}")
    st.metric("Frekuensi Pemesanan per Tahun", f"{order_frequency:.2f} kali")
    
    # Visualisasi
    st.subheader("Analisis Sensitivitas")
    q_values = np.linspace(eoq * 0.5, eoq * 1.5, 50)
    cost_values = [(D / q) * S + (q / 2) * H for q in q_values]
    
    fig, ax = plt.subplots()
    ax.plot(q_values, cost_values, label='Total Biaya')
    ax.axvline(eoq, color='red', linestyle='--', label=f'EOQ = {eoq:.2f}')
    ax.set_xlabel('Jumlah Pesanan (Q)')
    ax.set_ylabel('Total Biaya (Rp)')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Penjelasan EOQ
with st.expander("ℹ️ Tentang EOQ"):
    st.markdown("""
    **Economic Order Quantity (EOQ)** adalah model persediaan yang menentukan jumlah pesanan optimal 
    untuk meminimalkan total biaya persediaan (biaya pemesanan + biaya penyimpanan).
    
    Rumus EOQ:
    ```
    EOQ = √((2 × D × S) / H)
    ```
    - D = Permintaan tahunan
    - S = Biaya pemesanan per pesanan
    - H = Biaya penyimpanan per unit per tahun
    """)

# Catatan Kaki
st.caption("Developed by [Nama Anda] | © 2023")
