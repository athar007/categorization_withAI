#
# @Author: India GDC
# @Date: 2024-02-04
# @LastEditTime: 
# @LastEditors: 2024-03-14
# @Description: const
#
QUESTION_TEXT={
    1:"上記の指摘に正確な指示と問題内容が明確に記載していますか？他の回答がいらない、以下のフォーマットに沿って返信してください",
    2:"Does the above comment clearly state the precise instructions and the problem content? No other answers are needed, please reply according to the following format: "
}
JOSN_FORMAT = {
    1:"\{\"result\": \"OK/NG\",\"content\": \"NGの場合、簡単にNGの所のみ説明　OKの場合、説明無し\"\}",
    2:"\{\"result\": \"OK/NG\",\"content\": \"If it's NG, briefly explain only the NG part. If it's OK, no explanation is needed.\"\}"
    
}
JOSN_FORMAT_EN="\{\"result\": \"OK/NG\",\"JP_content\": \"NGの場合、簡単にNGの所のみ説明　OKの場合、説明無し\",\"EN_content\": \"If it is NG, please provide a brief explanation of the location of the problem. If it is OK, no explanation is needed.\"\}",

# テスト用
# QUESTION_TEXT1="上記の指摘に指摘箇所と指摘根拠が明確に記載していますか？他の回答がいらない、以下のフォーマットを返信してください"
# JOSN_FORMAT1 = "\{\"result\": \"OK/NG\",\"content\": \"説明\"\}"

# QUESTION_TEXT2="上記の指摘にあるべき箇所と今問題発生する箇所が明確に記載していますか？？他の回答がいらない、以下のフォーマットを返信してください"
# JOSN_FORMAT2 = "\{\"result\": \"OK/NG\",\"content\": \"説明\"\}"

# QUESTION_TEXT3="上記の指摘にあるべき内容と今問題発生する内容が明確に記載していますか？他の回答がいらない、以下のフォーマットを返信してください"
# JOSN_FORMAT3 = "\{\"result\": \"OK/NG\",\"content\": \"説明\"\}"

# QUESTION_TEXT4="上記の指摘にどうすべきの記述と今問題発生した内容の記述が明確に記載していますか？他の回答がいらない、以下のフォーマットを返信してください"
# JOSN_FORMAT4 = "\{\"result\": \"OK/NG\",\"content\": \"NGの場合、NGの所のみ説明　OKの場合、説明無し\"\}"

# QUESTION_TEXT5="上記の指摘にどうすべきの記述と今問題発生した内容の記述が明確に記載していますか？以下のフォーマットを返信してください"
# JOSN_FORMAT5 = "\{\"result\": \"OK/NG\",\"content\": \"NGの場合、簡単にNGの所のみ説明　OKの場合、説明無し\"\}"


# QUESTION_TEXT6="上記指摘内容に、指摘箇所と該当した箇所にあるべき内容の記載がありますか？他の回答がいらない、以下のフォーマットを返信してください"
# JOSN_FORMAT6 = "\{\"result\": \"OK/NG\",\"content\": \"NGの場合、簡単にNGの所のみ説明　OKの場合、説明無し\"\}"

# QUESTION_TEXT7="上記の指摘に正確な指示の記述と今問題発生した内容の記述が明確に記載していますか？他の回答がいらない、以下のフォーマットを返信してください"
# JOSN_FORMAT7 = "\{\"result\": \"OK/NG\",\"content\": \"NGの場合、簡単にNGの所のみ説明　OKの場合、説明無し\"\}"

# QUESTION_TEXT8="上記の指摘に正確な指示の記述と問題内容の記述が明確に記載していますか？他の回答がいらない、以下のフォーマットを返信してください"
# JOSN_FORMAT8 = "\{\"result\": \"OK/NG\",\"content\": \"NGの場合、簡単にNGの所のみ説明　OKの場合、説明無し\"\}"

