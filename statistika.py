import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

# 1. Membaca dataset (Sesuaikan nama file jika berbeda di laptopmu)
file_name = "data set baru arif.xlsx - Sheet1.csv"
df = pd.read_csv(file_name)

# 2. Menentukan variabel X (bebas) dan Y (terikat) sesuai petunjuk kolom
X = df[["total_weight_gr (X1)", "Total Pembayaran (X2)"]]
Y = df["total_qty (Y)"]

# --- METODE 1: Menggunakan Statsmodels (Sangat bagus untuk Tugas Statistika) ---
# Kita perlu menambahkan konstanta (intercept) secara manual di statsmodels
X_stat = sm.add_constant(X)
model_stat = sm.OLS(Y, X_stat).fit()

print("=" * 20, "HASIL REGRESI STATISTIK", "=" * 20)
print(model_stat.summary())
print("\n" + "=" * 65 + "\n")

# --- METODE 2: Menggunakan Scikit-Learn (Untuk Prediksi & Visualisasi) ---
model_sklearn = LinearRegression()
model_sklearn.fit(X, Y)

# Mengambil nilai Intercept dan Koefisien
intercept = model_sklearn.intercept_
coef_x1, coef_x2 = model_sklearn.coef_

print("=" * 20, "PERSAMAAN REGRESI", "=" * 20)
print(f"Persamaan: Y = {intercept:.4f} + ({coef_x1:.6f})*X1 + ({coef_x2:.6f})*X2")
print("-" * 60)

# --- BONUS: Visualisasi Sederhana Hubungan Tiap Variabel ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot X1 vs Y
ax1.scatter(df["total_weight_gr (X1)"], Y, color="blue", alpha=0.5)
ax1.set_title("Total Weight (X1) vs Total Qty (Y)")
ax1.set_xlabel("Total Weight (gr)")
ax1.set_ylabel("Total Qty")

# Plot X2 vs Y
ax2.scatter(df["Total Pembayaran (X2)"], Y, color="green", alpha=0.5)
ax2.set_title("Total Pembayaran (X2) vs Total Qty (Y)")
ax2.set_xlabel("Total Pembayaran")
ax2.set_ylabel("Total Qty")

plt.tight_layout()
plt.show()