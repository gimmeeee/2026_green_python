# %%
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

path = r'C:\Users\gimnn\OneDrive\12_공부\코딩\2026_green_python\260227\csv\서울특별시_송파구_노인요양시설_현황.csv'
df = pd.read_csv(path, encoding='cp949')

# %%
df = df.set_index('년월').T
df.index = pd.to_datetime(df.index)

df.plot(figsize=(12,6))

plt.title('월별 요양시설 현황')
plt.xlabel('년월')
plt.ylabel('개수')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
