def average(marks):
    return sum(marks) / len(marks)


def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B+"
    elif avg >= 60:
        return "B"
    else:
        return "F"


def is_pass(marks):
    return all(mark >= 40 for mark in marks)


marks = []
n = int(input("Enter Number of Subjects: "))

if n <= 0:
    print("Number of subjects must be greater than 0.")
else:
    for i in range(1, n + 1):
        score = float(input(f"Enter marks for subject {i}: "))
        marks.append(score)

    avg = average(marks)
    status = "PASS" if is_pass(marks) else "FAIL"

    print("\n--- Result Summary ---")
    print(f"Marks:          {marks}")
    print(f"Average:        {avg:.2f}")
    print(f"Grade:          {grade(avg)}")
    print(f"Status:         {status}")
    print(f"Highest Mark:   {max(marks)}")
    print(f"Lowest Mark:    {min(marks)}")