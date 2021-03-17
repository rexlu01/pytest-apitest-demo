"""
获取config里的数据
"""
import yaml
import os, sys

class GetData():

    def __init__(self):
        curPath = os.path.abspath(os.path.dirname(__file__))
        self.rootPath = os.path.split(curPath)[0]
        sys.path.append(self.rootPath)

    
    def get_config_data(self,confrow,environmental="test"):
        if environmental == "test":
            config_path = self.rootPath + "/config/test/config.yaml"
        elif environmental == "dev":
            config_path = self.rootPath + "/config/dev/config.yaml"
        
        with open(config_path) as f:
            dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
            base_config = dat["base_config"]
            for cd in base_config:
                if cd.get(confrow):
                    return cd.get(confrow)
        
        return None
