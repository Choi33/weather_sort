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

sns.relplot(data=data, x="날짜", y="최저기온", hue="지역", kind="line")
plt.xlabel('날짜')
plt.ylabel('최저기온')
plt.title('수능날 기온',fontsize=15)
plt.show()



# data.corr()['최저기온'].sort_values() #히트맵에서의 상관관계파악