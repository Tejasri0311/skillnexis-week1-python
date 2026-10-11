
def calculate_grade(average):
    if average >= 90:
        return "A Grade"
    elif average >= 80:
        return "B Grade"
    elif average >= 70:
        return "C Grade"
    elif average >= 60:
        return "D Grade"
    else:
        return "Fail"


def main():
    marks1 = float(input("Enter marks in Subject 1: "))
    marks2 = float(input("Enter marks in Subject 2: "))
    marks3 = float(input("Enter marks in Subject 3: "))

    average = (marks1 + marks2 + marks3) / 3

    grade = calculate_grade(average)

    print("Average Marks:", round(average, 2))
    print("Grade:", grade)


main()
