# global result
print('Student Dictionary Input')
s_name = input("Enter Student Name: ")

print("Enter student Marks in following subject: ")
S_marks_maths = float(input("Maths:"))
S_marks_english = float(input("English:"))
S_marks_hindi = float(input("Hindi:"))
S_marks_sst: float = float(input("Social Science:"))
S_marks_science = float(input("Science:"))

print("Enter student assignment number in following subject: ")
S_ass_maths = float(input("Maths:"))
S_ass_english = float(input("English:"))
S_ass_hindi = float(input("Hindi:"))
S_ass_sst = float(input("Social Science:"))
S_ass_science = float(input("Science:"))

print(" Enter marks obtain in lab: ")
S_lab_maths = float(input("Maths:"))
S_lab_science = float(input("Science:"))


def avg_marks():
    marks = (S_marks_maths + S_marks_english + S_marks_hindi + S_marks_sst + S_marks_science) / 5
    assignment = (S_ass_maths + S_ass_english + S_ass_hindi + S_ass_sst + S_ass_science) / 5
    lab = (S_lab_maths + S_lab_science) / 2
    result = (0.7 * marks) + (0.1 * assignment) + (0.2 * lab)
    print("Total Marks percentage by", s_name, "is ", result, "%")
    if result >= 90:
       print ("you scored  A grade")
    elif result >= 80:
        print ("you scored B grade")
    elif result >= 70:
       print ("you scored C grade")
    elif result >= 60:
       print ("you scored D grade")
    else:
       print ("you scored E grade")




total_result = avg_marks()
