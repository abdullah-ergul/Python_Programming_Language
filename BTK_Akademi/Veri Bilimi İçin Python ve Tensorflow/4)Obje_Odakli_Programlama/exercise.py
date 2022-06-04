class Faculty():
    def __init__(self, faculty_name):
        self.faculty_name= faculty_name

    def info(self):
        print("Faculty Name:" + str(self.faculty_name))


class Department(Faculty):
    def __init__(self, department_name):
        Faculty.__init__(self, faculty_name= self.faculty_name)
        self.department_name= department_name

    def info(self):
        Faculty.info()
        print("Deaprtment Name:" + str(self.department_name))


class Lesson(Department):
    def __init__(self, prg_skill, eng_skill):
        self.prg_skill= prg_skill
        self.eng_skill= eng_skill

    def info(self):
        print("Faculty Name:" + str(self.faculty_name))



eng_fac= Faculty(str(input("Enter Faculty Name: ")))
eng_fac.info()
print("--------------")
cmp_eng= Department(str(input("Enter Department Name: ")))
