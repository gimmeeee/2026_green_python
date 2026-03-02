# %%
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

import os

path = os.path.join('csv', '서울특별시_송파구_노인요양시설_현황.csv')
df = pd.read_csv(path, encoding='cp949')

# %%
fig, ax = plt.subplots(figsize=(12,6))

# 선그래프 (요양원 신고 수)
line = ax.plot(
    df.index,
    df['요양원 신고 수'],
    marker='o',
    linewidth=2,
    color='#FF8C42',
    label='요양원 신고 수'
)

# 막대그래프 (새로 지어진 시설 수)
bars = ax.bar(
    df.index,
    df['새로 지어진 시설 수'],
    width=10,
    alpha=0.6,
    color='#2F5597',
    label='새로 지어진 시설 수'
)

# 제목 및 축 설정
ax.set_title('월별 요양시설 현황')
ax.set_xlabel('년월')
ax.set_ylabel('개수')

plt.xticks(rotation=45)

# 범례 추가
ax.legend()

plt.tight_layout()
plt.show()


# %%
