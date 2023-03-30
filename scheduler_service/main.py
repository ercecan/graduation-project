# from typing import Dict, List

# from csp import CSP
# from data import course_list
# from models.constraints import (MajorConstraint, PrerequisitiesConstraint,
#                                 TimeSlotConstraint)
# from models.course import OpenedCourse
# from models.preferences import TimePreference
from models.student import Student
from models.major import Major
from models.course import Course
from enums.languages import Languages
# from preference_scorer import PreferenceScorer
from services.db_service import DBService
# from services.student_db_service import StudentDBService
from services.course_db_service import CourseDBService

# student_mock = Student(name="erce", surname="bekture", major=[Major(name="CMPE", code="BLG", language="EN")], 
#                        student_id="150180009", email="can18@itu.edu.tr", password="123", gpa="3.52", year=3, taken_courses=[])


# variables: List[OpenedCourse] = course_list
# domains: Dict[OpenedCourse, List[bool]] = {}
# for variable in variables:
#     domains[variable] = [True, False]
# csp: CSP[OpenedCourse, bool] = CSP(variables, domains)

# # csp.add_constraint(YearConstraint(variables))
# csp.add_constraint(MajorConstraint(variables))
# csp.add_constraint(TimeSlotConstraint(variables))
# csp.add_constraint(PrerequisitiesConstraint(variables))


# csp.backtracking_search()
# all_schedules = csp.get_all_possible_schedules()
# pref_scorer = PreferenceScorer(all_schedules)


# # pref_scorer.add_preference(DayPreference(1, Days.FRIDAY))
# # pref_scorer.add_preference(DayPreference(3, Days.TUESDAY))
# # pref_scorer.add_preference(DayPreference(5, Days.MONDAY))
# pref_scorer.add_preference(TimePreference(3, "13:00"))
# pref_scorer.add_preference(TimePreference(3, "09:00"))
# pref_scorer.add_preference(TimePreference(3, "12:00"))
# pref_scorer.add_preference(TimePreference(2, "10:00"))

# pref_scorer.scoring()
# pref_scorer.print_schedules()

# print_schedules()
# for schedule_and_score in schedule_and_scores:
#     print(schedule_and_score, "\n")


async def main():
    db = DBService()
    await db.init_database()
    studentm = Student(name="ercecan", surname="bekture", major=[Major(name="CMPE", code="BLG", language="English")], 
                       student_id="150180009", email="can18@itu.edu.tr", password="123", gpa="3.52", year=3, taken_courses=[])
    course3 = Course(name="C3", code="423", major_restrictions=["BLG"],crn="20203", ects=10, credits=4, language=Languages.ENGLISH, year_restrictions=[2, 3], prereqs=["421"])
    sb = CourseDBService()
    course = await sb.create_course(course3)
    # student = await sb.update_student(studentm, "641eebfabc338b811292511a")
    c = await sb.get_courses_by_ids(["6421e372d94bb2b9e50e7356"])
    print(c)

if __name__ == "__main__":
    try:
        import asyncio
        asyncio.run(main())
    except Exception as e:
        print(e)