import streamlit as st
import pandas as pd
from data.istanbul_data import get_istanbul_coordinates
from core.matrix_utils import create_distance_matrix
from core.ant_algorithm import AntColonyOptimization
from visual.plotting import plot_convergence, plot_route_on_map
from streamlit_folium import st_folium

# Sayfa Ayarları
st.set_page_config(page_title="ACO Rota Optimizasyonu", layout="wide")

st.title("🐜 Karınca Kolonisi ile Rota Optimizasyonu")


st.sidebar.markdown("---")
st.sidebar.header("🛠 Algoritma Parametreleri")

col_ants = st.sidebar.slider("Karınca Sayısı", 5, 100, 30)
col_iter = st.sidebar.slider("İterasyon Sayısı", 10, 500, 50)
st.sidebar.markdown("---")
alpha = st.sidebar.slider("Alpha (Feromon)", 0.1, 5.0, 1.0)
beta = st.sidebar.slider("Beta (Mesafe)", 0.1, 5.0, 3.0) # İstanbul trafiği için mesafeye daha çok önem verdik
rho = st.sidebar.slider("Buharlaşma Oranı", 0.01, 0.99, 0.1)

locations = get_istanbul_coordinates()
st.info("İstanbul Senaryosu Seçildi: 15 Tarihi Mekan")

city_names = list(locations.keys())

# Mesafeleri Hesapla
with st.spinner('Mesafe matrisi hesaplanıyor...'):
    distance_matrix, _ = create_distance_matrix(locations)

# Şehirleri/Mekanları Listele (Expander içinde gizli olsun yer kaplamasın)
with st.expander("📍 Lokasyon Listesini ve Koordinatları Göster"):
    df_loc = pd.DataFrame.from_dict(locations, orient='index', columns=['Lat', 'Lon'])
    st.dataframe(df_loc)

# --- Çalıştırma Butonu ---
if st.button("🚀 En Kısa Rotayı Bul"):
    
    aco = AntColonyOptimization(
        distances=distance_matrix,
        n_ants=col_ants,
        n_iterations=col_iter,
        alpha=alpha,
        beta=beta,
        evaporation_rate=rho
    )
    
    with st.spinner('Karıncalar en kısa yolu arıyor...'):
        best_route_indices, best_distance, history = aco.run()
    
    # --- Sonuçları Göster ---
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.success(f"🏁 Toplam Mesafe: **{best_distance:.2f} km**")
        
        st.subheader("📋 Optimize Edilmiş Sıralama:")
        # Daha şık bir liste görünümü
        for i, idx in enumerate(best_route_indices):
            st.write(f"{i+1}. {city_names[idx]}")
        
        # Yakınsama Grafiği
        st.subheader("📈 İyileşme Grafiği")
        fig_conv = plot_convergence(history)
        st.pyplot(fig_conv)

    with col2:
        st.subheader("🗺️ Rota Haritası")
        map_obj = plot_route_on_map(best_route_indices, locations, city_names)
        st_folium(map_obj, width=800, height=600)