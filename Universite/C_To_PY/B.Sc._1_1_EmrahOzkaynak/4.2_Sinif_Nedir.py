class Student():
    def __init__(self, no, name, sname, mexam, fexam):
        self.no = str(no)
        self.name = name
        self.sname = sname
        self.mexam = str(mexam)
        self.fexam = str(fexam)
        self.grade = float(mexam)*0.4 + float(fexam)*0.6

def choose():
    print("1 for Create a File")
    print("2 for List File")
    print("3 for List Success Students (Get Greater Than 50)")
    print("4 for Make Files for Pass or Fail Students")
    print("5 for Print File's Size")
    print("0 for Exit The Program")
    return int(input("\nYour choice: "))

def mk_file():
    with open("data.txt", "w", encoding="utf-8") as file:
        no= input("Enter Student's Number: ")
        while (no != 0):
            name, sname, mexam, fexam = input("Enter Student's Information: ").split()
            ogrenci = Student(no, name, sname, mexam, fexam)
            file.write(ogrenci.no + " " + ogrenci.name + " " + ogrenci.sname + " " + ogrenci.mexam + " " + ogrenci.fexam + " " + str(ogrenci.grade) + "\n")
            no= input("Enter Student's Number: ")

def ls_file():
    with open("data.txt", "r", encoding="utf-8") as file:
        for i in file:
            print(i,end=(""))

def ls_success():
    with open("data.txt", "r", encoding="utf-8") as file:
        for i in file:
            list1= i.split()
            if float(list1[5]) > 50:
                print(i,end=(""))


choice= choose()
while(1):
    if choice == 1:
        mk_file()
    elif choice == 2:
        ls_file()
    elif choice == 3:
        ls_success()
    elif choice == 0:
        break
    else:
        print("Your  is Not Found! Please Give a Diffrent Number.")
    print("\n--------------------------------\n")
    choice = choose()
