class student:
    @staticmethod
    def pass_fail(mark):
        pass_marks=35
        if mark>=35:
            print("pass")
        else:
            print("fail")
s=student()
mark=int(input("enter the marks: "))
s.pass_fail(mark)
