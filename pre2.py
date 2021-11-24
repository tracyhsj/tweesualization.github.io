#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  21 09:58:10 2020

@author: tracy
"""

# import argparse
import pandas as pd
import numpy as np

# df=pd.DataFrame(0, index=range(1,73), columns=["Candidate", "Tweets"])
df = pd.read_csv("tweets_22sample.csv")

count=0
# time=0
# data=np.zeros((24, 3))
# print(data)
# df=pd.DataFrame(index=range(1,73), columns=["Time", "Candidate", "Tweets"])
# time_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# df_w["Time"]=time_list


# text = df['text']
# trump_count=0
# biden_count=0
# obama_count=0
# hillary_count=0

# print(df)
# for w in text:


for index, row in df.iterrows():
    # time+=1
    count+=1
    
    # words=i.split(' ')
    # for w in words:
    date=row['created_at']
    hour=date.split(' ')[1].split(':')[0]

    lw=row['text'].lower()
    # print(lw)
    if "trump" in lw or "donald" in lw:
        df.at[index,'created_at']="10/22: "+hour
        # df.iloc[index, df.columns.get_loc("created_at")]=hour
        df.at[index,'text']="Trump"
        # print(w)
    elif "biden" in lw or "joe" in lw:
        df.at[index,'created_at']="10/22: "+hour
        df.at[index,'text']="Biden"
    elif "obama" in lw:
        df.at[index,'created_at']="10/22: "+hour
        df.at[index,'text']="Obama"
            # print(w)
    elif "hillary" in lw:
        df.at[index,'created_at']="10/22: "+hour
        df.at[index,'text']="Hillary"
    else:
        df=df.drop(labels=index, axis=0)

    # if (count==5):
    #     break




df=df[["text","created_at"]]
# print(df[:1])
# df=df.iloc[1:, :]
df=df.groupby(["created_at", "text"]).size().reset_index(name='Tweets')
# print(type(df))

# print(df)
df=df.rename(columns={"text":"Candidate", "created_at":"Time"})
# df=df.set_axis([*df.columns[0], "Time"], axis=0, inplace=False)
# df=df.set_axis([*df.columns[1], "Candidate"], axis=0, inplace=False)

print(df)
# print(df[:5])       
 


# print(trump_count)
# print(biden_count)
# print(obama_count)
# print(hillary_count)
# rows=[pd.Series(['Trump_22', trump_count], index=df.columns), pd.Series(['Biden_22', biden_count], index=df.columns), pd.Series(['Obama_22', obama_count], index=df.columns), pd.Series(['Hillary_22', hillary_count], index=df.columns)]
# # df = df.append({"Trump22": trump_count, "Biden22": biden_count, "Obama22": obama_count ,"Hillary22": hillary_count}, ignore_index=True)
# df=df.append(rows, ignore_index=True)

# pd.set_option('display.max_columns', 10)
# print(df)


df.to_csv("prep2_tweets_22.csv", index=False)



