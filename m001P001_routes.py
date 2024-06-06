#
# @Author: Syed Athar Hussain
# @Date: 2024-02-04
# @LastEditTime: 
# @LastEditors: 2024-03-14
# @Description: routes
#
import os
import shutil
import pandas as pd
from flask import Flask, render_template, request,abort,send_file
from werkzeug.utils import secure_filename

# from ..assets.const.m001P001_const import (custom_css,)
# from WebContent.views.assets.const.m001P001_const import (CUSTOM_CSS,REDMINE_URL,PARENT_NUMBER,REVIEW_LABLE,CLEAR_LABLE,
#                                            REVIEW_LIST,REVIEW_CONTENT,TREATMENT_CONTENT,CORRECTION,
#                                            CLASSIFICATION,EXCEL_PATH,TITLE,ISSUE_NO,RESULT,COMMENT,
#                                            INSUFFICIENT_INFOR,REVISED_ARTICLE,REFERENCE)
# from action.m001p001.m001P001_action import (data_processing,get_extra_info,data_batch_revise,excel_read_info)
from WebContent.views.programs.m001p001_view import m001P001_view

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.csv', '.xlsx', '.xlsm']
app.config['UPLOAD_PATH'] = './data/input'
app.config['DOWNLOAD_PATH'] = './data/output/'

form_data = m001P001_view()

@app.route('/') 

# import web as const
def homepage(): 

# returning index.html and list 
# and length of list to html page 
    return render_template("index.html")

@app.route('/redmine_review', methods=['POST'])
def form_redmine_review():
    print("form_redmine_url_check")
    print(request.form['redmine_url'])
    redmine_url = request.form['redmine_url']
    parent_no = request.form['parent_no']
    
    content_change = request.form['inlineRadioOptions']
    redmine_review_data = form_data.redmine_review(redmine_url, parent_no,content_change)
    print("redmine_review_data length:--")
    return render_template("redmine-review.html", len=len(redmine_review_data['Issue_No']),review_content = redmine_review_data,content_change=content_change, step=1)

@app.route('/excel_review', methods=['POST'])
def form_excel_review():
    uploaded_file = request.files['excel_path']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    content_change = request.form['inlineRadioOptions']
    path = app.config['UPLOAD_PATH']+"/"+filename
    print(path)
    excel_review_data = form_data.excel_review(path, content_change)

    print("redmine_review_data length:--")
    return render_template("redmine-review.html", len=len(excel_review_data['Issue_No']),review_content = excel_review_data,content_change=content_change, step=1)

@app.route('/correction', methods=['POST'])
def form_table_correction():
    print("form_redmine_url_check")
    data=request.form.get('review_content')
    data_dict= eval(data)
    length=len(data_dict['Issue_No'])
    for i in range(0,length):
        data_dict['Insufficient_Information'][i]=request.form.get('textarea'+str(i))
    print(data_dict['Insufficient_Information'])
    content_change = request.form['content_change']
    # modified_data=global_mo
    print(content_change)
    insufficient_data=form_data.global_modify(data_dict,content_change)
    print("form_check")
    return render_template("redmine-review.html", len=len(insufficient_data['Issue_No']),review_content = insufficient_data, content_change=content_change, step=2)

@app.route('/category_generation', methods=['POST'])
def form_table_category_generation():
    print("form_redmine_url_check")
    data=request.form.get('review_content')
    data_dict= eval(data)
    content_change = request.form['content_change']
    # modified_data=global_mo
    print(content_change)
    category_suggestions=form_data.category_suggestion(data_dict, content_change)
    print("form_check")
    return render_template("redmine-review.html", len=len(category_suggestions['Issue_No']),review_content = category_suggestions, content_change=content_change, step=3)

@app.route('/extract_to_excel', methods=['POST'])
def form_table_extract_to_excel():
    content_change = request.form['content_change']
    data=request.form.get('review_content')
    data_dict= eval(data)
    length=len(data_dict['Issue_No'])
    print(length)
    for i in range(0,length):
        data_dict['Final Category'].append(request.form.get('final_cat'+str(i)))
    # modified_data=global_mo
    print("category")
    print(data_dict['Final Category'])
    download_path = form_data.process_table_to_excel(data_dict, content_change)
    if download_path[0]==1:
        return render_template("success-download.html")
    else:
        return render_template("error-download.html", error = download_path[1])

@app.route('/download')
def download():
    result_path = "./data/output/output_00_review-sheet.xlsm"
    return send_file(result_path, as_attachment=True)

if __name__ == '__main__':

        # running app 
    app.run()


