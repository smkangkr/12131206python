import csv  /csv 파일 불러오기
f = open('2016년_사망교통사고.csv')
data = csv.reader(f)
result=[]    /list만들기
name = input('원하는 요일을 적어주세요: ')  
a=0
b=0
c=0
d=0
e=0
f=0
for row in data:
    if name in row[4]:   
        result.append(int(row[1][8:]))  
        
        if 0 <= int(row[1][8:]) <= 3 :    
            a += 1                                         
        elif 4 <= int(row[1][8:]) <= 7:
            b +=1                                     
        elif 8 <= int(row[1][8:]) <= 11:
            c +=1                                      
        elif 12 <= int(row[1][8:]) <= 15:
            d +=1                                     
        elif 16 <= int(row[1][8:]) <= 19:
            e +=1                                       
        elif 20 <= int(row[1][8:]) <= 23:
            f +=1                                     
    
%matplotlib inline
import matplotlib.pyplot as plt
size=[a,b,c,d,e,f]                                                        
labels='0~3','4~7','8~11','12~15','16~19','20~23'      
plt.rc('font', family = 'Malgun Gothic')
plt.title(name+'요일의 시간대별 교통사고 비율')       
plt.pie(size , labels=labels)                                     

plt.axis('equal')
plt.show()
if max(a,b,c,d,e,f)==a:
    print(name+'요일은 0~3시를 조심하세요')
elif max(a,b,c,d,e,f)==b:
    print(name+'요일은 4~7시를 조심하세요')
elif max(a,b,c,d,e,f)==c:
    print(name+'요일은 8~11시를 조심하세요')
elif max(a,b,c,d,e,f)==d:
    print(name+'요일은 12~15시를 조심하세요')
elif max(a,b,c,e,d,f)==e:
    print(name+'요일은 16~19시를 조심하세요')
elif max(a,b,c,d,e,f)==f:
    print(name+'요일은 20~24시를 조심하세요') 