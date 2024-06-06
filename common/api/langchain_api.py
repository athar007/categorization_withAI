#
# @Author: Syed Athar Hussain
# @Date: 2024-02-04
# @LastEditTime: 
# @LastEditors: 2024-03-14
# @Description:langchainのapi呼び出し
#
import os

from langchain.callbacks import get_openai_callback
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema import HumanMessage, SystemMessage
import openai
from openai.api_resources.abstract.engine_api_resource import EngineAPIResource
# from ..const.m001P001_const import (QUESTION_TEXT,JOSN_FORMAT)
import common.const.m001P001_const as m001P001_const



def langchain_api_review(type,text,languageType):
    openai.log = "debug"
    
    # # ChatAIを使えるようにする。
    EngineAPIResource.class_url = lambda a, b, c: ""
    api_key = os.getenv('OPENAI_API_KEY')
    api_base = "https://ai-foundation-api.app/ai-foundation/chat-ai/gpt4"
    openai.api_type = "azure"
    openai.api_version = "2023-05-15"
    chat = ChatOpenAI(
        model_name='gpt-4-32k',
        openai_api_key = api_key, 
        openai_api_base = api_base,
        model_kwargs={"deployment_id":""},
        temperature=0
    )

    template = (
        "{text}{question}{format}"
    )

    human_message_prompt = HumanMessagePromptTemplate.from_template(template)
    
    chat_prompt = ChatPromptTemplate.from_messages(
        [human_message_prompt]
    )

    # Get result and track token usage
    with get_openai_callback() as cb:
        # get a chat completion from the formatted messages
        if type==1:
            # 指摘内容
            result = chat(chat_prompt.format_prompt(text=text,question=m001P001_const.QUESTION_TEXT[languageType],format=m001P001_const.JOSN_FORMAT_EN).to_messages())
        elif type==2:
            # 処置内容
            result = chat(chat_prompt.format_prompt(text=text,question=m001P001_const.QUESTION_TEXT1[languageType],format=m001P001_const.JOSN_FORMAT_EN).to_messages())
        print("哈哈哈测试",m001P001_const.QUESTION_TEXT[languageType]+m001P001_const.JOSN_FORMAT[languageType])
        return result.content

def langchain_api_revise(type,content1,content2,content3,languageType):
    openai.log = "debug"
    
    # # ChatAIを使えるようにする。
    EngineAPIResource.class_url = lambda a, b, c: ""
    api_key = os.getenv('OPENAI_API_KEY')
    api_base = "https://ai-foundation-api.app/ai-foundation/chat-ai/gpt4"
    openai.api_type = "azure"
    openai.api_version = "2023-05-15"
    chat = ChatOpenAI(
        model_name='gpt-4-32k',
        openai_api_key = api_key, 
        openai_api_base = api_base,
        model_kwargs={"deployment_id":""},
        temperature=0
    )

    template = (
        "{text1}{content1}{text2}{content2}{text3}{content3}{text4}"
    )

    human_message_prompt = HumanMessagePromptTemplate.from_template(template)
    
    chat_prompt = ChatPromptTemplate.from_messages(
        [human_message_prompt]
    )

    # Get result and track token usage
    with get_openai_callback() as cb:
        # get a chat completion from the formatted messages
        if type==1:
            # 指摘内容
            result = chat(chat_prompt.format_prompt(text1=m001P001_const.TEST1[languageType],content1=content1,text2=m001P001_const.TEST2[languageType],content2=content2,text3=m001P001_const.TEST3[languageType],content3=content3,text4=m001P001_const.TEST4_EN).to_messages())
        elif type==2:
            # 処置内容
            result = chat(chat_prompt.format_prompt(text1=m001P001_const.TEST5[languageType],content1=content1,text2=m001P001_const.TEST6[languageType],content2=content2,text3=m001P001_const.TEST7[languageType],content3=content3,text4=m001P001_const.TEST8_EN).to_messages())
        print("问题：",m001P001_const.TEST5[languageType]+content1+m001P001_const.TEST6[languageType]+content2+m001P001_const.TEST7[languageType]+content3+m001P001_const.TEST8_EN)
        print("哈哈哈测试result",result)
        return result.content