#処置内容：
QUESTION_TEXT1={
    1:"上記の内容について、以下の要素を参照し、具体的な処置内容と不具合原因を記載していますか？問題発生主体、問題発生原因、正確内容、問題内容。他の回答がいらない、以下のフォーマットに沿って返信してください",
    2:"Does the above content refer to the following elements and describe the specific treatment content and the cause of the malfunction? Problem occurrence entity, problem cause, accurate content, problem content.No other answers are needed, please reply according to the following format."
}
JOSN_FORMAT1 ={
    1: "{\"result\": \"OK/NG\",\"content\": \"NGの場合、簡単にNGの所のみ説明　OKの場合、説明無し\"\}",
    2:"{\"result\": \"OK/NG\",\"content\": \"If NG, briefly explain only the NG part. If OK, no explanation\"}"
}


# 処置内容テスト用
# QUESTION_TEXT1="上記の処置内容と不具合原因に問題発生の主体、原因、正確な姿、誤りと修正前や修正後内容が明確に記載していますか？以下のフォーマットを返信してください"
# JOSN_FORMAT1 = "{\"result\": \"OK/NG\",\"content\": \"NGの場合、NGの所説明　OKの場合、説明無し\"\}"


# QUESTION_TEXT2="上記の処置内容と不具合原因に問題発生の主体、原因、正確な姿、誤りと修正前や修正後内容が明確に記載していますか？以下のフォーマットを返信してください"
# JOSN_FORMAT2 = "{\"result\": \"OK/NG\",\"content\": \"NGの場合、簡単にNGの所のみ説明　OKの場合、説明無し\"\}"


# QUESTION_TEXT3="上記の処置内容と不具合原因について、原因として、問題発生主体、問題発生原因、正確内容、問題内容など要素が明確に記載していますか？以下のフォーマットを返信してください"
# JOSN_FORMAT3 = "{\"result\": \"OK/NG\",\"content\": \"NGの場合、簡単にNGの所のみ説明　OKの場合、説明無し\"\}"


# QUESTION_TEXT4="上記の処置内容と不具合原因について、原因として、問題発生主体、問題発生原因、正確内容、問題内容など要素が記載していますか？処置内容として、修正前後内容が記載していますか？以下のフォーマットを返信してください"
# JOSN_FORMAT4 = "{\"result\": \"OK/NG\",\"content\": \"NGの場合、簡単にNGの所のみ説明　OKの場合、説明無し\"\}"

# QUESTION_TEXT5="上記の処置内容と不具合原因について、以下の要素が含まれていますか？問題発生主体、問題発生原因、正確内容、問題内容、修正前後内容。以下のフォーマットを返信してください"
# JOSN_FORMAT5 = "{\"result\": \"OK/NG\",\"content\": \"NGの場合、簡単にNGの所のみ説明　OKの場合、説明無し\"\}"


# QUESTION_TEXT6="上記の処置内容と不具合原因について、以下の要素が含まれていますか？問題発生主体、問題発生原因、正確内容、問題内容、修正前後内容。他の回答がいらない、以下のフォーマットに沿って返信してください"
# JOSN_FORMAT6 = "{\"result\": \"OK/NG\",\"content\": \"NGの場合、簡単にNGの所のみ説明　OKの場合、説明無し\"\}"


# QUESTION_TEXT7="上記の処置内容と不具合原因について、以下の要素が含まれていますか？問題発生主体、問題発生原因、正確内容、問題内容、修正前後内容。以下のフォーマットに沿って返信してください"
# JOSN_FORMAT7 = "{\"result\": \"OK/NG\",\"content\": \"NGの場合、説明　OKの場合、説明無し\"\}"

# QUESTION_TEXT8="上記の内容について、以下の要素を参照し、具体的な処置内容と不具合原因を記載していますか？ A：人・モノ（誰が？何が？）B：何が原因でこの事象が発生してしまったのかを記述する。 C：あるべき姿を記述する。 D：現状どうであったかを記述する。以下のフォーマットに沿って返信してください"
# JOSN_FORMAT8 = "{\"result\": \"OK/NG\",\"content\": \"NGの場合、説明　OKの場合、説明無し\"\}"

