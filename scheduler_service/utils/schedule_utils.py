from typing import List, Any
from models.preferences import DayPreference, TimePreference, InstructorPreference
from models.constraints import MajorConstraint, TimeSlotConstraint, YearConstraint, CapacityConstraint, PrerequisitiesConstraint, CourseConstraint

def create_preferences(preferences: List[Any]):
    preferences_ = []
    for preference in preferences:
        if preference['type'] == 'day':
            preferences_.append(DayPreference(day=preference['value'], priority=preference['priority']))
        elif preference['type'] == 'time':
            preferences_.append(TimePreference(start_time=preference['value'], priority=preference['priority']))
        elif preference['type'] == 'instructor':
            preferences_.append(InstructorPreference(instructor=preference['value'], priority=preference['priority']))
    return preferences_

def get_ITU_constraints():
    return [MajorConstraint(), TimeSlotConstraint(), YearConstraint(), CourseConstraint(), PrerequisitiesConstraint(), CapacityConstraint()]