from enums.semesters import Semesters

def next_semester(semester: Semesters) -> Semesters:
    if semester == Semesters.FALL:
        return Semesters.SPRING
    elif semester == Semesters.SPRING:
        return Semesters.FALL
    else:
        raise Exception("Invalid semester")