# QUESTION_TEXT9="上記の内容について、以下の要素を参照し、具体的な処置内容と不具合原因を記載していますか？問題発生主体、問題発生原因、正確内容、問題内容。以下のフォーマットに沿って返信してください"
# JOSN_FORMAT9 = "{\"result\": \"OK/NG\",\"content\": \"NGの場合、説明　OKの場合、説明無し\"\}"


# QUESTION_TEXT="上記の内容について、以下の要素を参照し、具体的な処置内容と不具合原因を記載していますか？問題発生主体、問題発生原因、正確内容、問題内容。他の回答がいらない、以下のフォーマットに沿って返信してください"
# JOSN_FORMAT = "{\"result\": \"OK/NG\",\"content\": \"NGの場合、簡単にNGの所のみ説明　OKの場合、説明無し\"\}"

TEST1={
    1:"指摘内容：",
    2:"Comments:"
}
TEST2={
    # 1:"\r\n上記の指摘内容について、下記の説明と補充情報を参照し、正確な指示と問題内容を補充してください。\r\nNG説明：",
    1:"\r\n上記の指摘内容について、下記の説明と補充情報を参照し、改修してください。。\r\nNG説明：",
    2:"\r\nFor the above comments, please refer to the following explanations and supplementary information, and make corrections.\r\nNG explanation: "
}

# OK_TEST2="\r\n上記の指摘内容について、「下さい」や「お願い」など指示ような意を含む文章に改修してください。 "
OK_TEST2="\r\n上記の指摘内容について、適度に具体的な指示と問題内容を含む文章に改修してください。 "
TEST3={
    1:"\r\n補充情報：",
    2:"\r\nSupplementary information: "
}
TEST4={
    1:"\r\n他の回答がいらない、以下のフォーマットを返信してください {\"content\": \"修正後指摘内容\"\}",
    2:"\r\nNo other answers are needed, please reply in the following format {\"content\": \"Revised comments\"\}"
}
TEST4_EN="\r\n他の回答がいらない、以下のフォーマットを返信してください {\"JP_content\": \"修正後指摘内容\",\"EN_content\": \"Revised comments\"\}"





# QUESTION="指摘内容：{}\r\n上記の指摘内容について、下記の説明と補充情報を参照し、改修してください。\r\nNG説明：{}\r\n補充情報：{}\r\n他の回答がいらない、以下のフォーマットを返信してください {\"content\": \"修正後指摘内容\"\}"

TEST5={
    1:"処置内容：",
    2:"Treatment Content: "
}
TEST6={
    # 1:"\r\n上記の処置内容について、下記の説明と補充情報を参照し、原因と対処を改修してください。。\r\nNG説明：",
    1:"\r\n上記の処置内容について、下記の説明と補充情報を参照し、改修してください。\r\nNG説明：",
    2:"\r\nPlease revise the above treatment content by referring to the following explanation and supplementary information.\r\n NG Explanation: "
}
# OK_TEST6="\r\n上記の処置内容について、適度に具体的な処置内容と不具合原因を含む文章に改修してください。 "
OK_TEST6="\r\n上記の処置内容について、処置内容と不具合原因ような意を含む文章に改修してください。 "
TEST7={
    1:"\r\n補充情報：",
    2:"\r\nSupplementary Information: "
}
TEST8={
    1:"\r\n他の回答がいらない、以下のフォーマットを返信してください {\"content\": \"【原因】：…　【対処】：…\"\}",
    2:"\r\nNo other answers are needed, please reply in the following format {\"content\": \"【Cause】:... 【Treatment】:...\"\}"
}
TEST8_EN="\r\n他の回答がいらない、以下のフォーマットを返信してください {\"JP_content\": \"【原因】：…　【対処】：…\",\"EN_content\": \"【Cause】：…　【Handle】：…\"\}"










