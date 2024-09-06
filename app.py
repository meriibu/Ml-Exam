from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

questions = [
    {
        'question': "Python programlama dilinde yapay zeka geliştirmek için kullanılan temel veri yapısı hangisidir?",
        'options': ['a) String', 'b) List', 'c) Tuple', 'd) Set'],
        'answer': 'b) List'
    },
    {
        'question': "Python'da AI geliştirmek için hangi dosya formatı yaygın olarak veri saklamak için kullanılır?",
        'options': ['a) .txt', 'b) .csv', 'c) .docx', 'd) .html'],
        'answer': 'b) .csv'
    },
    {
        'question': "Python'da matematiksel işlemler yapmak için hangi kütüphane kullanılır?",
        'options': ['a) NumPy', 'b) Flask', 'c) BeautifulSoup', 'd) Requests'],
        'answer': 'a) NumPy'
    },
    {
        'question': "Python'da veri görselleştirme için hangi kütüphane kullanılır?",
        'options': ['a) Matplotlib', 'b) Django', 'c) Selenium', 'd) Pillow'],
        'answer': 'a) Matplotlib'
    },
    {
        'question': "Python'da AI geliştirmek için veri setlerini yüklemek ve işlemek için kullanılan popüler bir kütüphane nedir?",
        'options': ['a) Pandas', 'b) Flask', 'c) Selenium', 'd) Pillow'],
        'answer': 'a) Pandas'
    }
]

high_scores = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        session['score'] = 0
        session['responses'] = []
        return redirect(url_for('question', q=0))

    return render_template('quiz.html')

@app.route('/question/<int:q>', methods=['GET', 'POST'])
def question(q):
    if q >= len(questions):
        return redirect(url_for('result'))

    if request.method == 'POST':
        answer = request.form['answer']
        session['responses'].append(answer)
        if answer == questions[q]['answer']:
            session['score'] += 20
        return redirect(url_for('question', q=q+1))

    return render_template('question.html', question=questions[q], q=q)

@app.route('/result')
def result():
    score = session['score']
    high_scores.append(score)
    high_scores.sort(reverse=True)
    top_score = high_scores[0] if high_scores else 0
    return render_template('result.html', score=score, top_score=top_score)

if __name__ == '__main__':
    app.run(debug=True)
