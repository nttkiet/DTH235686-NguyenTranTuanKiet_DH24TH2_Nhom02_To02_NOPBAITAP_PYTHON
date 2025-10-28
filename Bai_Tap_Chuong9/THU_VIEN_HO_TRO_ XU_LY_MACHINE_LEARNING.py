# -*- coding: utf-8 -*-
# HỒI QUY TUYẾN TÍNH DỰ ĐOÁN CÂN NẶNG DỰA TRÊN CHIỀU CAO
from sklearn import linear_model
import numpy as np

# ======================
# DỮ LIỆU HUẤN LUYỆN
# ======================
# Chiều cao (cm)
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# Cân nặng (kg)
y = np.array([49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])

# ======================
# XÂY DỰNG MÔ HÌNH HỒI QUY
# ======================
regr = linear_model.LinearRegression()
regr.fit(X, y)

# ======================
# HIỂN THỊ KẾT QUẢ HỒI QUY
# ======================
print("Hệ số w1 (hệ số góc):", regr.coef_[0])
print("Hệ số w0 (hệ số chặn):", regr.intercept_)

# ======================
# NHẬP DỮ LIỆU NGƯỜI DÙNG
# ======================
yourHeight = float(input("Nhập chiều cao của bạn (cm): "))
yourWeight = regr.predict([[yourHeight]])

# ======================
# KẾT QUẢ DỰ ĐOÁN
# ======================
print("Chiều cao của bạn là:", yourHeight, "cm")
print("=> Dự đoán cân nặng là:", round(float(yourWeight[0]), 2), "kg")
