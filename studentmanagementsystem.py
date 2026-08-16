class Student:
    def __init__(self,name,grade,marks,section,regdno):
        self.name = name
        self.grade = grade
        self.marks = marks
        self.section = section
        self.regdno = regdno


    
    def result(self):
    # Decide grade and GPA
        if self.marks >= 95:
            alpha = "A"
            gpa = 4.0
        elif self.marks >= 60:
            alpha = "B"
            gpa = 3.0
        elif self.marks >= 40:
            alpha = "C"
            gpa = 2.0
        elif self.marks >= 30:
            alpha = "D"
            gpa = 1.0
        else:
            alpha = "F"
            gpa = 0.0

# Decide remark based on GPA
        if gpa == 4.0:
            remark = "Outstanding"
        elif gpa == 3.0:
            remark = "Good"
        elif gpa == 2.0:
            remark = "Average"
        elif gpa == 1.0:
            remark = "Below Average"
        else:
            remark = "Fail"

        # Print the full result
        print(f"Marks: {self.marks}")
        print(f"Grade: {alpha}")
        print(f"GPA: {gpa}")
        print(f"Remark: {remark}\n")
        print("--------------------")


        
    def show_info(self):
        print(f"The name of the student is: {self.name}\nThe class is: {self.grade}\nThe section is: {self.section}\nThe registration number is: {self.regdno}\n")

class Classroom:
    def __init__(self):
        self.students = []   # list to store student objects

    def show_all(self):
        if not self.students:
            print("No students in classroom.")
        else:
            print("\n--- Classroom Students ---")
            for s in self.students:
                s.show_info()


# Example usage
a1 = Student("Sandip Neupane", "9", 95, "GLS", "7793")
a1.show_info()
a1.result()
a2 = Student("Sadish Adhikari", "9", 90, "DBM", "5024")
a2.show_info()
a2.result()

classroom = Classroom()

# Directly append student objects without add_student function
classroom.students.append(a1)
classroom.students.append(a2)

# Show all students
classroom.show_all()