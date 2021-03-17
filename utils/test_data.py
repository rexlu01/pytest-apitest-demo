"""
获取data里的测试数据
"""
import yaml
import os, sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

class GetTestData():

    #获取测试数据
    def get_test_data(self, file_name):
        case = []
        http = []
        expected = []
        if type(file_name) == str:
            data_path = rootPath + "/data/" + file_name
        with open(data_path, encoding="utf-8") as f:
            dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
            test_data = dat["tests"]
            for td in test_data:
                case.append(td.get("case",""))
                http.append(td.get("http",""))
                expected.append(td.get("expected",{}))
        parameters = zip(case, http, expected)
        return case, parameters

if __name__ == "__main__":
    a = GetTestData()
    case, res = a.get_test_data("demo/test_in_search.yaml")
    print(list(res))