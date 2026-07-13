'''
hello_llm.py- My first OpenAI API Call
'''

# imports
import sys
from dotenv import load_dotenv
from openai import OpenAI


# Loading env files for API key
load_dotenv()

# Init OpenAI client object
client = OpenAI()

def ask(question: str) -> str:
    '''
        Sends question to LLM and returns response from LLM
    '''
    resp = client.chat.completions.create(
        model= "gpt-4o-mini",
        messages = [
            {"role":"system", "content":"Be concise." },
            {"role":"user", "content":question}
        ],
        temperature = 0.3,
    )
    return resp.choices[0].message.content

# For command-line run
if __name__ == "__main__":
    print(ask(" ".join(sys.argv[1:]) or "Hello"))