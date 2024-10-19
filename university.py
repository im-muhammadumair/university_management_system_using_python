class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}(ID: {self.member_id}, Name: {self.name})"


class Student(Member):
    def __init__(self, student_id, name, program):
        super().__init__(student_id, name)
        self.program = program

    def __repr__(self):
        return f"Student(ID: {self.member_id}, Name: {self.name}, Program: {self.program})"


class Teacher(Member):
    def __init__(self, teacher_id, name, courses):
        super().__init__(teacher_id, name)
        self.courses = courses

    def __repr__(self):
        return f"Teacher(ID: {self.member_id}, Name: {self.name}, Courses: {self.courses})"


class Course:
    def __init__(self, course_id, course_name, program):
        self.course_id = course_id
        self.course_name = course_name
        self.program = program

    def __repr__(self):
        return f"Course(ID: {self.course_id}, Name: {self.course_name}, Program: {self.program})"


class Program:
    def __init__(self, program_id, program_name, sub_campus):
        self.program_id = program_id
        self.program_name = program_name
        self.sub_campus = sub_campus

    def __repr__(self):
        return f"Program(ID: {self.program_id}, Name: {self.program_name}, Sub-Campus: {self.sub_campus})"


class SubCampus:
    def __init__(self, sub_campus_id, sub_campus_name):
        self.sub_campus_id = sub_campus_id
        self.sub_campus_name = sub_campus_name

    def __repr__(self):
        return f"SubCampus(ID: {self.sub_campus_id}, Name: {self.sub_campus_name})"


