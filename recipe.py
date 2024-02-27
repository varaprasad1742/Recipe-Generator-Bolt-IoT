from flask import Flask,render_template,request,render_template_string
import openai
import os
import re

openai.api_key="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"


def chat_gpt(prompt: str):
  if openai.api_key=="":
    print("No api key available")
    exit(1)
  response=openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role":"system","content":"You are a helpful assistant."},
      {"role":"user","content":f'I have some ingredients. Using these ingredients make a recipe. Have a nice name to it at start and give steps how to make it. Finally give an interesting fact about the recipe. Here are the ingredients {prompt} oil, salt, sugar, water, yeast, flour, baking powder.'}
    ]
  )
  return response.choices[0].message.content


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    if request.method == 'POST':
        components = request.form['components']
        output = chat_gpt(components)
        output= re.sub("*","",output)
        flag=True
    return render_template("index.html",output=output)




@app.route('/generate', methods=['POST'])
def generate():
    components = request.form['components']
    return chat_gpt(components)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug="True")

  
  