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

    def get_base_env(self):
        env_path = self.rootPath + "/config/envconfig.yaml"

        with open(env_path) as f:
            env = yaml.load(f.read(), Loader=yaml.SafeLoader)
            base_env = env["base_env"][0]
            return base_env.get("env").get("environmental")

if __name__ == "__main__":
    a = GetData()
    res = a.get_base_env()
    print(res)
