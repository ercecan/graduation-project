from enums.days import Days
from enums.grades import Grades
from enums.languages import Languages
from enums.semesters import Semesters
from models.course import Course, OpenedCourse, TakenCourse
from models.major import Major
from models.student import Student
from models.time import Term, TimeSlot

ts11 = TimeSlot(day=Days.MONDAY, start_time="9:00", end_time="12:00")
ts12 = TimeSlot(day=Days.MONDAY, start_time="13:00", end_time="15:00")
ts21 = TimeSlot(day=Days.TUESDAY, start_time="8:30", end_time="11:30")
ts22 = TimeSlot(day=Days.TUESDAY, start_time="10:30", end_time="12:30")
ts23 = TimeSlot(day=Days.TUESDAY, start_time="13:00", end_time="16:00")
ts31 = TimeSlot(day=Days.WEDNESDAY, start_time="9:00", end_time="12:00")
ts32 = TimeSlot(day=Days.WEDNESDAY, start_time="13:00", end_time="16:00")
ts41 = TimeSlot(day=Days.THURSDAY, start_time="10:30", end_time="13:00")
ts42 = TimeSlot(day=Days.THURSDAY, start_time="13:30", end_time="15:30")
ts51 = TimeSlot(day=Days.FRIDAY, start_time="09:30", end_time="12:00")
ts52 = TimeSlot(day=Days.FRIDAY, start_time="12:30", end_time="16:30")



course1 = Course(name="C1", code="421", major_restrictions=["BLG"], crn="20201", ects=10, credits=4, language=Languages.TURKISH, year_restrictions=[2, 4])
course2 = Course(name="C2", code="422", major_restrictions=["BLG"],crn="20202", ects=8, credits=3, language=Languages.ENGLISH, year_restrictions=[2, 3])
course3 = Course(name="C3", code="423", major_restrictions=["BLG"],crn="20203", ects=10, credits=4, language=Languages.ENGLISH, year_restrictions=[2, 3], prereqs=["421"])
course4 = Course(name="C4", code="424", major_restrictions=["BLG"],crn="20204", ects=4, credits=2, language=Languages.ENGLISH, year_restrictions=[1, 2], prereqs=["423"])
course5 = Course(name="C5", code="425", major_restrictions=["BLG"], crn="20205", ects=14, credits=6, language=Languages.TURKISH, year_restrictions=[3, 4])
course6 = Course(name="C6", code="426", major_restrictions=["BLG"],crn="20206", ects=6, credits=3, language=Languages.ENGLISH, year_restrictions=[2, 3, 4])
course7 = Course(name="C7", code="427", major_restrictions=["YZV"],crn="20207", ects=2, credits=1, language=Languages.ENGLISH, year_restrictions=[3, 4], prereqs=["423"])
course8 = Course(name="C8", code="428", major_restrictions=["BLG"],crn="20208", ects=4, credits=2, language=Languages.ENGLISH, year_restrictions=[3, 4], prereqs=["421"])

opened_course1 = OpenedCourse(course=course1, time_slot=[ts11, ts31])
opened_course2 = OpenedCourse(course=course2, time_slot=[ts31, ts51])
opened_course3 = OpenedCourse(course=course3, time_slot=[ts41, ts52])
course4 = OpenedCourse(course=course4, time_slot=[ts31])
course5 = OpenedCourse(course=course5, time_slot=[ts12, ts22])
course6 = OpenedCourse(course=course6, time_slot=[ts41])
course7 = OpenedCourse(course=course7, time_slot=[ts31])
course8 = OpenedCourse(course=course8, time_slot=[ts32, ts51])

term1=Term(semester = Semesters.SPRING,year = 3)
term2=Term(semester = Semesters.ALL,year = 2)
term3=Term(semester = Semesters.FALL,year = 4)

taken_course1 = TakenCourse(course=course1, grade=Grades.CB, term=term1)
taken_course2 = TakenCourse(course=course2, grade=Grades.CB, term=term2)
taken_course3 = TakenCourse(course=course3, grade=Grades.CB, term=term3)

course_list = [opened_course1, opened_course2, opened_course3]

## Student

student_mock1 = Student(name="erce", surname="bekture", major=[Major(name="CMPE", code="BLG", language="EN")], student_id="150180009", email="can18@itu.edu.tr", password="123", gpa="3.52", year=3, taken_courses=[taken_course1])
student_mock2 = Student(name="ömer", surname="özkan", major=[Major(name="CMPE", code="BLG", language="EN")], student_id="150180007", email="ozkan18@itu.edu.tr", password="123", gpa="3.72", year=3, taken_courses=[taken_course2, taken_course3])
