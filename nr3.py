import numpy as np
import pandas as pd


idx = pd.date_range(start="12/24/2025", end="1/6/2026", freq="B")
# idx = pd.bdate_range(start="12/24/2025", end="1/6/2026")

print("========= a) ==========")

print(idx)

print("Es gibt " + str(idx.size) + " normale Wochentage/reguläre Arbeitstage in den Weihnachtsferien 2025/26.")


print("========= b) ==========")

idx = pd.date_range(start="12/24/2025", end="1/6/2027")

days = idx[idx.is_month_start & (idx.day_of_week == 6)]

print(days)

print("Vom 24.12.2025 bis zum 6.1.2027 gibt es " + str(days.size) + " Sonntage, die auf den 1. des Monats fallen.")
