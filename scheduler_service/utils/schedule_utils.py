from typing import List, Any
from models.preferences import DayPreference, TimePreference, InstructorPreference
from models.constraints import MajorConstraint, TimeSlotConstraint, YearConstraint, CapacityConstraint, PrerequisitiesConstraint

def create_preferences(preferences: List[Any]):
    preferences = []
    for preference in preferences:
        if preference['type'] == 'day':
            preferences.append(DayPreference(day=preference['value'], priority=preference['priority']))
        elif preference['type'] == 'time':
            preferences.append(TimePreference(start_time=preference['value'], priority=preference['priority']))
        elif preference['type'] == 'instructor':
            preferences.append(InstructorPreference(instructor=preference['value'], priority=preference['priority']))
    return preferences

def get_ITU_constraints():
    return [MajorConstraint(), TimeSlotConstraint(), YearConstraint(), CapacityConstraint(), PrerequisitiesConstraint()]