#
# @Author: Syed Athar Hussain
# @Date: 2024-02-04
# @LastEditTime: 
# @LastEditors: 2024-03-14
# @Description: constants
#
CUSTOM_CSS = """
#custom_button {
   max-width: 200px;
    max-height:30px;
    flex-wrap: nowrap;
}

#custom_process_btn {
    max-width: 200px;
    margin-left: 42%;
    min-height: 50px;
    font-size: 22px;
    background: #60965a;
    color: #ffffff;
}
#custom_radiobutton {
    padding:0;
    max-height:30px;
}
#custom_dropdown {
    max-height:40px;
    padding:0;
}
#custom_textbox {
    
    max-height:30px;
    padding:0;
}
#lable_css {
    max-width: 300px;
    max-height:30px;
    flex-wrap: nowrap;
    background-color:transparent;
}
.container.svelte-1pq4gst{
    padding:0 !important
}
.svelte-1mhtq7j {
    color:#1f2937;
    float: left;
}
.svelte-1mhtq7j label {
    width: 50% !important;
}
.svelte-1gfkn6j {
    display: none !important
}
.svelte-1kzox3m{
    overflow-y: hidden !important;
    height: 30px !important;
    padding: 0 !important;
    line-height: 2 !important;
    resize: none;
    text-indent: 10px;
    display: block;
}
.svelte-1f354aw {
    overflow-y: hidden !important;
    height: 30px !important;
    padding: 0 !important;
    line-height: 2 !important;
    resize: none;
    text-indent: 10px;
}

h2{
      margin: 0px;
    padding: 0px !important;
    font-size: 20px !important;
   
}
label{
    color:transparent;
    box-shadow: none;
    border:none;
    z-index:-999
}
.form{
 width: 50%;   
 
}
.border{
        box-shadow: var(--block-shadow);
    border-width: var(--block-border-width);
    border-color: var(--block-border-color);
    border-radius: var(--block-radius);
    
        box-sizing: border-box;
    border-width: 0;
    border-style: solid;
}
p{
    display: none !important;
}
footer{
    display: none !important;
}
.cell-wrap{
    white-space: pre-line;
}
table {
    overflow: auto;
}
th {
    width: auto !important;
    min-width:60px !important;
    text-align: center;
}
td {
    width: auto !important;
    min-width:60px !important;
}
td:nth-child(3) span {
    text-align: center !important;
}
td:nth-child(1) span{
    text-align: center !important;
}
td:nth-child(3) {
    max-width:60px !important;
    pointer-events: none;
}
td:nth-child(1){
    max-width:60px !important;
    pointer-events: none;
}
td:nth-child(2) {
    pointer-events: none;
}
td:nth-child(4){
    pointer-events: none;
}
th span{
    pointer-events: none;
}
td:nth-child(5){
    background-color:#ffffff;
    border-bottom: solid 0.05px #f1f3f5;
}
th:nth-child(3) {
    max-width:60px !important;
}
th:nth-child(1){
    max-width:60px !important;
}
# .svelte-vomtxz{
#     padding : 0 !important;
   
# }
# .svelte-sfqy0y{
#      position: absolute;
#     right: 0;
#     width: 150px;
#     z-index: 9999;
# }
.controls-wrap{
    display: none !important;
}
""" 
TITLE = {
    1:"指摘票レビュー",
    2:"Review of Issue Report"
}
REDMINE_URL={
    1:"RedmineのURL：",
    2:"RedmineURL："
}
EXCEL_PATH={
    1:"ファイルパス：",
    2:"File Path ："
}
PARENT_NUMBER={
    1:"親チケット番号：",
    2:"Parent Issue No："
}


REVIEW_LABLE={
    1:"レビュー",
    2:"Review"
}

POINT_OUT_CATEGORY={
    1:"指摘内容と指摘の根拠",
    2:"Pointed out contents and basis of pointing it out"
}

CAUSE_CATEGORY_CONTENT={
    1:"処置内容と不具合原因",
    2:"Description of action and cause of failure"
}
CONTENT_SELECT={
    1:"選択して続行します:",
    2:"Select to Proceed:"
}

CLEAR_LABLE={
    1:"クリア",
    2:"Clear"
}
REVIEW_LIST={
    1:"レビュー結果一覧",
    2:"List of Review Results"
}
REVIEW_CONTENT={
    1:"指摘内容",
    2:"Review Content"
}
TREATMENT_CONTENT={
    1:"処置内容",
    2:"Treatment Content"
}
CORRECTION={
    1:"修正",
    2:"Correction"
}
CLASSIFICATION={
    1:"区分",
    2:"Classification"
}

ISSUE_NO={
    1:"チケット番号",
    2:"Issue_No"
}

RESULT={
    1:"レビュー結果",
    2:"Result"
}
COMMENT={
    1:"説明",
    2:"Comment"
}
INSUFFICIENT_INFOR={
    1:"不足情報",
    2:"Insufficient_Information"
}
REVISED_ARTICLE={
    1:"修正後文章",
    2:"Revised article"
}
REFERENCE={
    1:"参考",
    2:"Reference"
}

POINT_CATEGORY={
    2:"Point Out Category Suggestions"
}
CAUSE_CATEGORY={
    2:"Cause Category Suggestions"
}
CAUSE_CLASSIFIATION={
    2:"Cause Classification Suggestions"
}
FINAL_CATEGORY={
    2:"Final Category"
}


