#!/usr/bin/python3

import openai
from snlp import tokenize, build_context
from bot.grennie import Greenie
from googletrans import Translator, constants

f = open ("data/example.txt")
raw = f.read()
raw = raw.replace('\n', '')
raw = raw.replace(';', '.')


# init the Google API translator
translator = Translator()

# translate a spanish text to english text (by default)
translation = translator.translate(raw)

messages = [
    {"role": "system", "content": "You are a helpful, pattern-following assistant that helps field operators and citizens on a smart city."},
    {"role": "system", "content": "If you don't know the answer to a question say, I don't know."},
    {"role": "system", "content": f'{raw}'},
    {"role": "user", "content": "Tell me the first item needed"},
]

if __name__ == '__main__':
    q = "whats the first step in the pcb charger assembly?"
    print(f'Before: {q}')
    tok = tokenize(q)
    print(f'After: {tok}')

    context = build_context(raw, tok)
    print(f'Context: {context}')

    bot = Greenie()
    tokens = bot.count_tokens(messages)
    total = bot.req_price(tokens)
    print (f'Tokens: {tokens}')
    print (f'Total Price: {total}$')

# openai.api_key = getenv("OPENAI_API_KEY")
# turbo = "gpt-3.5-turbo"
# custom_prompt = context # here you'll add the context plus conversation carried so far and question from user

# openai.Completion.create(
#     model = Model.TURBO,
#     prompt = context,
#     temperature = 0,
#     max_tokens = 10
# )




