from typing import Dict, List

from csp import CSP, Constraint
from enums.days import Days
from enums.languages import Languages
from models.constraints import (MajorConstraint, PrerequisitiesConstraint,
                                TimeSlotConstraint, YearConstraint)
from models.course import OpenedCourse
from models.major import Major
from models.preferences import DayPreference
from models.schedule import Schedule
from models.student import Student
from models.time import Term, TimeSlot
from preference_scorer import PreferenceScorer

ts1 = TimeSlot(day=Days.MONDAY, start_time="9:00", end_time="12:00")
ts3 = TimeSlot(day=Days.TUESDAY, start_time="8:30", end_time="11:30")
ts31 = TimeSlot(day=Days.TUESDAY, start_time="10:30", end_time="12:30")
ts4 = TimeSlot(day=Days.TUESDAY, start_time="13:00", end_time="16:00")
ts5 = TimeSlot(day=Days.WEDNESDAY, start_time="9:00", end_time="12:00")
ts6 = TimeSlot(day=Days.WEDNESDAY, start_time="13:00", end_time="16:00")
ts32 = TimeSlot(day=Days.WEDNESDAY, start_time="13:30", end_time="15:00")


courseFP = OpenedCourse(name="FP", code="425", major_restrictions=["BLG"], crn="20201", ects=10, credits=4,
                         language=Languages.TURKISH, year_restrictions=[2, 3], time_slot=[ts1, ts3])

courseAI = OpenedCourse(name="AI", code="432", major_restrictions=["BLG"],crn="20200", ects=8, credits=3, 
                        language=Languages.ENGLISH, year_restrictions=[3, 4], time_slot= [ts31])

courseOOMD = OpenedCourse(name="OOMD", code="420", major_restrictions=["BLG"],crn="20203", ects=10, credits=4, 
                          language=Languages.ENGLISH, year_restrictions=[3, 4], time_slot=[ts4], prereqs=["418"])

course_list = [courseOOMD, courseAI, courseFP]




variables: List[OpenedCourse] = course_list
domains: Dict[OpenedCourse, List[bool]] = {}
for variable in variables:
    domains[variable] = [True, False]
csp: CSP[OpenedCourse, bool] = CSP(variables, domains)

# csp.add_constraint(YearConstraint(variables))
# csp.add_constraint(MajorConstraint(variables))
# csp.add_constraint(TimeSlotConstraint(variables))
csp.add_constraint(PrerequisitiesConstraint(variables))


csp.backtracking_search()
all_schedules = csp.get_all_possible_schedules()
pref_scorer = PreferenceScorer(all_schedules)


pref_scorer.add_preference(DayPreference(3, Days.FRIDAY))
pref_scorer.add_preference(DayPreference(2, Days.TUESDAY))
pref_scorer.add_preference(DayPreference(1, Days.MONDAY))
pref_scorer.scoring()
pref_scorer.print_schedules()

# print_schedules()
# for schedule_and_score in schedule_and_scores:
#     print(schedule_and_score, "\n")
