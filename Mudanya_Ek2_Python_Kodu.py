import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Excel dosyasını okuma
df = pd.read_excel("Mudanya.xlsx")

# M² sütununu sayıya çevirme
df["M²"] = pd.to_numeric(df["M²"], errors="coerce")

# Boş/hatalı satırları temizleme
df = df.dropna()

# İlk satırları gösterme
print(df.head())

# Eksik veri kontrolü
print(df.isnull().sum())

# Toplam cami sayısı
toplam_cami = len(df)

# Toplam iç alan
toplam_alan = df["M²"].sum()

# Ortalama iç alan
ortalama_alan = df["M²"].mean()

# Ortanca değer
ortanca = df["M²"].median()

# En büyük iç alan
en_buyuk = df["M²"].max()

# En küçük iç alan
en_kucuk = df["M²"].min()

# Standart sapma
standart_sapma = df["M²"].std()

print("Toplam cami sayısı:", toplam_cami)
print("Toplam iç alan:", toplam_alan)
print("Ortalama iç alan:", ortalama_alan)
print("Ortanca:", ortanca)
print("En büyük iç alan:", en_buyuk)
print("En küçük iç alan:", en_kucuk)
print("Standart sapma:", standart_sapma)

# En büyük 10 cami
en_buyuk_10 = df.sort_values("M²", ascending=False).head(10)
print(en_buyuk_10)

# En küçük 5 cami
en_kucuk_5 = df.sort_values("M²", ascending=True).head(5)
print(en_kucuk_5)

# Grafik - İç alan karşılaştırması
plt.figure(figsize=(14,6))
plt.bar(df["İbadethane Adı"], df["M²"])

plt.xlabel("İbadethane Adı")
plt.ylabel("İç Alan (m²)")
plt.title("Mudanya İbadethaneleri İç Alan Karşılaştırması")

plt.xticks(rotation=90)

plt.tight_layout()
plt.show()

# İç alan sınıflandırması
kosullar = [
    (df["M²"] <= 200),
    (df["M²"] > 200) & (df["M²"] <= 500),
    (df["M²"] > 500) & (df["M²"] <= 750),
    (df["M²"] > 750)
]

siniflar = [
    "Küçük Ölçekli",
    "Orta Ölçekli",
    "Büyük Ölçekli",
    "Çok Büyük Ölçekli"
]

df["Sinif"] = np.select(kosullar, siniflar)

# Sınıflandırma sonuçları
sinif_analizi = df.groupby("Sinif")["M²"].agg(["count", "sum", "mean"])

print(sinif_analizi)

# Regresyon analizi için örnek veri
df["Cami_No"] = range(1, len(df)+1)

X = df[["Cami_No"]]
y = df["M²"]

# Model oluşturma
model = LinearRegression()
model.fit(X, y)

print("Sabit Terim:", model.intercept_)
print("Katsayı:", model.coef_[0])

# Tahmin
tahmin = model.predict(X)

# Regresyon grafiği
plt.figure(figsize=(10,6))

plt.scatter(X, y)
plt.plot(X, tahmin)

plt.xlabel("Cami Sırası")
plt.ylabel("İç Alan (m²)")
plt.title("Mudanya İbadethaneleri Regresyon Analizi")

plt.show()

# İş yükü hesabı
ekip_sayisi = 5
ekip_kapasitesi = 1500

gunluk_toplam_kapasite = ekip_sayisi * ekip_kapasitesi

print("Günlük toplam kapasite:", gunluk_toplam_kapasite)

# Teorik bitiş süresi
teorik_sure = toplam_alan / gunluk_toplam_kapasite

print("Teorik bitiş süresi:", teorik_sure)

# Gerçek süre varsayımı
gercek_sure = teorik_sure + 2.4

print("Gerçek süre:", gercek_sure)

# Gecikme nedenleri
nedenler = [
    "Elektrik kesintileri",
    "Camilerin ekstra kirli olması",
    "Yanlış rota planlaması",
    "Ulaşım süresinin uzaması",
    "Personel beklemeleri"
]

print("Gecikme nedenleri:")
for neden in nedenler:
    print("-", neden)
