def maxScore(dataDict):
    result=max(dataDict.items(),key=lambda d:d[1])
    print("最高分及科目：")
    print(result[1],result[0],sep="：")
    print("\n")
def sortedScore(dataDict):
    result=sorted(dataDict.items(),key=lambda score:score[1],reverse=True)
    print("分数降序排名及对应科目：")

    for i,key_value in enumerate(result):
        if(i==len(result)-1):
            print(key_value[1],key_value[0],sep="：",end="\n")
        else:
            print(key_value[1],key_value[0],sep="：",end="\n")

dataDict={}
print("请输入学科及对应分数：")
while True:
    s=input()
    if not s:
        break
    inputData = s.split("：")
    dataDict[inputData[0]]=float(inputData[1])
maxScore(dataDict)
sortedScore(dataDict)