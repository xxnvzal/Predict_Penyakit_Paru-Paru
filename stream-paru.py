import pickle
import streamlit as st

#membaca model
loaded_model = pickle.load(open("paru_model.sav", "rb"))

#judul web
st.title('Data Mining Prediksi Penyakit Paru')

# Memisahkan kolom
col1, col2 = st.columns(2)

with col1:
    Usia = st.text_input('Masukkan Usia (Contoh: Tua: 0, Muda: 1)')

with col2:

    Jenis_Kelamin = st.text_input('Masukkan Jenis Kelamin (Contoh: Pria: 0, Wanita: 1)')

with col1:

    Merokok = st.text_input('Riwayat Merokok (Contoh: Aktif: 0, Pasif: 1)')

with col2:

    Bekerja = st.text_input('Keseringan Bekerja (Contoh: Tidak: 0, Ya: 1)')

with col1:

    Rumah_Tangga = st.text_input('Berumah Tangga (Contoh: Tidak: 0, Ya: 1)')

with col2:

    Aktivitas_Begadang = st.text_input('Aktivitas Begadang (Contoh: Tidak: 0, Ya: 1)')

with col1:

    Aktivitas_Olahraga = st.text_input('Aktivitas Olahraga (Contoh: Jarang: 0, Sering: 1)')

with col2:

    Asuransi = st.text_input('Asuransi (Contoh: Ada: 0, Tidak: 1)')

with col1:

    Penyakit_Bawaan = st.text_input('Penyakit Bawaan (Contoh: Ada: 0, Tidak: 1)')

# Code untuk prediksi
paru_diagnosis = ''

# Membuat tombol untuk prediksi
if st.button('Prediksi'):
    paru_diagnosis = loaded_model.predict([[Usia, Jenis_Kelamin, Merokok, Bekerja, Rumah_Tangga, Aktivitas_Begadang, Aktivitas_Olahraga, Asuransi, Penyakit_Bawaan]])

    if paru_diagnosis == 1:
        paru_diagnosis = 'Pasien Terjangkit Penyakit Paru-Paru'
    else:
        paru_diagnosis = 'Pasien Tidak Terjangkit Penyakit Paru-Paru'

    st.success(paru_diagnosis)
