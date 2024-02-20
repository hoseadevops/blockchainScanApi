import os
import re
import sys
import json
import fire
import requests

# 创建相对路径文件夹
def mkdir(file_path):
  directory = os.path.dirname(file_path)
  if not os.path.exists(directory):
    os.makedirs(directory)

class contract(object):

  def getsourcecode(self, project, address):
    
    url = "https://api.etherscan.io/api"
    API_KEY = os.environ["API_KEY"]
    params = {
      "module": "contract",
      "action": "getsourcecode",
      "address": address,
      "apikey": API_KEY
    }

    print("DEBUG: ", project, address)

    response = requests.get(url, params=params)
    data = response.json()
    
    # 错误处理
    if(data["status"] == "0"):
      print(data["result"])
      sys.exit(1)

    SourceCode = data["result"][0]["SourceCode"]
    # 多文件
    if SourceCode.startswith("{"):
      # 修正双括号
      SourceCode = re.sub(r"\{+", "{", SourceCode)
      SourceCode = re.sub(r"\}+", "}", SourceCode) 
      # 解析json
      SourceCode = json.loads(SourceCode)

      # 文件路径
      for name, code in SourceCode["sources"].items():
        name = "project/" + project + "/" + name
        # 创建路径
        mkdir(name)
        with open(name, "w") as file:
          file.write(code["content"])
    else:
      # 单文件
      name = data["result"][0]["ContractName"] + ".sol";
      name = "project/" + project + "/" + name
      mkdir(name)
      with open(name, "w") as file:
        file.write(SourceCode)

if __name__ == '__main__':
  fire.Fire(contract)