def langchain_api_ok_revise(type,content):
    openai.log = "debug"
    
    # # ChatAIを使えるようにする。
    EngineAPIResource.class_url = lambda a, b, c: ""
    api_key = os.getenv('OPENAI_API_KEY')
    api_base = "https://ai-foundation-api.app/ai-foundation/chat-ai/gpt4"
    openai.api_type = "azure"
    openai.api_version = "2023-05-15"
    chat = ChatOpenAI(
        model_name='gpt-4-32k',
        openai_api_key = api_key, 
        openai_api_base = api_base,
        model_kwargs={"deployment_id":""},
        temperature=0
    )
    
    template = (
         "{text1}{content1}{text2}{text4}"
    )

    human_message_prompt = HumanMessagePromptTemplate.from_template(template)
    
    chat_prompt = ChatPromptTemplate.from_messages(
        [human_message_prompt]
    )

    # Get result and track token usage
    with get_openai_callback() as cb:
        # get a chat completion from the formatted messages
        if type==1:
            # 指摘内容
            print("来来来——指摘内容——不足情报——无")
            result = chat(chat_prompt.format_prompt(text1=m001P001_const.TEST1[1],content1=content,text2=m001P001_const.OK_TEST2,text4=m001P001_const.TEST4_EN).to_messages())
        elif type==2:
            # 処置内容
            result = chat(chat_prompt.format_prompt(text1=m001P001_const.TEST5[1],content1=content,text2=m001P001_const.OK_TEST6,text4=m001P001_const.TEST8_EN).to_messages())
        print("test",result)
        return result.content
    
def pointOutCategoryFun(pointed_outcontents):

    EngineAPIResource.class_url = lambda a, b, c: ""
    api_key = os.getenv('OPENAI_API_KEY')
    api_base = "https://ai-foundation-api.app/ai-foundation/chat-ai/gpt4"
    openai.api_type = "azure"
    openai.api_version = "2023-05-15"
    llm = ChatOpenAI(
        model_name='gpt-4-32k',
        openai_api_key = api_key, 
        openai_api_base = api_base,
        model_kwargs={"deployment_id":""},
        temperature=1
    )
    model_kwargs = {"device": "cpu"}
    pointed_out_category = []
    i=0
    
    
    for value in pointed_outcontents:
        if not (isinstance(value, float)):
            template = (
                """You are a helpful assistant that predicts the suitable list of categories with atleast 1 and maximum 3 category of {value} out of these 
                ('01: 内容漏れ', '02: 内容誤り', '03: 記述曖昧／不備', '04: 仕様間不整合', 
                '05:改善', '06: 共通仕様違反', '07: 記述冗長／不統一') categories
                using the conditions choose '01: 内容漏れ' when the content is '設計の内容に漏れがある。', 
                choose '02: 内容誤り' when the content is '設計の内容が誤っている。', choose '03: 記述曖昧／不備' 
                when the content is '設計書の記述が曖昧である。または表現上の考慮が不足している。', 
                choose '04: 仕様間不整合' when the content is '設計書内または設計書間の整合性が取れていない。', 
                choose '05:改善' when the content is '内容自体に誤りはないが、効率化、性能の観点等で改善した方がよい。',
                choose '06: 共通仕様違反' when the content is '設計の内容がシステム共通仕様に従っていない。', 
                choose '07: 記述冗長／不統一' when the content is 
                '設計書の記述が冗長で分かり辛い。または設計書間で記述が統一されていない。', and return output
                  as a list of category inside [] without aditional content and suggestions"""
            )
            val = value
            if val=="":
                break
            
            input_data = SystemMessagePromptTemplate.from_template(template)
            input_data1 = HumanMessagePromptTemplate.from_template(val)
            try:
                chat_prompt = ChatPromptTemplate.from_messages(
                    [input_data, input_data1]
                )
                print("--------------------------")
                print(val, i+1)
                result = llm(
                    chat_prompt.format_prompt(
                        value=val
                    ).to_messages()
                )
                pointed_out_category.append(result.content)
                print(result.content, i)
                i=i+1
                
            except Exception as e:
                pointed_out_category.append("カテゴリが見つかりません")
    return pointed_out_category

