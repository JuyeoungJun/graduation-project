import re
import csv
import pandas as pd
hangul = re.compile('[^ ㄱ-ㅣ가-힣]+') # 한글과 띄어쓰기를 제외한 모든 글자
# hangul = re.compile('[^ \u3131-\u3163\uac00-\ud7a3]+')  # 위와 동일
#result = hangul.sub('', s) # 한글과 띄어쓰기를 제외한 모든 부분을 제거

df = pd.DataFrame(columns=['Review','Total'])
f = open('./data/장안구_율전동_프랜차이즈_df.csv','r',encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    token = hangul.sub('',line[0])
    if(len(token)==0):
        continue
    df.loc[len(df)] = {
        'Review': token,
        'Total': line[1]
    }

f.close()
df.to_csv("./data/{}_{}_{}_refined_df.csv".format("장안구","율전동","프랜차이즈"),index=False,encoding="utf-8-sig")