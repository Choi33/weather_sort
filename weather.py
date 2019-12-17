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
sns.pointplot(data=data, x="날짜", y="평균기온", hue="지역")
plt.xlabel('날짜')
plt.ylabel('평균기온')
plt.title('수능날 기온',fontsize=15)
plt.show()

jeju_minus=0; #제주시 기준 수능 전 날보다 추운 날
jeju_plus=0; #제주시 기준 수능 전 날보다 따뜻한 날
for b in range(len(jeju_index)):
    if(data['온도차이'].iloc[b]>0):
        jeju_plus= jeju_plus + 1
    if(data['온도차이'].iloc[b]<0):
        jeju_minus= jeju_minus + 1

seogwipo_minus=0 #서귀포시 기준 수능 전 날보다 추운 날
seogwipo_plus=0; #서귀포시 기준 수능 전 날 보다 따뜻한 날
for c in range(len(seogwipo_index)):
    if(data['온도차이'].iloc[c]>0):
        seogwipo_plus= seogwipo_plus + 1
    if(data['온도차이'].iloc[c]<0):
        seogwipo_minus= seogwipo_minus + 1


bar_width=0.3
ypoint1=[jeju_plus,seogwipo_plus]
ypoint2=[jeju_minus,seogwipo_minus]
N=len(data['지역'].unique())
index = np.arange(N)

label=['제주시','서귀포시']
jeju_bar=plt.bar(index, ypoint1,color='b',alpha=0.5,width=0.3)
seogwipo_bar=plt.bar(index+bar_width,ypoint2,color='r',alpha=0.5,width=0.3)
plt.xticks(index,label,fontsize=16)
plt.legend((jeju_bar[0],seogwipo_bar[0]),('기온상승','기온하락'),fontsize=14)
plt.show()





# data.corr()['최저기온'].sort_values() #히트맵에서의 상관관계파악