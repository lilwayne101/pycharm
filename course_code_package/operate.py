from course_code_package.class_stu import Class
from course_code_package.teacher import Teacher
from course_code_package.student import Student

class Operate:

    def max_salary(self, teacher_list):
        salary_list = [teacher_list[i].salary for i in range(len(teacher_list))]
        return max(salary_list)

    def mean_salary(self, teacher_list):
        salary_list = [teacher_list[i].salary for i in range(len(teacher_list))]
        return sum(salary_list) / len(salary_list)

    def min_salary(self, teacher_list):
        salary_list = [teacher_list[i].salary for i in range(len(teacher_list))]
        return min(salary_list)

    def show_teacher(self, teacher_list):
        for teacher in teacher_list:
            print(f"\n{teacher.name}教:", end='')
            for sub in teacher.t_sub:
                print(f"{sub}", end='\t')
            print(f"\n{teacher.name}带:", end='')
            for c in teacher.c_list:
                print(f"{c}", end='\t')

    def stu_teacher(self, student_list, teacher_list):
        print()
        for stu in student_list:
            for sub in list(stu.sub_score.keys()):
                for thr in teacher_list:
                    if sub == thr.t_sub and stu.stu_class in thr.c_list:
                        print(f"{stu.name}的{sub}科目的老师为{thr.name}")

    def mean_score_stu(self, student_list):
        for stu in student_list:
            score_list = list(stu.sub_score.values())
            print(f"{stu.name}的平均分为{round(sum(score_list) / len(stu.sub_score), 2)}")

    def good_at_sub(self, student_list):
        for stu in student_list:
            score_list = list(stu.sub_score.values())
            index = score_list.index(max(score_list))
            sub = list(stu.sub_score.keys())[index]
            print(f"{stu.name}最擅长的科目是：{sub}")

    def create_class_list(self, class_data):
        class_list = []
        for key, value in class_data.items():
            class_list.append(
                eval(f"Class('{key}',[Student('{value[0][0]}','{value[0][1]}','{value[0][2]}',{value[0][3]}),Student('{value[1][0]}','{value[1][1]}','{value[1][2]}',{value[1][3]})])"))
        return class_list

    def create_student_list(self, student_data):
        student_list_temp = []
        for stu in student_data:
            student_list_temp.append(
                eval(f"Student('{stu[0]}','{stu[1]}','{stu[2]}',{stu[3]})"))
        return student_list_temp

    def create_teacher_list(self, teacher_data):
        teacher_list_temp = []
        for thr in teacher_data:
            teacher_list_temp.append(
                eval(f"Teacher('{thr[0]}',{thr[1]},'{thr[2]}',{thr[3]})"))
        return teacher_list_temp
