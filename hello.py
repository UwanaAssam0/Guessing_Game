def collect_courses():
    grades = []
    no_of_courses = int(input("How many courses do you offer?: "))
    print()
    for i in range(no_of_courses):
        print(f"Course {i + 1}: ")
        course_code = input(" Enter Course Code: ")
        exam_score = float(input(" Enter Exam Score (0-70): "))
        test_score = float(input(" Enter Test Score (0-30): "))
        credit_unit = int(input(" What's the credit unit for the course?: "))

        total_score = exam_score + test_score
        grades.append({
            "course_code": course_code,
            "score": total_score,
            "credit_unit": credit_unit
        })
        print()
    return grades


def calculate_grade_point(score):
    if score >= 70:
        return 5
    elif score >= 60:
        return 4
    elif score >= 50:
        return 3
    elif score >= 45:
        return 2
    elif score >= 40:
        return 1
    else:
        return 0


def calculate_cgpa(grades, prev_cgpa=0.0, prev_credits=0):
    total_quality_points = 0
    total_credits = 0

    for course in grades:
        gp = calculate_grade_point(course['score'])
        credit = course['credit_unit']
        total_quality_points += gp * credit
        total_credits += credit

    # Add previous CGPA contribution if any
    if prev_credits > 0:
        total_quality_points += prev_cgpa * prev_credits
        total_credits += prev_credits

    if total_credits == 0:
        return 0.0

    return round(total_quality_points / total_credits, 2)


def feedback(grades):
    remarks = []
    for course in grades:
        score = course['score']
        course_code = course['course_code']
        if score >= 70:
            remarks.append(f"{course_code}: Excellent 👏")
        elif score >= 60:
            remarks.append(f"{course_code}: Very Good 👍")
        elif score >= 50:
            remarks.append(f"{course_code}: Good 🙂")
        elif score >= 45:
            remarks.append(f"{course_code}: Fair 😐")
        elif score >= 40:
            remarks.append(f"{course_code}: Pass 🫤")
        else:
            remarks.append(f"{course_code}: Fail ❌ - Needs serious improvement!")

    return "\n".join(remarks)


def main():
    name = input("What is your name?: ") 
    print(f"\nHello {name}. Welcome to A+ VIBES! 😀")
    print("Where you can confidently forecast your CGPA eventually making you an excellent student! 🤩\n")

    grades = collect_courses()

    prev_cgpa_input = input("Enter previous CGPA (or leave blank): ")
    prev_cgpa = float(prev_cgpa_input) if prev_cgpa_input else 0.0

    prev_credits_input = input("Enter previous total credit units (or leave blank): ")
    prev_credits = int(prev_credits_input) if prev_credits_input else 0

    cgpa = calculate_cgpa(grades, prev_cgpa=prev_cgpa, prev_credits=prev_credits)
    print(f"\n{name}, your current CGPA is: {cgpa}")
    print("\nOur honest review and suggestions are as follows:")
    print(feedback(grades))


if __name__ == "__main__":
    main()
