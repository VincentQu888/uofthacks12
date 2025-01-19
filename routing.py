from flask import Flask, render_template, request, redirect, session
from livereload import Server
from llm import teacher_generator_llm, student_generator_llm, pro_generator_llm

app = Flask(__name__)
app.debug = True  


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def generate():
    notes = request.form['notes-input']
    accidentals = request.form['accidentals-input']
    clef = request.form['clef-select']
    time = request.form['time-input']
    key = request.form['key-input']
    toggle_accidentals = True if request.form.get('toggle-accidentals', 'off') == 'on' else False
    toggle_perspective = True if request.form.get('toggle-perspective', 'off') == 'on' else False
    
    accidentalsPrompt = "random accidentals"
    if not toggle_accidentals:
        accidentalsPrompt = "no accidentals"
    prompt = fThere is a {clef} clef staff in {time} time signature with {accidentalsPrompt} that you cannot see. With this information make a list of questions about the staff. No images and no answers."

    return render_template(
        'index.html',
        notes = notes,
        accidentals = accidentals,
        clef = clef,
        time = time,
        key = key,
        toggle_accidentals = toggle_accidentals,
        toggle_perspective = toggle_perspective,
        teacher_questions = teacher_generator_llm(prompt) if toggle_perspective else "",
        student_questions = student_generator_llm(prompt) if toggle_perspective else "",
        pro_questions = pro_generator_llm(prompt) if toggle_perspective else ""
    )  


server = Server(app.wsgi_app)
server.watch("templates\index.html")
server.serve()
