from flask import Flask, render_template, request
import google.generativeai as genai

# Chave API
genai.configure(api_key="AIzaSyClYeI7WsOpD-2FCEanStmn2MV7S1TPBGM")

app = Flask(__name__) # objeto app que define as rotas e lida com requisições HTTP

@app.route('/', methods=['GET', 'POST']) # definicao de rota, aceita tanto GET quanto POST
def chatbot():
    response_text = ""
    if request.method == 'POST':
        language = request.form.get('language') # recupera o código submetido pelo usuário.
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
                    model = genai.GenerativeModel('gemini-pro') # O modelo gemini-pro é usado para processar a solicitação.
                    response = model.generate_content(texto04) # A função retorna a análise gerada pelo modelo em resposta ao texto enviado.
                    response_text = response.text
                except Exception as e:
                    response_text = f"Erro ao gerar resposta: {str(e)}"
            else:
                response_text = "Por favor, insira uma pergunta."
    
    return render_template('index.html', response=response_text)

if __name__ == '__main__':
    app.run()