from typing import Any, Dict, List

from models.preferences import Preference


class PreferenceScorer:
    def __init__(self, all_schedules: List[Any]) -> None:
        self.all_schedules = all_schedules
        self.preferences:List[Preference] = []

    def print_schedules(self):
        data = []
        self.all_schedules = sorted(self.all_schedules, key=lambda x: x[1])
        for (schedule, point) in self.all_schedules:
            sch = []
            for course in schedule:
                sch.append(course.course.name)
            sch.append(point)
            data.append(sch)

        with open("output.txt", "w") as file:
            for elements in data:
                file.write(str(elements) + "\n")

    def add_preference(self, preference: Preference):
        self.preferences.append(preference)

    def scoring(self): 
        for index, schedule in enumerate(self.all_schedules):
            score = 0
            for preference in self.preferences:
                score += preference.calculate_score(schedule[0])
            self.all_schedules[index] = (schedule[0], schedule[1] + score)
