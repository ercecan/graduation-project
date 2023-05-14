from enums.semesters import Semesters

def next_semester(semester: Semesters) -> Semesters:
    if semester == Semesters.FALL.value:
        return Semesters.SPRING.value
    elif semester == Semesters.SPRING.value:
        return Semesters.FALL.value
    else:
        raise Exception("Invalid semester")