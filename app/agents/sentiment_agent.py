from openai import OpenAI
from config.settings import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def analyze_market(news_text):
    prompt = f'''
你是一个专业量化分析师。

请分析以下新闻：

{news_text}

返回：
1. 市场情绪
2. 风险等级
3. 建议仓位
'''

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
