#
# @Author: Syed Athar Hussain
# @Date: 2024-02-04
# @LastEditTime: 
# @LastEditors: 2024-03-14
# @Description: common function
#
import requests


def get_data(url,code):
    #codeの有無の場合、response_urlの変化
    # response_url=""
    if code.strip():
        response_url=url + "&parent_id=" +code
    else:
        response_url=url
    #追加異常処理    
    try:
        response = requests.get(response_url)
        # start エラーリターン、具体的な実現は未定
        if response.status_code!=200:
            return [response.status_code,{"result":[response.text]}]
        # end エラーリターン、具体的な実現は未定
        json_data =response.json()
      
        return [response.status_code,json_data]
        
    except requests.exceptions.RequestException as e:
        return [400,{"result":[e]}]
    
    
# get_data()を上方のget_dataとm001P001_action.pyのbの29~63行に分解する
# def get_data(url,code):
#     #codeの有無の場合、response_urlの変化
#     # response_url=""
#     if code.strip():
#         response_url=url + "&parent_id=" +code
#     else:
#         response_url=url
#     #追加異常処理    
#     try:
#         response = requests.get(response_url)
#         # start エラーリターン、具体的な実現は未定
#         if response.status_code!=200:
#             return [response.status_code,{"result":[response.text]}]
#         # end エラーリターン、具体的な実現は未定
#         json_data =response.json()
#         data =  {}
#         data['チケット番号'] = []
#         data['指摘内容'] = []
#         data['指摘内容_api用'] = []
#         data['処置内容'] = []
#         data['処置内容_api用'] = []
        
#         data['ステータス'] = []
#         for issues in json_data["issues"]:
#             data['チケット番号'].append(issues["id"])
#             data['ステータス'].append(issues["status"]["id"])
#             for custom_field in issues["custom_fields"]:
#                 if custom_field["id"] ==31:
#                     #指摘内容
#                     data['指摘内容'].append(custom_field["value"])
#                     if "指摘内容" in custom_field["value"]:
#                         data['指摘内容_api用'].append(custom_field["value"])
#                     else:
#                         data['指摘内容_api用'].append("指摘内容："+custom_field["value"])
#                 # TODO 処置内容
#                 elif custom_field["id"] ==33 :
#                 # if custom_field["id"] ==33 :
#                     print("処置内容",custom_field)
#                     data['処置内容'].append(custom_field["value"])
#                     if "処置内容" in custom_field["value"]:
#                         data['処置内容_api用'].append(custom_field["value"])
#                     else:
#                         data['処置内容_api用'].append("処置内容："+custom_field["value"])
                    
#             # print(data)
          
#         return [response.status_code,data]
        
#     except requests.exceptions.RequestException as e:
#         return [400,{"result":[e]}]
     
    
    
if __name__ == "__main__":
    #test
    url="http://10.167.84.241/redmine/projects/syuukei/issues.json?tracker_id=32"
    code="3963"
    get_data(url,code)