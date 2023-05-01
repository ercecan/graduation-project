from abc import ABC, abstractmethod
from typing import Dict, Generic, List, Optional, TypeVar
from models.constraints import Constraint
from dtos.student_dto import StudentSearchDto

V = TypeVar('V') # variable type
D = TypeVar('D') # domain type
  
# A constraint satisfaction problem consists of variables of type V
# that have ranges of values known as domains of type D and constraints
# that determine whether a particular variable's domain selection is valid
class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = variables # variables to be constrained
        self.domains: Dict[V, List[D]] = domains # domain of each variable
        self.constraints: List[Constraint[V, D]]
        self.answer = []
        self.constraints = []

        for variable in self.variables:
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it.")

    def add_constraint(self, constraint: Constraint) -> None:
        self.constraints.append(constraint)

    # Check if the value assignment is consistent by checking all constraints
    # for the given variable against it
    def consistent(self, assignments: Dict[V, D], student: StudentSearchDto) -> bool:
        for constraint in self.constraints:
            if not constraint.satisfied({k: v for k, v in assignments.items() if v}, student):
                return False
        return True

    def backtracking_search(self, student: StudentSearchDto, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        # assignment is complete if every variable is assigned (our base case)
        if len(assignment) == len(self.variables):
            return assignment

        # get all variables in the CSP but not in the assignment
        unassigned: List[V] = [v for v in self.variables if v not in assignment]

        # get the every possible domain value of the first unassigned variable
        first: V = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            # if we're still consistent, we recurse (continue)
            if self.consistent(local_assignment, student=student):
                result: Optional[Dict[V, D]] = self.backtracking_search(student, local_assignment)
                # if we didn't find the result, we will end up backtracking
                if result is not None:
                    self.answer.append(result) 
        return None

    def get_all_possible_schedules(self):
        all_schedules = []
        if len(self.answer) == 0:
            print("No solution found!") # Exception
        else:
            for ans in self.answer:
                schedule = []
                for course in ans:
                    if ans[course] == True:
                        schedule.append(course)
                all_schedules.append((schedule, 0))
        return all_schedules