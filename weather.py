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


jeju_hightwind=0;
jeju_lowwind=0;
for d in range(len(jeju_index)):
    if(data['풍속차이'].iloc[d]>0):
        jeju_hightwind = jeju_hightwind + 1;
    if(data['풍속차이'].iloc[d]<0):
        jeju_lowwind = jeju_lowwind + 1;

seogwipo_hightwind=0;
seogwipo_lowwind=0;
for e in range(len(seogwipo_index)):
    if(data['풍속차이'].iloc[e]>0):
        seogwipo_hightwind = seogwipo_hightwind + 1;
    if(data['풍속차이'].iloc[e]<0):
        seogwipo_lowwind = seogwipo_lowwind + 1;

jeju_longsun=0;
jeju_shortsun=0;
zero=0;
for f in range(len(jeju_index)):
    if(data['일조시간차이'].iloc[f]>0):
        jeju_longsun=jeju_longsun+1
    if(data['일조시간차이'].iloc[f]<0):
        jeju_shortsun=jeju_shortsun+1
    if(data['일조시간차이'].iloc[f]==0):
        zero=zero+1;

seogwipo_longsun=0;
seogwipo_shortsun=0;
for g in range(len(seogwipo_index)):
    if(data['일조시간차이'].iloc[g]>0):
        seogwipo_longsun=seogwipo_longsun+1;
    if(data['일조시간차이'].iloc[g]<0):
        seogwipo_shortsun=seogwipo_shortsun+1;
    if(data['일조시간차이'].iloc[g]==0):
        zero=zero+1;

bar_width=0.3
ypoint1=[jeju_plus,seogwipo_plus]
ypoint2=[jeju_minus,seogwipo_minus]
ypoint3=[jeju_hightwind,seogwipo_hightwind]
ypoint4=[jeju_lowwind,seogwipo_lowwind]
ypoint5=[jeju_longsun, seogwipo_longsun]
ypoint6=[jeju_shortsun, seogwipo_shortsun]
N=len(data['지역'].unique())
index = np.arange(N)

label=['제주시 기온','서귀포시 기온']
temp_bar1=plt.bar(index, ypoint1,color='b',alpha=0.7,width=0.3)
temp_bar2=plt.bar(index+bar_width,ypoint2,color='r',alpha=0.7,width=0.3)
plt.xticks(index,label,fontsize=16)
plt.legend((temp_bar1[0],temp_bar2[0]),('상승','하락'),fontsize=14)
plt.show()

label_wind=['제주시 풍속','서귀포시 풍속']
wind_bar1=plt.bar(index,ypoint3,color='b',alpha=0.7,width=0.3)
wind_bar2=plt.bar(index+bar_width,ypoint4,color='r',alpha=0.7,width=0.3)
plt.xticks(index,label_wind,fontsize=16)
plt.legend((wind_bar1[0],wind_bar2[0]),('상승','하락'),fontsize=14)
plt.show()

label_sun=['제주시 일조시간','서귀포시 일조시간']
sun_bar1=plt.bar(index,ypoint5, color='b',alpha=0.7, width=0.3)
sun_bar2=plt.bar(index+bar_width,ypoint6, color='r',alpha=0.7, width=0.3)
plt.xticks(index,label_sun,fontsize=16)
plt.legend((sun_bar1[0], sun_bar2[0]),('상승','하락'),fontsize=14)
plt.show()


plt.figure(figsize=(12,6))
sns.heatmap(data=data.corr(), annot=True, cmap='cubehelix_r')
plt.show()




# data.corr()['최저기온'].sort_values() #히트맵에서의 상관관계파악