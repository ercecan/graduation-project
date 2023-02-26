from typing import Dict, List, Optional

from enums.languages import Languages
from models.constraints import MajorConstraint, YearConstraint
from models.course import OpenedCourse
from models.major import Major
from models.student import Student
from models.time import Term, TimeSlot

from CSP.csp import CSP, Constraint

courseFP = OpenedCourse(name="FP", code="425", major_restrictions=["BLG"], crn="20201", ects=10, credits=4, language=Languages.TURKISH, year_restrictions=[2, 3])
courseOOP = OpenedCourse(name="OOP", code="418", major_restrictions=["BLG"],crn="20202", ects=12, credits=5, language=Languages.ENGLISH, year_restrictions=[1, 2])
courseAI = OpenedCourse(name="AI", code="432", major_restrictions=["YZV"],crn="20200", ects=8, credits=3, language=Languages.ENGLISH, year_restrictions=[3, 4])


course_list = [courseFP, courseOOP, courseAI]


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

    csp.add_constraint(YearConstraint(variables))
    csp.add_constraint(MajorConstraint(variables))


csp.backtracking_search()
if len(csp.answer) == 0:
    print("No solution found!")
else:
    for ans in csp.answer:
        print(ans, 3*"\n")