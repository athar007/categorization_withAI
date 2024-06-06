#
# @Author: Syed Athar Hussain
# @Date: 2024-02-04
# @LastEditTime: 
# @LastEditors: 2024-03-14
# @Description: main
#

#from WebContent.views.programs.m001p001_view import m001P001_view 
import WebContent.WEB_INF.file_config as file_config
from common.api.langchain_api import langchain_api_review
from action.m001p001.m001P001_action import data_processing
from m001P001_routes import app
if __name__ == "__main__":
    file_config.set_config()
    frame =app
    frame.run()
    # test = "指摘内容：帳票パイロット検証_チェックリスト_PRT_00102.xlsxによると、「PRT_00102」フォルダ内のファイルエラーがあり、帳票IDが一致しません。"
    # langchain_api_review(8,test)
    # url="http://10.167.84.241/redmine/projects/syuukei/issues.json?status_id=*&tracker_id=32&limit=3"
    # code=""
    # data_processing(url,code)