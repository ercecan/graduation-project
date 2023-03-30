from abc import ABC, abstractmethod
from typing import Dict, Generic, List, Optional, TypeVar

from data import student_mock1, student_mock2
from models.student import Student

V = TypeVar('V') # variable type
D = TypeVar('D') # domain type
  
  
# Base class for all constraints
class Constraint(Generic[V, D], ABC):
    # The variables that the constraint is between
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    # Must be overridden by subclasses
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
         ...

  
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

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        self.constraints.append(constraint)

    # Check if the value assignment is consistent by checking all constraints
    # for the given variable against it
    def consistent(self, assignments: Dict[V, D], student: Student = student_mock1) -> bool:
        for constraint in self.constraints:
            if not constraint.satisfied({k: v for k, v in assignments.items() if v}, student):
                return False
        return True

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
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
            if self.consistent(local_assignment):
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
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