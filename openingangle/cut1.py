import csv
import pandas as pd


enamelist=csv.reader(open('/home/ding/csv/Energy-selected.csv','r'))
###print(namelist)
###for stu in namelist:
###    print(stu[0])
# print(type(enamelist))
ecolumn=[column[0]for column in enamelist]
# name=str(ecolumn)
# print(type(name))
###print(ecolumn[0])
# eecolumn=str(ecolumn)
# print(ecolumn)
# print(ecolumn[0])
# summ=[ecolumn[0]]+[ecolumn[1]]
# sum1=summ+[ecolumn[2]]
# print(sum1)
# print(type(ecolumn))

tlist=csv.reader(open('/home/ding/csv/Time-selected.csv','r'))
timecolumn=[row[0]for row in tlist]
tlist1=csv.reader(open('/home/ding/csv/Time-selected.csv','r'))
t90=[row[1]for row in tlist1]
tlist2=csv.reader(open('/home/ding/csv/Time-selected.csv','r'))
trise=[row[2]for row in tlist2]
tlist3=csv.reader(open('/home/ding/csv/Time-selected.csv','r'))
tfall=[row[3]for row in tlist3]
tlist4=csv.reader(open('/home/ding/csv/Time-selected.csv','r'))
cts=[row[4]for row in tlist4]
tlist5=csv.reader(open('/home/ding/csv/Time-selected.csv','r'))
ratepk=[row[5]for row in tlist5]
tlist6=csv.reader(open('/home/ding/csv/Time-selected.csv','r'))
band=[row[6]for row in tlist6]
###print(timecolumn[1050])
#summ=ecolumn[1]+ecolumn[2]

# print(timecolumn[1])
# print(t90[1])
# print(trise[1])
# print(tfall[1])
# print(cts[1])
# print(ratepk[1])
# print(band[1])


i=1
namecut=[]
t90cut=[]
trisecut=[]
tfallcut=[]
ctscut=[]
ratepkcut=[]
bandcut=[]
for i in range(1051):
    # timelistname=list(timecolumn[i])
    if timecolumn[i] in ecolumn:
        namecut=namecut+[timecolumn[i]]
        t90cut=t90cut+[t90[i]]
        trisecut=trisecut+[trise[i]]
        tfallcut=tfallcut+[tfall[i]]
        ctscut=ctscut+[cts[i]]
        ratepkcut=ratepkcut+[ratepk[i]]
        bandcut=bandcut+[band[i]]
    i=i+1
# print(len(trisecut))
# print(type(t90cut[0]))

dataframename=pd.DataFrame(namecut)
dataframename.to_csv('/home/ding/csv/namecut.csv',sep=',')
dataframet90=pd.DataFrame(t90cut)
dataframet90.to_csv('/home/ding/csv/t90cut.csv',sep=',')
dataframetrise=pd.DataFrame(trisecut)
dataframetrise.to_csv('/home/ding/csv/trisecut.csv',sep=',')
dataframetfall=pd.DataFrame(tfallcut)
dataframetfall.to_csv('/home/ding/csv/tfallcut.csv',sep=',')
dataframects=pd.DataFrame(ctscut)
dataframects.to_csv('/home/ding/csv/ctscut.csv',sep=',')
dataframeratepk=pd.DataFrame(ratepkcut)
dataframeratepk.to_csv('/home/ding/csv/ratepkcut.csv',sep=',')
dataframeband=pd.DataFrame(bandcut)
dataframeband.to_csv('/home/ding/csv/bandcut.csv',sep=',')