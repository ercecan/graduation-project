from typing import Dict, List

from csp import CSP
from data import course_list
from models.constraints import (MajorConstraint, PrerequisitiesConstraint,
                                TimeSlotConstraint)
from models.course import OpenedCourse
from models.preferences import TimePreference
from preference_scorer import PreferenceScorer

# student_mock = Student(name="erce", surname="bekture", major=[Major(name="CMPE", code="BLG", language="EN")], 
                    #    student_id="150180009", email="can18@itu.edu.tr", password="123", gpa="3.52", year=3, taken_courses=[])


variables: List[OpenedCourse] = course_list
domains: Dict[OpenedCourse, List[bool]] = {}
for variable in variables:
    domains[variable] = [True, False]
csp: CSP[OpenedCourse, bool] = CSP(variables, domains)

# csp.add_constraint(YearConstraint(variables))
csp.add_constraint(MajorConstraint(variables))
csp.add_constraint(TimeSlotConstraint(variables))
csp.add_constraint(PrerequisitiesConstraint(variables))


csp.backtracking_search()
all_schedules = csp.get_all_possible_schedules()
pref_scorer = PreferenceScorer(all_schedules)


# pref_scorer.add_preference(DayPreference(1, Days.FRIDAY))
# pref_scorer.add_preference(DayPreference(3, Days.TUESDAY))
# pref_scorer.add_preference(DayPreference(5, Days.MONDAY))
pref_scorer.add_preference(TimePreference(3, "13:00"))
pref_scorer.add_preference(TimePreference(3, "09:00"))
pref_scorer.add_preference(TimePreference(3, "12:00"))
pref_scorer.add_preference(TimePreference(2, "10:00"))

pref_scorer.scoring()
pref_scorer.print_schedules()

# print_schedules()
# for schedule_and_score in schedule_and_scores:
#     print(schedule_and_score, "\n")
