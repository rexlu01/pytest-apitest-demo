"""
按照指定格式生成测试数据
"""
import random
import string

class GenerateTestData():

    def LimitTestData(self, dirData, limit):
        # eg dirdata = {"tid":"int 1 60", "newowner":"str 20 100","leave":"obj 0 0"}
        d = {}
        for kv in dirData.items():
            datakey = kv[0]
            field = kv[1].split( )
            if field[0] == "int":
                ranint = random.randint(field[1],field[2])
                d[datakey] = ranint
            if field[0] == "str":
                ranint = random.randint(field[1],field[2])
                ranstr = ''.join(random.sample(string.ascii_letters + string.digits, ranint))
                d[datakey] = ranstr
        
        res = {"content":d}
        return res