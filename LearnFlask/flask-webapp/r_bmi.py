from flask import Flask, render_template, request

app = Flask(__name__)

def calc_bmi(weight: float, height: float) -> float:
    return round(weight/((height / 100) ** 2), 2)

@app.route("/", methods=['GET','POST'])
def index():
    bmi = ''
    if request.method == "POST" and "weight" in request.form and "height" in request.form:
        weight = float(request.form.get("weight"))
        height = float(request.form.get("height"))
        bmi = calc_bmi(weight, height)
    return render_template("bmi_calc.html", bmi=bmi)

app.run(debug=True)