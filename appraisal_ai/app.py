from flask import Flask, render_template, request, redirect
from database import init_db, insert_employee, get_all
from ai_generator import generate_ai_employee, calculate_score

app = Flask(__name__)

init_db()

# ==============================
# AUTO INSERT 3 AI EMPLOYEES
# ==============================

def seed_data():
    employees = [
        generate_ai_employee("Hifza Toufiq"),
        generate_ai_employee("Ali Khan"),
        generate_ai_employee("Sara Ahmed")
    ]
    for emp in employees:
        insert_employee(emp)

# run once
seed_data()



# ==============================
# HOME
# ==============================

@app.route("/")
def home():
    records = get_all()
    return render_template("records.html", records=records)


# ==============================
# NEW APPRAISAL FORM
# ==============================

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        working = float(request.form["working"])
        present = float(request.form["present"])
        leave = float(request.form["leave"])
        performance = float(request.form["performance"])

        punctuality, regularity, total, rating = calculate_score(
            working, present, leave, performance
        )

        insert_employee((
            name, working, present, leave,
            punctuality, regularity,
            performance, total, rating
        ))

        return render_template("result.html",
                               name=name,
                               total=total,
                               rating=rating)

    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)