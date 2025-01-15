from flask import Flask, render_template, request
import google.generativeai as genai

# Chave API
genai.configure(api_key="AIzaSyDKieJO0iC8vndmITnCw3Yc5SIOXfZccu0")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chatbot():
    response_text = ""
    if request.method == 'POST':
        language = request.form.get('language')
        if not language:
            response_text = "Por favor, selecione uma linguagem."
        else:
            question = request.form.get('intention')
            question2 = request.form.get('code')
            texto01 = "Considere a seguinte intenção do usuário: "
            texto02 = texto01 + question
            texto03 = texto02 + "\nTambém considere o código na linguagem de programação " + language + " a seguir: "
            texto04 = texto03 + question2 + "\nIdentifique o erro no código e me explique a causa."
            print(texto04)
            if question.strip():
                try:
                    model = genai.GenerativeModel('gemini-pro') 
                    response = model.generate_content(texto04)
                    response_text = response.text
                except Exception as e:
                    response_text = f"Erro ao gerar resposta: {str(e)}"
            else:
                response_text = "Por favor, insira uma pergunta."
    
    return render_template('index.html', response=response_text)

if __name__ == '__main__':
    app.run()