import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Fungsi untuk memperbaiki format tanggal
def fix_date_format(date):
    try:
        return pd.to_datetime(date, format='%Y-%m-%d', errors='raise')
    except:
        return pd.to_datetime(date, format='%d/%m/%Y', errors='coerce')

# Membaca data dari file CSV
file_path = 'main_data.csv'  # Ganti dengan path file Anda
all_data_df = pd.read_csv(file_path)

# Memperbaiki format tanggal
all_data_df['order_estimated_delivery_date'] = all_data_df['order_estimated_delivery_date'].apply(fix_date_format)

# Judul Utama
st.title("E-Commerce Public Dataset")
st.markdown("## Dashboard Analisis Data - Dicoding")

# Tab 1: Dashboard Analisis Data
def dashboard_tab():
    # Tentukan tanggal akhir sebagai acuan (misal: 31 oktober 2018)
    end_date = pd.Timestamp('2018-10-31')

    # Filter data untuk 3 bulan sebelumnya (agustus, september, oktober)
    start_date = end_date - pd.DateOffset(months=3)
    filtered_data = all_data_df[(all_data_df['order_estimated_delivery_date'] >= start_date) & 
                                (all_data_df['order_estimated_delivery_date'] <= end_date)]


    # Bagian 1: Jumlah Order Status
    st.header("Jumlah Order Status pada 3 Bulan Terakhir")
    order_status_count = filtered_data['order_status'].value_counts()
    fig, ax = plt.subplots(figsize=(12, 6))
    order_status_count.plot(kind='barh', color='lightcoral', ax=ax)
    ax.set_title('Jumlah Order Status pada 3 Bulan Terakhir (Agustus - Oktober 2018)', fontsize=14)
    ax.set_xlabel('Jumlah', fontsize=12)
    ax.set_ylabel('Order Status', fontsize=12)
    st.pyplot(fig)

    # Bagian 2: Pengantaran Tepat Waktu vs Terlambat per Bulan
    st.header("Pengantaran Tepat Waktu vs Terlambat per Bulan")
    all_data_df['order_estimated_delivery_date'] = pd.to_datetime(all_data_df['order_estimated_delivery_date'], errors='coerce')
    all_data_df['year_month'] = all_data_df['order_estimated_delivery_date'].dt.to_period('M')
    status_counts = all_data_df.groupby(['year_month', 'delivery_status']).size().unstack(fill_value=0)
    late_counts = status_counts.get('Terlambat', pd.Series(dtype=int))
    on_time_counts = status_counts.get('Tepat Waktu', pd.Series(dtype=int))
    fig, ax = plt.subplots(1, 2, figsize=(18, 8), sharey=True)
    ax[0].barh(late_counts.index.astype(str), late_counts, color='red')
    ax[0].set_title('Pengantaran Terlambat (Semua Data)', fontsize=14)
    ax[0].set_xlabel('Jumlah', fontsize=16)
    ax[0].set_ylabel('Tahun-Bulan', fontsize=16)
    ax[0].invert_yaxis()
    ax[1].barh(on_time_counts.index.astype(str), on_time_counts, color='blue')
    ax[1].set_title('Pengantaran Tepat Waktu (Semua Data)', fontsize=16)
    ax[1].set_xlabel('Jumlah', fontsize=16)
    st.pyplot(fig)

    # Bagian 3: Persentase Pengantaran
    st.header("Persentase Pengantaran Terlambat vs Tepat Waktu")
    total_counts = all_data_df['delivery_status'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 8))
    labels = total_counts.index
    sizes = total_counts.values
    colors = ['blue', 'red']
    explode = (0.1, 0)
    wedges, texts, autotexts = ax.pie(
        sizes, 
        labels=labels, 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=colors, 
        explode=explode, 
        textprops={'fontsize': 12},
        pctdistance=0.85)
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)
    total_text = (
        f"Total Data\n{total_counts.sum()}\n\n"
        f"Terlambat: {total_counts.get('Terlambat', 0)}\n"
        f"Tepat Waktu: {total_counts.get('Tepat Waktu', 0)}"
    )
    plt.annotate(
        total_text, 
        xy=(0, 0), 
        fontsize=12, 
        ha='center', 
        va='center', 
        color='black'
    )
    plt.title('Persentase Pengantaran Terlambat vs Tepat Waktu (Keseluruhan Data)', fontsize=16)
    st.pyplot(fig)

    # Bagian 4: 10 Kategori Produk Teratas Berdasarkan Pendapatan
    st.header("10 Kategori Produk Teratas Berdasarkan Price")
    all_data_df['total_revenue'] = all_data_df['price']
    category_revenue = all_data_df.groupby('product_category_name')['total_revenue'].sum().sort_values(ascending=False)
    top_10_categories = category_revenue.head(10)
    fig, ax = plt.subplots(figsize=(12, 6))
    top_10_categories.plot(kind='barh', color='lightblue', ax=ax)
    ax.set_title('10 Kategori Produk Teratas Berdasarkan Price', fontsize=16)
    ax.set_xlabel('Total Pendapatan', fontsize=12)
    ax.set_ylabel('Kategori Produk', fontsize=12)
    st.pyplot(fig)

    # Bagian 5: Hubungan Skor Ulasan Berdasarkan Status Pengantaran
    st.header("Hubungan Skor Ulasan Berdasarkan Status Pengantaran")
    all_data_df['order_delivered_customer_date'] = pd.to_datetime(all_data_df['order_delivered_customer_date'], errors='coerce')
    all_data_df['delivery_status'] = all_data_df.apply(
        lambda row: 'Terlambat' if row['order_delivered_customer_date'] > row['order_estimated_delivery_date'] else 'Tepat Waktu',
        axis=1
    )
    filtered_data = all_data_df.dropna(subset=['review_score', 'delivery_status'])
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(
        filtered_data[filtered_data['delivery_status'] == 'Terlambat'].index,
        filtered_data[filtered_data['delivery_status'] == 'Terlambat']['review_score'],
        label='Terlambat', color='red', alpha=0.6, marker='o'
    )
    ax.scatter(
        filtered_data[filtered_data['delivery_status'] == 'Tepat Waktu'].index,
        filtered_data[filtered_data['delivery_status'] == 'Tepat Waktu']['review_score'],
        label='Tepat Waktu', color='green', alpha=0.6, marker='x'
    )
    ax.set_title('Hubungan Skor Ulasan Berdasarkan Status Pengantaran (2018)', fontsize=16)
    ax.set_xlabel('Index Dari Data', fontsize=12)
    ax.set_ylabel('Review Score', fontsize=12)
    ax.legend()
    st.pyplot(fig)

    st.caption('Copyright (c) Rasio Fernandis')

