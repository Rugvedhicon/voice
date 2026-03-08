import ollama
import re

def llm_similarity(original, transcript):

    prompt = f"""
Compare the meaning of these two sentences and output ONLY a number between 0 and 1.

Sentence 1: {original}
Sentence 2: {transcript}
"""

    response = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0}
    )

    text = response["message"]["content"]

    match = re.search(r"\d+\.?\d*", text)

    if match:
        return float(match.group())

    return None