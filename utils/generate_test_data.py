"""
按照指定格式生成测试数据
"""
import random
import string
import time

class GenerateTestData():
    
    #生成不同类型及制定长度的测试数据
    def genterateRandom(self, type, limitLen, element=0):
        resList = []
        resChnStr = ""
        if type == "int":
            return int("".join(map(lambda x:random.choice(string.digits), range(limitLen))))
        elif type == "str":
            return "".join(random.sample(string.ascii_letters + string.digits, limitLen))
        elif type == "list" and element > 0:
            for _ in range(limitLen):
                x = ''.join(random.sample(string.ascii_letters + string.digits, element))
                resList.append(x)
            return resList
        elif type == "chn":
            for _ in range(limitLen):
                resChnStr += chr(random.randint(0x4e00, 0x9fbf))
            return resChnStr

    #生成时间范围的随机时间戳
    def genterateRandomTime(self, startTime, endTime):
        startTimeArray = time.strptime(startTime, "%Y-%m-%d")
        endTimeArray = time.strptime(endTime, "%Y-%m-%d")
        #转为时间戳
        startTimeStamp = int(time.mktime(startTimeArray))
        endTimeStamp = int(time.mktime(endTimeArray))
        return random.randint(startTimeStamp, endTimeStamp)

    #生成字典形式的测试数据
    def integrationData(self, dirData):
        resData = {}
        if len(dirData) > 0:
            for key, value in dirData.items():
                valueList = value.split(" ")
                #eg {"tid":"int -"} 返回3位数的负数
                if valueList[0].strip() in ["int"] and len(valueList) == 2 and valueList[1] == "-":
                    resData[key] = 0 - self.genterateRandom(valueList[0], 3)
                #eg {"tid":"int 0"} 返回原型（零）
                elif valueList[0].strip() in ["int"] and len(valueList) == 2 and int(valueList[1]) == 0:
                    resData[key] = 0
                #eg {"tid":"int 10"} 返回长度为10的正整数
                elif valueList[0].strip() in ["int"] and len(valueList) == 2 and int(valueList[1]) > 0:
                    resData[key] = self.genterateRandom(valueList[0], int(valueList[1]))
                #eg {"tid":"int -2"} 返回原型（负数）
                if valueList[0].strip() in ["int"] and len(valueList) == 2 and len(valueList[1]) > 1 and "-" in valueList[1]:
                    resData[key] = 0 - int(valueList[1][1:])
                #eg {"offset":"str N"} 返回none
                if valueList[0].strip() in ["str"] and len(valueList) == 2 and valueList == "N":
                    resData[key] = None
                #eg {"offset":"str 10"} 返回长度为10的字符串，如果把10改成0就是空串
                elif valueList[0].strip() in ["str"] and len(valueList) == 2 and int(valueList[1]) >= 0:
                    resData[key] = self.genterateRandom(valueList[0], int(valueList[1]))
                #eg {"offset":"str 0 3"} 返回空格
                if valueList[0].strip() in ["str"] and len(valueList) == 3 and int(valueList[1]) == 0 and int(valueList[2]) >= 1:
                    resSpace = ""
                    for _ in range(int(valueList[2])):
                        resSpace += " "
                    resData[key] = resSpace
                #eg {"message":"chn 5"}返回长度为5的中文
                if valueList[0].strip() in ["chn"] and len(valueList) == 2 and int(valueList[1]) > 0:
                    resData[key] = self.genterateRandom(valueList[0], int(valueList[1]))
                #eg {"stateList":"list 8 9"} 返回长度为8， 每个元素包含9个字符的list
                if valueList[0].strip() == "list" and len(valueList) == 3 and int(valueList[1]) >= 0 and int(valueList[2]) >= 0:
                    resData[key] = self.genterateRandom(valueList[0], int(valueList[1]), int(valueList[2]))
                #eg {"time 2020-02-20 2020-02-23"} 返回时间范围内随机时间戳
                if valueList[0].strip() == "time" and type(valueList[1]) == str and type(valueList[2]) == str:
                    resData[key] = self.genterateRandomTime(valueList[1], valueList[2])
        else:
            print("test date cannot become '' ")

        return resData


if __name__ == "__main__":
    dirData = {"tid":"int -2", "offset":"str 0", "statelist":"list 8 9", "timestamp":"time 2020-02-20 2020-02-23", "message":"chn 5"}
    a = GenerateTestData()
    res = a.integrationData(dirData)
    print(res)