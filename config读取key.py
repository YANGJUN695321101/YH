import os

def get_api_key():
    with open("D:/DESK/萤火/openai.env", "r") as f:
        api_key_line = f.readline().strip()
        api_key = api_key_line.split("=")[1]
        print(f"获取到的API密钥为：{api_key}")
    return api_key

get_api_key()
