from typing import List
from dtos.course_dto import OpenedCourseDto
from models.course import Course, OpenedCourse
from models.time import Term, TimeSlot
from models.classroom import Classroom

def create_course_from_dto(opened_course: OpenedCourseDto) -> Course:
    course = Course(name=opened_course.name, code=opened_course.code, crn=opened_course.crn, ects=opened_course.ects,
                    credits=opened_course.credits, language=opened_course.language,
                    major_restrictions=opened_course.major_restrictions, prereqs=opened_course.prereqs,
                    year_restrictions=opened_course.year_restrictions, description=opened_course.description,
                    semester=opened_course.semester, recommended_semester=opened_course.recommended_semester,
                    instructor=opened_course.instructor, is_elective=opened_course.is_elective, tag=opened_course.tag)
    return course

def create_opened_course_from_dto(opened_course: OpenedCourseDto, course_id: str) -> OpenedCourse:
    term = Term(year=opened_course.term['year'], semester=opened_course.term['semester'])
    time_slot = []
    for time in opened_course.time:
        time_slot.append(TimeSlot(day=time['day'], start_time=time['start_time'], end_time=time['end_time']))
    
    classroom = None
    if opened_course.classroom:
        classroom = Classroom(name=opened_course.classroom['name'], building=opened_course.classroom['building'])
    opened_course = OpenedCourse(course_id=course_id, term=term, time_slot=time_slot, classroom=classroom,
                                 capacity=opened_course.capacity, teaching_method=opened_course.teaching_method)
    return opened_course