class UniversityManagementSystem:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []
        self.programs = []
        self.sub_campuses = []

    def add_sub_campus(self, sub_campus_id, sub_campus_name):
        sub_campus = SubCampus(sub_campus_id, sub_campus_name)
        self.sub_campuses.append(sub_campus)
        print("Sub-Campus added:", sub_campus)

    def manage_students(self, action, student_id=None, name=None, program=None):
        if action == 'add':
            student = Student(student_id, name, program)
            self.students.append(student)
            print("Student added:", student)

        elif action == 'remove':
            self.students = [student for student in self.students if student.member_id != student_id]
            print(f"Student with ID {student_id} removed.")

        elif action == 'search':
            student = next((s for s in self.students if s.member_id == student_id), None)
            print("Searched Student:", student if student else "Student not found.")

        elif action == 'view_all':
            print("\n--- All Students ---")
            for student in self.students:
                print(student)

    def manage_teachers(self, action, teacher_id=None, name=None, courses=None):
        if action == 'add':
            teacher = Teacher(teacher_id, name, courses)
            self.teachers.append(teacher)
            print("Teacher added:", teacher)

        elif action == 'remove':
            self.teachers = [teacher for teacher in self.teachers if teacher.member_id != teacher_id]
            print(f"Teacher with ID {teacher_id} removed.")

        elif action == 'search':
            teacher = next((t for t in self.teachers if t.member_id == teacher_id), None)
            print("Searched Teacher:", teacher if teacher else "Teacher not found.")

        elif action == 'view_all':
            print("\n--- All Teachers ---")
            for teacher in self.teachers:
                print(teacher)

    def manage_courses(self, action, course_id=None, course_name=None, program=None):
        if action == 'add':
            course = Course(course_id, course_name, program)
            self.courses.append(course)
            print("Course added:", course)

        elif action == 'remove':
            self.courses = [course for course in self.courses if course.course_id != course_id]
            print(f"Course with ID {course_id} removed.")

        elif action == 'search':
            course = next((c for c in self.courses if c.course_id == course_id), None)
            print("Searched Course:", course if course else "Course not found.")

        elif action == 'view_all':
            print("\n--- All Courses ---")
            for course in self.courses:
                print(course)

    def manage_programs(self, action, program_id=None, program_name=None, sub_campus=None):
        if action == 'add':
            program = Program(program_id, program_name, sub_campus)
            self.programs.append(program)
            print("Program added:", program)

        elif action == 'remove':
            self.programs = [program for program in self.programs if program.program_id != program_id]
            print(f"Program with ID {program_id} removed.")

        elif action == 'search':
            program = next((p for p in self.programs if p.program_id == program_id), None)
            print("Searched Program:", program if program else "Program not found.")

        elif action == 'view_all':
            print("\n--- All Programs ---")
            for program in self.programs:
                print(program)

    def menu(self):
        while True:
            print("\n--- University Management System ---")
            print("1. Manage Students")
            print("2. Manage Teachers")
            print("3. Manage Courses")
            print("4. Manage Programs")
            print("5. Manage Sub-Campuses")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.manage_member('students')
            elif choice == '2':
                self.manage_member('teachers')
            elif choice == '3':
                self.manage_member('courses')
            elif choice == '4':
                self.manage_member('programs')
            elif choice == '5':
                self.manage_sub_campuses()
            elif choice == '6':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_member(self, member_type):
        while True:
            print(f"\n--- Manage {member_type.capitalize()} ---")
            print("1. Add")
            print("2. Remove")
            print("3. Search")
            print("4. View All")
            print("5. Back to Main Menu")
            action = input("Choose an action: ")

            if action == '1':
                if member_type == 'students':
                    student_id = input("Enter Student ID: ")
                    name = input("Enter Student Name: ")
                    program = input("Enter Student Program: ")
                    self.manage_students('add', student_id, name, program)
                elif member_type == 'teachers':
                    teacher_id = input("Enter Teacher ID: ")
                    name = input("Enter Teacher Name: ")
                    courses = input("Enter Teacher Courses (comma-separated): ").split(',')
                    self.manage_teachers('add', teacher_id, name, courses)
                elif member_type == 'courses':
                    course_id = input("Enter Course ID: ")
                    course_name = input("Enter Course Name: ")
                    program = input("Enter Course Program: ")
                    self.manage_courses('add', course_id, course_name, program)
                elif member_type == 'programs':
                    program_id = input("Enter Program ID: ")
                    program_name = input("Enter Program Name: ")
                    sub_campus = input("Enter Sub-Campus Name: ")
                    self.manage_programs('add', program_id, program_name, sub_campus)

            elif action == '2':
                if member_type == 'students':
                    student_id = input("Enter Student ID to remove: ")
                    self.manage_students('remove', student_id=student_id)
                elif member_type == 'teachers':
                    teacher_id = input("Enter Teacher ID to remove: ")
                    self.manage_teachers('remove', teacher_id=teacher_id)
                elif member_type == 'courses':
                    course_id = input("Enter Course ID to remove: ")
                    self.manage_courses('remove', course_id=course_id)
                elif member_type == 'programs':
                    program_id = input("Enter Program ID to remove: ")
                    self.manage_programs('remove', program_id=program_id)

            elif action == '3':
                if member_type == 'students':
                    student_id = input("Enter Student ID to search: ")
                    self.manage_students('search', student_id=student_id)
                elif member_type == 'teachers':
                    teacher_id = input("Enter Teacher ID to search: ")
                    self.manage_teachers('search', teacher_id=teacher_id)
                elif member_type == 'courses':
                    course_id = input("Enter Course ID to search: ")
                    self.manage_courses('search', course_id=course_id)
                elif member_type == 'programs':
                    program_id = input("Enter Program ID to search: ")
                    self.manage_programs('search', program_id=program_id)

            elif action == '4':
                if member_type == 'students':
                    self.manage_students('view_all')
                elif member_type == 'teachers':
                    self.manage_teachers('view_all')
                elif member_type == 'courses':
                    self.manage_courses('view_all')
                elif member_type == 'programs':
                    self.manage_programs('view_all')

            elif action == '5':
                break
            else:
                print("Invalid action. Please try again.")

    def manage_sub_campuses(self):
        while True:
            print("\n--- Manage Sub-Campuses ---")
            print("1. Add")
            print("2. Remove")
            print("3. View All")
            print("4. Back to Main Menu")
            action = input("Choose an action: ")

            if action == '1':
                sub_campus_id = input("Enter Sub-Campus ID: ")
                sub_campus_name = input("Enter Sub-Campus Name: ")
                self.add_sub_campus(sub_campus_id, sub_campus_name)

            elif action == '2':
                sub_campus_id = input("Enter Sub-Campus ID to remove: ")
                self.sub_campuses = [sc for sc in self.sub_campuses if sc.sub_campus_id != sub_campus_id]
                print(f"Sub-Campus with ID {sub_campus_id} removed.")

            elif action == '3':
                print("\n--- All Sub-Campuses ---")
                for sc in self.sub_campuses:
                    print(sc)

            elif action == '4':
                break
            else:
                print("Invalid action. Please try again.")


if __name__ == "__main__":
    ums = UniversityManagementSystem()
    ums.menu()