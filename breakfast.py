from langchain_openai import ChatOpenAI

# Create the AI model
llm = ChatOpenAI(model="gpt-4o-mini")

# Give instructions to the model
prompt = """
Give me exactly 5 healthy breakfast ideas.

Each idea should be nutritious and balanced, preferably with
protein, fiber, and healthy ingredients.

Format:
1. One breakfast idea
2. One breakfast idea
3. One breakfast idea
4. One breakfast idea
5. One breakfast idea

Give one idea per line.
Do not include any introduction or conclusion.
"""

# Send the prompt to the AI
reply = llm.invoke(prompt)

# Print only the actual text response
print(reply.content)