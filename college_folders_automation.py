import os

# Default directory
directory = "C:\\Users\\macie\\Desktop"

# Folder names
course_name = "HND Software Development"
year_one = "Year 1"
year_two = "Year 2"
semester_one = "Semester 1"
semester_two = "Semester 2"

# List of all the units for semester 1
semester1_modules = ["H1F734 - Professionalism and Ethics in Computing",
           "H1W034 - Project Management for IT",
           "H17X34 - Software Development - Programming Foundations",
           "H17334 - Developing Software - Introduction",
           "H17135 - Software Development OOP",
           "H17534 - Computer System Fundamentals",
           "H17734 - Troubleshooting Computer Problems"]

# List of all the units for semester 2
semester2_modules = ["DH3J34 - SQL Introduction",
           "H1J834 - Graded Unit 1",
           "H17R35 - Mobile Technologies",
           "H17Y34 - Software Development - Systems Foundations",
           "H17135 - Software Development OOP",
           "H17834 - Teamworking in Computing",
           "H18034 - Systems Development Introduction"]


def create_directories(course, year, semester, modules):

    """
    Creates folders for each module in each semester along with folders for Assessments, Resources and each week of the semester
    """

    # Change working director to Year folder
    os.chdir(f"{directory}\\{course}\\{year}")

    # The course is split in to two semesters. Create a folder for each semester
    os.makedirs(semester)

    # Changes working directory to Semester
    os.chdir(f"{directory}\\{course}\\{year}\\{semester}")

    # Creates a folder for each module in the module list passed
    for module in modules:
        os.makedirs(module)

    # For each module, change directory to the module folder. Create an assessments folder, resources folder and folders ranging from week 1 to 12
    for module in modules:
        os.chdir(f"{directory}\\{course}\\{year}\\{semester}\\" + module)
        os.makedirs("Assessments")
        os.makedirs("Resources")
        for i in range(1, 13):
            if i <= 9:
                os.makedirs(f"Week0{i}")
            else:
                os.makedirs(f"Week{i}")


# Change working directory to desktop
os.chdir(directory)

# Create a folder named after the course
os.makedirs(course_name)

# Change directory to folder named after the course
os.chdir(f"{directory}\\{course_name}")

# It is a two year course, creates a folder for each year
os.makedirs(year_one)
os.makedirs(year_two)

create_directories(course_name, year_one, semester_one, semester1_modules)
create_directories(course_name, year_one, semester_two, semester2_modules)
