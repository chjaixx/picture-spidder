import numpy as np
arr1=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
arr2=np.array([0,2,3,4])
arr3=arr1*arr2
print(arr3)
print(np.sum(arr3))
print(np.count_nonzero(arr3))
print(np.mean(arr3))
print(np.sum(arr3,axis=0))
print(np.mean(arr3,axis=1))
import pandas as pd
arr=pd.read_csv("student_scores.csv",index_col='stu_id')
print(arr.count())
arr=arr.drop_duplicates()
print(arr.count())
arr['age']=arr['age'].astype(str)
arr=arr.fillna({'age':'未登记','class_id':'未登记','score':-1})
arr['gender']=arr['gender'].replace({'M':'男','f':'女'})
arr_new=pd.DataFrame([{'name':'苏沫','age':21.0,'gender':'女',
                       'class_id':'C02','subject':'Python','score':99.0,
                       'exam_date':'2026-09-03'}],index=[1024])
arr=pd.concat([arr,arr_new])
arr=arr[(arr['score']>=0) & (arr['score']<=100)]
arr['good']=np.where(arr['score']>=90,'优秀',
                     np.where(arr['score']>=70,'良好',
                              np.where(arr['score']>=60,'合格','不合格')))
print(arr.loc[(arr['good']=='优秀')&(arr['subject']=='Python')])
arr_greap=arr.groupby('class_id')
print(arr_greap['score'].mean())
arr4=pd.read_csv('class_info.csv')
res_inner=arr.merge(arr4,on='class_id',how='left')
print(res_inner.to_string())
res_inner_c2=res_inner.loc[res_inner['class_id']=='C02']
res_inner_c2.to_csv('C02_all_student_teachar.csv',encoding='utf-8',index=False)