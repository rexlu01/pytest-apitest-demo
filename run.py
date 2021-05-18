import getopt
import shutil
import sys,os
import pytest
import subprocess


def init_report():
    cmd = "allure generate data --clean data -o report"
    subprocess.call(cmd, shell=True)
    project_path = os.path.abspath(os.path.dirname(__file__))
    report_path = project_path + "/report/" + "index.html"
    print(report_path)

def remove_all_files(path):
    try:
        shutil.rmtree(path)
    except Exception as e:
        print("clear cache files" + path + "faile.." + str(e))

def clear_cache():
    remove_all_files("data")
    remove_all_files("report")


if __name__ == "__main__":
    moudle = ""
    version = ""
    modle_and_version_message = ""
    try:
        opts, args  = getopt.getopt(sys.argv[1:], "m:v:", ["moudle=","version="])
        for opt, value in opts:
            if opt in ("-m", "--moudle"):
                moudle = value
            if opt in ("-v", "--version"):
                version = value
    except getopt.GetoptError:
        pass
    print("----hello---" + moudle + "-" + version)
    if moudle != "all" and moudle and version == "":
        pytest.main(["-v", "-s", f"case/{moudle}","--alluredir=data"])
        modle_and_version_message = f"moudel: " + moudle + "\n"
    elif moudle != "all" and moudle and version:
        pytest.main(["-s","-vv", f"cases/{moudle}/{version}","--alluredir=data"])
        modle_and_version_message = f"moudel: " + moudle + ", " + f"version: " + version + "\n"
    elif moudle == "backDoor":
        pytest.main(["-v",  "-s", f"cases/dti/4.5", "--alluredir=data"])
        modle_and_version_message = f"this is test " + "\n"
    with open("." + os.sep + "resultAPI.text", "a", encoding="utf8") as f:
        f.write(modle_and_version_message)
