# %%
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

path = r'C:\Users\gimnn\OneDrive\12_공부\코딩\2026_green_python\260227\csv\서울특별시_송파구_노인요양시설_현황.csv'
df = pd.read_csv(path, encoding='cp949')

# try:
#     df = pd.read_csv(file_path, encoding='cp949')
#     print("성공! cp949 방식으로 읽었습니다.")
# except:
#     df = pd.read_csv(file_path, encoding='utf-8')
#     print("성공! utf-8 방식으로 읽었습니다.")

print("데이터 이사 완료! 이제 위쪽 Jupyter Variables를 눌러 표를 확인하세요.")
# 판다스의 역할과 시각화의 기본인 맵프로립의 차이를 이해한다.
# %%
