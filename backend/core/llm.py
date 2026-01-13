
from openai import OpenAI
from backend.core.prompts import AURA_IDENTITY_PROMPT
from backend.core.context import build_context
from backend.utils.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(user_input: str, memory_summary: str) -> str:

    context = build_context(memory_summary)

    messages = [
        {"role": "system", "content": AURA_IDENTITY_PROMPT},
        {"role": "system", "content": context},
        {"role": "user", "content": user_input},
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.4,
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"[Aura Error] {str(e)}"

