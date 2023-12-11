import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)
print("DataFrame Awal:")
print(df)

# Menambah kolom Gaji karyawan setelah diberikan peningkatan 5%
print("\nPertanyaan 1:")
df['Gaji setelah Peningkatan'] = df['Gaji'] * 1.05

print("\nDataFrame setelah diperbarui:")
print(df)

# Menambah kolom Gaji_Sebelumnya dan Peningkatan_Gaji
print("\nPertanyaan 2:")
df['Gaji_Sebelumnya'] = df['Gaji setelah Peningkatan'] / 1.05
df['Peningkatan_Gaji'] = df['Gaji setelah Peningkatan'] - df['Gaji_Sebelumnya']

print("\nRingkasan perubahan:")
print(df[['Nama', 'Gaji_Sebelumnya', 'Gaji setelah Peningkatan', 'Peningkatan_Gaji']])

# Menambah kolom Gaji karyawan yang usianya di atas 30 tahun dan Peningkatan_Gaji_Akhir
print("\nPertanyaan 3 & 4:")
df['Gaji di atas 30 tahun'] = df.apply(lambda row: row['Gaji setelah Peningkatan'] * 1.02 if row['Usia'] > 30 else row['Gaji setelah Peningkatan'], axis=1)
df['Peningkatan_Gaji_Akhir'] = df['Gaji di atas 30 tahun'] - df['Gaji setelah Peningkatan']

print("\nGaji karyawan yang usianya di atas 30 tahun:")
print(df[['Nama', 'Usia', 'Gaji di atas 30 tahun']])

print("\nRingkasan perubahan akhir:")
print(df[['Nama', 'Usia', 'Gaji di atas 30 tahun', 'Peningkatan_Gaji_Akhir']])