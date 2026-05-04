from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_project = None
    email_saved = None
    text_saved = None

    if request.method == 'POST':
        if 'email' in request.form:
            email_saved = request.form.get('email')
            text_saved = request.form.get('text')

        elif 'button_python' in request.form:
            selected_project = 'python'
        elif 'button_discord' in request.form:
            selected_project = 'discord'
        elif 'button_html' in request.form:
            selected_project = 'html'
        elif 'button_db' in request.form:
            selected_project = 'db'

    return render_template(
        'index.html',
        project=selected_project,
        email=email_saved,
        text=text_saved
    )

if __name__ == "__main__":
    app.run(debug=True)
