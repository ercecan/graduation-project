import pypdf
import re


def get_lines(pdf_path):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = pypdf.PdfReader(pdf_file)
    pages = pdf_reader.pages
    all_lines = []
    for page in pages:
        page_text = page.extract_text()
        lines = page_text.split('\n')
        all_lines += lines
    return all_lines

def extract_courses(pdf_path):
    all_lines = get_lines(pdf_path)
    courses_by_term = {} #term: courses

    term_pattern = r'\d{4}-\d{4} (?:Yaz Okulu|Güz Dönemi|Bahar Dönemi)'
    course_pattern = r'[A-Z]{3}\s?\d{3,4}\s?[A-Z]{0,2}?\s[\w\s&\']+'      
    is_course = False  
    for idx, line in enumerate(all_lines):
        course = {'code': '', 'name': '', 'letter_grade': ''}
       
        if re.match(term_pattern, line):
            # start term
            term = line.split(' ')[0] + ' ' + line.split()[1]
            term = term.replace('Bahar', 'spring')
            term = term.replace('Güz', 'fall')
            term = term.replace('Yaz', 'summer')
            sem = term.split()[1]
            if sem == 'fall':
                term = term[0:4] + ' ' + term.split()[1]
            else:
                term = term[5:9] + ' ' + term.split()[1]
            #term = line
            courses_by_term[term] = []
        
        if line == '(Comment)':
            # start adding courses
            is_course = True
            continue
        if line == 'DNO:':
            # end term
            is_course = False
        if is_course:
            if not line.startswith('('):
                if not re.match(course_pattern, line):
                    continue
                splitted = line.split()
                course['code'] = ' '.join(splitted[0:2])
                course['name'] = ' '.join(line.split()[2:])
                course['letter_grade'] = all_lines[idx + 1].split()[-2]
                courses_by_term[term].append(course)

        
    return courses_by_term

#Example usage
# pdf_path = '/Users/erce/Desktop/ITU/Graduation Project/graduation-project/user_service/1syf_Transkript.pdf'

# extracted_courses = extract_courses(pdf_path)
# print(extracted_courses)
