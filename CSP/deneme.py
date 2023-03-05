from typing import Dict, List

from csp import CSP, Constraint
from enums.languages import Languages
from enums.days import Days
from models.constraints import MajorConstraint, YearConstraint, TimeSlotConstraint, PrerequisitiesConstraint
from models.course import OpenedCourse
from models.major import Major
from models.student import Student
from models.time import Term, TimeSlot

ts1 = TimeSlot(day=Days.MONDAY, start_time="9:00", end_time="12:00")
ts3 = TimeSlot(day=Days.TUESDAY, start_time="8:30", end_time="11:30")
ts31 = TimeSlot(day=Days.TUESDAY, start_time="10:30", end_time="12:30")
ts4 = TimeSlot(day=Days.TUESDAY, start_time="13:00", end_time="16:00")
ts5 = TimeSlot(day=Days.WEDNESDAY, start_time="9:00", end_time="12:00")
ts6 = TimeSlot(day=Days.WEDNESDAY, start_time="13:00", end_time="16:00")
ts32 = TimeSlot(day=Days.WEDNESDAY, start_time="13:30", end_time="15:00")


# courseFP = OpenedCourse(name="FP", code="425", major_restrictions=["BLG"], crn="20201", ects=10, credits=4, language=Languages.TURKISH, year_restrictions=[2, 3], time_slot=[ts1])
courseAI = OpenedCourse(name="AI", code="432", major_restrictions=["BLG"],crn="20200", ects=8, credits=3, language=Languages.ENGLISH, year_restrictions=[3, 4], time_slot= [ts31])
courseOOMD = OpenedCourse(name="OOMD", code="420", major_restrictions=["BLG"],crn="20203", ects=10, credits=4, language=Languages.ENGLISH, year_restrictions=[3, 4], time_slot=[ts4], prereqs=["418"])

course_list = [courseOOMD, courseAI]

class DenemeConstraint(Constraint[str, str]):
    def __init__(self, place1: str, place2: str) -> None:
        super().__init__([place1, place2])
        self.place1: str = place1
        self.place2: str = place2

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        # If either place is not in the assignment then it is not
        # yet possible for their colors to be conflicting
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        # check the color assigned to place1 is not the same as the
        # color assigned to place2
        return assignment[self.place1] != assignment[self.place2]


if __name__ == "__main__":
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
if len(csp.answer) == 0:
    print("No solution found!")
else:
    for ans in csp.answer:
        for key, value in ans.items():
            print(key.name, value)
        print("\n")