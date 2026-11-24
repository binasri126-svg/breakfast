from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = """
Suggest exactly 5 healthy breakfast ideas.
Include balanced sources of protein, fibre and carbohydrates.
Avoid deep-fried foods and excessive sugar.
Use a numbered list with one idea per line.
Do not include any introduction or explanation.
"""

reply = llm.invoke(prompt)

print(reply.content)