# Tab 2: Menu Filtering Data
def filter_tab():
    st.title("E-Commerce Public Dataset")
    st.markdown("## Filter Data - Dicoding")

    # Menambahkan komponen filtering di bagian atas
    st.subheader("Filter Data")
    unique_categories = all_data_df['product_category_name'].dropna().unique()
    selected_categories = st.multiselect(
        "Pilih Kategori Produk:",
        options=unique_categories,
        default=unique_categories[:5]  # Pilih 5 kategori pertama secara default
    )
    review_score_range = st.slider(
        "Pilih Rentang Skor Ulasan:",
        min_value=int(all_data_df['review_score'].min()),
        max_value=int(all_data_df['review_score'].max()),
        value=(int(all_data_df['review_score'].min()), int(all_data_df['review_score'].max()))
    )
    date_range = st.date_input(
        "Pilih Rentang Tanggal Pengantaran:",
        [all_data_df['order_estimated_delivery_date'].min(), all_data_df['order_estimated_delivery_date'].max()]
    )

    # Terapkan Filter ke Data
    filtered_data = all_data_df[
        (all_data_df['product_category_name'].isin(selected_categories)) &
        (all_data_df['review_score'].between(review_score_range[0], review_score_range[1])) &
        (all_data_df['order_estimated_delivery_date'] >= pd.Timestamp(date_range[0])) &
        (all_data_df['order_estimated_delivery_date'] <= pd.Timestamp(date_range[1]))
    ]

    st.write(f"Total Data Setelah Filter: {len(filtered_data)} baris")

    # Tampilkan Data yang Sudah Difilter
    st.write("Data yang difilter:")
    st.dataframe(filtered_data)

    # Contoh Visualisasi dari Data yang Sudah Difilter
    st.subheader("Jumlah Order Status Berdasarkan Filter")
    order_status_count = filtered_data['order_status'].value_counts()
    plt.figure(figsize=(10, 5))
    order_status_count.plot(kind='barh', color='lightgreen')
    plt.title('Jumlah Order Status Setelah Filter', fontsize=14)
    plt.xlabel('Jumlah', fontsize=12)
    plt.ylabel('Order Status', fontsize=12)
    st.pyplot(plt)

# Membuat Tab
tab1, tab2 = st.tabs(["Dashboard", "Filter Data"])

with tab1:
    dashboard_tab()

with tab2:
    filter_tab()
