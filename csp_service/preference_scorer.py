from typing import Any, Dict, List

from models.preferences import Preference


class PreferenceScorer:
    def __init__(self, all_schedules: List[Any]) -> None:
        self.all_schedules = all_schedules
        self.preferences:List[Preference] = []

    def print_schedules(self):
        for (schedule, point) in self.all_schedules:
            for course in schedule:
                print(course.name)
            print(point, "\n")

    def add_preference(self, preference: Preference):
        self.preferences.append(preference)

    def scoring(self): 
        for index, schedule in enumerate(self.all_schedules):
            score = 0
            for preference in self.preferences:
                score += preference.calculate_score(schedule[0])
            self.all_schedules[index] = (schedule[0], schedule[1] + score)
