import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore', 'This pattern has match groups')
warnings.filterwarnings('ignore', 'The iterable function was deprecated in Matplotlib')


data=pd.read_csv('weather_data.csv', encoding='cp949')

jeju_index=[]
seogwipo_index=[]
for a in range(len(data)):
    if (data['지역'].iloc[a] == '제주시'): #제주시라는 값을 가지는 index 저장
        jeju_index.append(a)
    if(data['지역'].iloc[a]=='서귀포'):  #서귀포라는 값을 가지는 index 저장
        seogwipo_index.append(a)


# matplotlib에서 한글이 깨지지 않게 해줌
mpl.rcParams['axes.unicode_minus'] = False
plt.rcParams["font.family"] = 'Malgun Gothic'
plt.rcParams["font.size"] = 12
plt.rcParams["figure.figsize"] = (14,4)
data['지역'].astype(str)

# 수능 날 기온을 그래프상에서 점을 찍어 표시
sns.relplot(data=data, x="날짜", y="최저기온", hue="지역")
plt.xlabel('날짜')
plt.ylabel('최저기온')
plt.title('수능날 기온',fontsize=15)
plt.show()

jeju_minus=0; #제주시 기준 수능 전 날보다 추운 날
jeju_plus=0; #제주시 기준 수능 전 날보다 따뜻한 날
for b in range(len(jeju_index)):
    if(data['차이'].iloc[b]>0):
        jeju_plus= jeju_plus + 1
    if(data['차이'].iloc[b]<0):
        jeju_minus= jeju_minus + 1

seogwipo_minus=0 #서귀포시 기준 수능 전 날보다 추운 날
seogwipo_plus=0; #서귀포시 기준 수능 전 날 보다 따뜻한 날
for c in range(len(seogwipo_index)):
    if(data['차이'].iloc[c]>0):
        seogwipo_plus= seogwipo_plus + 1
    if(data['차이'].iloc[c]<0):
        seogwipo_minus= seogwipo_minus + 1

'''
print("제주시를 기준으로 수능 전날 보다 기온이 높은 날은 총 ",jeju_plus,"일 이다.")
print("제주시를 기준으로 수능 전날 보다 기온이 낮은 날은 총 ",jeju_minus,"일 이다.")

print("서귀포시를 기준으로 수능 전날 보다 기온이 높은 날은 총 ",seogwipo_plus,"일 이다.")
print("서귀포시를 기준으로 수능 전날 보다 기온이 낮은 날은 총 ",seogwipo_minus,"일 이다.")
'''

# 2019년 부터 2009년까지 기온이 상승한 날의 수와 기온이 하락한 날의 수를 막대 그래프로 표현
ypoint=[jeju_minus,jeju_plus, seogwipo_minus, seogwipo_plus]
xpoint=['제주시 : 기온하락','제주시 : 기온상승', '서귀포시 : 기온하락', '서귀포시 : 기온상승']
plt.bar(xpoint,ypoint,color='green', alpha=0.7)
plt.show()



# data.corr()['최저기온'].sort_values() #히트맵에서의 상관관계파악