def causeclassificationFun(categorycontents):
    print("cause")
    EngineAPIResource.class_url = lambda a, b, c: ""
    api_key = os.getenv('OPENAI_API_KEY')
    api_base = "https://ai-foundation-api.app/ai-foundation/chat-ai/gpt4"
    openai.api_type = "azure"
    openai.api_version = "2023-05-15"
    llm = ChatOpenAI(
        model_name='gpt-4-32k',
        openai_api_key = api_key, 
        openai_api_base = api_base,
        model_kwargs={"deployment_id":""},
        temperature=0
    )
    cause_classification = []
    i=0
    for value in categorycontents:
        
        if not (isinstance(value, float)):
            template = (
                """You are a helpful assistant that predicts the suitable list of categories with atleast 1 and maximum 3 category for {value} out of these 
                ('10:仕様変更（条件変更）', '11:仕様変更（仕様不具合）', '12:設計変更', '13:要件追加', 
                '20:検討不足', '21:影響調査漏れ', '22:標準化／規約不足', '23:提示条件の確認不足', '24:関連機能の確認不足'
                , '30:修正漏れ', '31:修正誤り', '32:標準化／規約違反', '33:周知連絡不徹底', '34:表現の配慮不足', 
                '35:単純ミス', '40:ノウハウ不足', '50:その他', '80:設計の改善', '90:指摘ミス', '91:対応せず（仕様通り）') categories 
                using the conditions choose '10:仕様変更（条件変更）' when the content is '提示された仕様に条件変更等があり、仕様を変更する（影響小）。', 
                choose '11:仕様変更（仕様不具合）' when the content is '提示された仕様に不具合があり、仕様を変更する（影響中）。',
                  choose '12:設計変更' when the content is '提示された要件に不具合もしくは不足があり、設計を変更する（影響大）。', 
                choose '13:要件追加' when the content is '提示された要件に不足があり、設計を追加する（影響大）。', 
                choose '20:検討不足' when the content is '設計内容の検討が不足している。または検討が漏れている。',
                choose '21:影響調査漏れ' when the content is '他不具合等が起因となる影響調査時に、調査対象から漏れていた。', 
                choose '22:標準化／規約不足' when the content is '作業標準、記述規約の記載内容が不足している。', 
                choose '23:提示条件の確認不足' in rare cases when the content is '提示条件の確認が不足している。または確認が漏れていた。',
                  choose '24:関連機能の確認不足' when the content is '関連機能の確認が不足している。または確認が漏れていた。', 
                  choose '30:修正漏れ' when the content is '不具合対応時の修正を漏らした。', choose '31:修正誤り' 
                when the content is '不具合対応時の修正を誤った。', 
                choose '32:標準化／規約違反' when the content is '作業標準、記述規約に従っていない。', 
                choose '33:周知連絡不徹底' when the content is '制限事項、変更内容等の周知／連絡をしていなかった。または漏れていた。',
                choose '34:表現の配慮不足' when the content is '記述内容に誤りは無いが、解釈が困難であったり、誤解を招きかねない表現／記述である。', 
                choose '35:単純ミス' when the content is '注意していれば防げたはずの誤り（単純ミス、ケアレスミス、うっかりミス）。', 
                choose '40:ノウハウ不足' in rare cases when the content is '作業を遂行するうえで必要なノウハウが不足していた。' choose '50:その他' 
                when the content is '上記以外の不具合。※基本的に使用しないこと。', 
                choose '80:設計の改善' when the content is '設計内容自体の誤りではなく、プロセス効率化・性能向上等の観点で仕様を改善した。', 
                choose '90:指摘ミス' when the content is '調査の結果、設計の内容で正しかった。',
                choose '91:対応せず（仕様通り）' when the content is '調査／検討の結果、設計内容の通りとした。', and return output
                  as a list of category inside [] without aditional content and suggestions"""
            )
            val = value
            input_data = SystemMessagePromptTemplate.from_template(template)
            input_data1 = HumanMessagePromptTemplate.from_template(val)
            try:
                chat_prompt = ChatPromptTemplate.from_messages(
                    [input_data, input_data1]
                )
                print("--------------------------")
                print(val, i+1)
                result = llm(
                    chat_prompt.format_prompt(
                        value=val
                    ).to_messages()
                )
                cause_classification.append(result.content)
                print(cause_classification[i], i)
                i=i+1
            except Exception as e:
                cause_classification.append("Unable to get the category")


    return cause_classification


if __name__ == '__main__':
    test = "指摘箇所:CBD00101のソース ビルド時にWarningが表示される "
    langchain_api_review(7,test)
