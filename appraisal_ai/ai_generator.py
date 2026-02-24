import random


def calculate_score(working_days, present, leave, performance):
    attendance = (present / working_days) * 100
    punctuality = round((attendance / 100) * 10, 2)
    regularity = round(((present - leave) / working_days) * 10, 2)
    total = round(punctuality + regularity + performance, 2)

    if total >= 90:
        rating = "Excellent"
    elif total >= 75:
        rating = "Very Good"
    elif total >= 60:
        rating = "Good"
    else:
        rating = "Needs Improvement"

    return punctuality, regularity, total, rating


def generate_ai_employee(name):
    working_days = random.randint(140, 180)
    present = random.randint(120, working_days)
    leave = random.randint(0, 10)
    performance = round(random.uniform(50, 80), 2)

    punctuality, regularity, total, rating = calculate_score(
        working_days, present, leave, performance
    )

    return (
        name,
        working_days,
        present,
        leave,
        punctuality,
        regularity,
        performance,
        total,
        rating
    )
