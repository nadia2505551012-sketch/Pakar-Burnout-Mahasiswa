# =========================================================
# DESAIN ANTARMUKA STREAMLIT (app.py)
# =========================================================

import streamlit as st
from engine import proses_forward_chaining_cf, DIK_CF_USER

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="BurnoutCheck - Sistem Pakar",
    page_icon="🧠",
    layout="wide"
)

# --- 2. INISIALISASI SESSION STATE ---
# Agar status diagnosa tersimpan dan slider tidak mereset halaman
if 'sudah_diagnosa' not in st.session_state:
    st.session_state.sudah_diagnosa = False

# --- 3. CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp {
        background-color: #F4F7FE !important;
    }
    .hero-banner {
        background: #EBF3FF;
        padding: 24px;
        border-radius: 16px;
        margin-bottom: 20px;
        border: 1px solid #D0E1FD;
    }
    .stat-card {
        background-color: #FFFFFF;
        padding: 16px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.03);
    }
    .stat-number {
        color: #3C4EAD;
        font-size: 26px;
        font-weight: bold;
    }
    .result-card {
        background-color: #FFFFFF;
        padding: 24px;
        border-radius: 16px;
        border-left: 6px solid #48BB78;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.03);
    }
    </style>
""", unsafe_allow_html=True)

# Header Tanggal & User
st.markdown("<div style='text-align: right; color: #718096; font-size: 13px; font-weight: 600;'>📅 Senin, 29 September 2026 | 👤 User</div>", unsafe_allow_html=True)

col_kiri, col_kanan = st.columns([1.8, 1.2])

with col_kiri:
    # Banner Hero
    st.markdown("""
    <div class="hero-banner">
        <span style="background-color: #C3DAFE; color: #2C5282; padding: 3px 8px; border-radius: 8px; font-size: 11px; font-weight: bold;">SISTEM PAKAR</span>
        <h2 style="color: #1A202C; margin-top: 8px; margin-bottom: 6px;">Deteksi Tingkat Burnout Mahasiswa</h2>
        <p style="color: #4A5568; font-size: 13px; margin: 0;">Menggunakan metode Forward Chaining dan Certainty Factor untuk membantu mendeteksi tingkat burnout berdasarkan kondisi akademik dan emosional mahasiswa.</p>
    </div>
    """, unsafe_allow_html=True)

    # 3 Stat Cards
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown('<div class="stat-card"><div class="stat-number">8</div><div style="font-size:12px; color:#718096;"><b>Gejala</b><br>Kondisi dianalisis</div></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="stat-card"><div class="stat-number">8</div><div style="font-size:12px; color:#718096;"><b>Rule</b><br>Aturan inferensi</div></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="stat-card"><div class="stat-number">3</div><div style="font-size:12px; color:#718096;"><b>Tingkat Burnout</b><br>Ringan, Sedang, Berat</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📝 Input Gejala")
    st.caption("Pilih tingkat keyakinan Anda terhadap setiap gejala yang dirasakan.")

    options = list(DIK_CF_USER.keys())
    
    col_g_a, col_g_b = st.columns(2)
    with col_g_a:
        g1 = st.selectbox("G1 - Sering Begadang", options, index=0)
        g2 = st.selectbox("G2 - Tugas Menumpuk", options, index=0)
        g3 = st.selectbox("G3 - Sulit Berkonsentrasi", options, index=0)
        g4 = st.selectbox("G4 - Kehilangan Motivasi Belajar", options, index=0)
    with col_g_b:
        g5 = st.selectbox("G5 - Mudah Lelah", options, index=0)
        g6 = st.selectbox("G6 - Sulit Tidur", options, index=0)
        g7 = st.selectbox("G7 - Mudah Marah", options, index=0)
        g8 = st.selectbox("G8 - Menarik Diri dari Pergaulan", options, index=0)

    btn_diagnosa = st.button("🔍 Diagnosa Sekarang", use_container_width=True, type="primary")

    if btn_diagnosa:
        st.session_state.sudah_diagnosa = True

with col_kanan:
    st.markdown("### 📊 Hasil Diagnosa")
    
    if st.session_state.sudah_diagnosa:
        kategori, persentase, log, G_val = proses_forward_chaining_cf(g1, g2, g3, g4, g5, g6, g7, g8)
        
        # Result Card
        st.markdown(f"""
        <div class="result-card">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <h3 style="margin:0; color:#2D3748;">Kategori {kategori}</h3>
                <span style="background-color:#C6F6D5; color:#22543D; padding:4px 8px; border-radius:6px; font-size:11px; font-weight:bold;">Tingkat Keyakinan</span>
            </div>
            <p style="font-size:13px; color:#4A5568; margin-top:10px;">
                Berdasarkan jawaban yang diberikan, tingkat burnout Anda berada pada kategori <b>{kategori.lower()}</b> dengan tingkat keyakinan <b>{persentase:.1f}%</b>.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### ⚙️ Skor Burnout")
        st.caption("Certainty Factor Total")
        st.markdown(f"# {persentase:.1f}%")
        
        st.markdown("---")
        st.markdown("### 💡 Rekomendasi Solusi")
        if kategori == "Burnout Berat":
            st.info("• Segera ambil tindakan intensif / penanganan khusus\n• Konsultasi dengan konselor psikologi")
        elif kategori == "Burnout Sedang":
            st.warning("• Kurangi beban tugas yang tidak prioritas\n• Perbaiki pola tidur dan manajemen waktu")
        elif kategori == "Burnout Ringan":
            st.success("• Istirahat yang cukup dan teratur\n• Lakukan olahraga atau hobi ringan")
        else:
            st.info("• Pertahankan pola hidup sehat dan manajemen waktu yang baik.")

        st.markdown("---")
        
        # TAB DETAIL: LOG, BACKWARD CHAINING, CALCULATOR CF & LIMITATIONS
        tab_log, tab_backward, tab_cf, tab_limit = st.tabs(["📄 Log FC", "🌲 Backward Chaining", "🧮 Perhitungan CF", "⚠️ Keterbatasan"])
        
        with tab_log:
            st.code("\n".join(log), language="text")
            
        with tab_backward:
            st.markdown(f"**Membuktikan Hipotesis Goal:** `{kategori}`")
            dot_code = f"""
            digraph G {{
                rankdir=BT;
                node [shape=box, style="filled,rounded", fontname="sans-serif", fontsize=10];
                
                G1 [label="G1: {g1}", fillcolor="#E1F5FE"];
                G5 [label="G5: {g5}", fillcolor="#E1F5FE"];
                F1 [label="F1: Kelelahan Fisik", fillcolor="#FFF9C4"];
                
                G1 -> F1; G5 -> F1;
                
                F4 [label="F4: Burnout Awal", fillcolor="#FFE0B2"];
                F1 -> F4;
                
                Goal [label="GOAL: {kategori}", fillcolor="#C8E6C9", shape=doubleoctagon];
                F4 -> Goal;
            }}
            """
            st.graphviz_chart(dot_code)
            st.write("Sistem melakukan verifikasi terbalik dari Hipotesis Goal ke Gejala pendukung yang diinputkan pengguna.")

        with tab_cf:
            st.markdown("#### Simulasi Rumus CF (Sesuai Gambar Slide)")
            st.write("1. **Kombinasi Premis AND:** $CF(bukti) = \\min(CF_1, CF_2)$")
            st.write("2. **Kalikan Bobot Rule:** $CF(kesimpulan) = CF(bukti) \\times CF(aturan)$")
            st.write("3. **Kombinasi Dua Bukti:** $CF_{gabungan} = CF_1 + CF_2(1 - CF_1)$")
            
            st.divider()
            col_cf1, col_cf2 = st.columns(2)
            with col_cf1:
                e1 = st.slider("CF Bukti 1", 0.0, 1.0, 0.90, 0.05, key="slider_e1")
                e2 = st.slider("CF Bukti 2", 0.0, 1.0, 0.80, 0.05, key="slider_e2")
            with col_cf2:
                rule_w = st.slider("CF Aturan (Pakar)", 0.0, 1.0, 0.85, 0.05, key="slider_rule")
                
            res_min = min(e1, e2)
            res_cf = res_min * rule_w
            
            st.markdown(f"""
            * **Langkah 1:** $\\min({e1:.2f}, {e2:.2f}) = {res_min:.2f}$
            * **Langkah 2:** ${res_min:.2f} \\times {rule_w:.2f} = \\mathbf{{{res_cf:.4f}}}$ (**{res_cf*100:.1f}%**)
            """)

        with tab_limit:
            st.markdown("""
            **Batas Kesimpulan Sistem (Limitations):**
            * **Terikat Kaku pada Rule Base:** Sistem hanya dapat mengambil keputusan jika kombinasi gejala persis memenuhi syarat $AND$ pada Aturan $R1-R8$.
            * **Sifat Rantai Ketergantungan (Chaining):** Jika satu fakta antara ($F1$ atau $F2$) gagal terbentuk, proses inferensi ke tingkat berikutnya otomatis terputus.
            * **Penilaian Subjektif:** Nilai kepastian masukan pengguna ($0.2, 0.4, 0.8, 1.0$) bersifat subjektif.
            """)
    else:
        st.info("Pilih tingkat keyakinan pada setiap gejala di sebelah kiri, lalu klik **Diagnosa Sekarang**.")