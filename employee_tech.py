import re
import operator
import csv

employee_scores = {}
employee_profile = {}
matches = {}

# compatible_list = ['microsoft sharepoint', 'adobe acrobat', 'adobe creative suite',
# 'imanage', 'microsoft office', 'citrix', 'dropbox', 'microsoft exchange',
# 'microsoft office 365', 'microsoft onenote', 'microsoft windows onedrive (formerly skydrive)',
# 'windows sharepoint services', 'microsoft active directory', 'google drive',
# 'docusign electronic signature solution', 'microsoft windows 7', 'citrix xenmobile (zenprize)',
# 'microsoft os', 'microsoft sharepoint server', 'microsoft windows 8', 'microsoft azure',
# 'microsoft windows servers']

acrobat = 'adobe acrobat'

i_file = "sf_test.csv"

# o_file = i_file[:-4] + ".txt"

# target = open(o_file, 'w')

with open(i_file) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    for employee in reader:
        # create a blank list for technologies to be placed in
        tech_list2 = []

        # how would you use employee id as a unique identifier?
        # define the company parameters to search
        employee_name = employee['Employee Full Name']
        employee_tech = employee['Employee Technologies (excludes HG Data technologies)']
        employee_title = employee['Employee Title']
        employee_seniority_level = employee['Employee Seniority Level']
        reports_to = employee['Employee Reports To']
        email = employee['Employee Email Address']
        phone_number = employee['Employee Direct Phone']

        # create the dictionary
        employee_scores[employee_name] = {}
        employee_scores[employee_name]["Title"] = employee_title
        employee_scores[employee_name]["Seniority"] = employee_seniority_level
        employee_scores[employee_name]["Reports To"] = reports_to
        employee_scores[employee_name]["Email Address"] = email
        employee_scores[employee_name]["Phone Number"] = phone_number
        matches[employee_name] = []

        tech_list = employee_tech.split(';')
        for tech in tech_list:
            tech = tech.split(',')
            for program in tech:
                if ":" in program:
                    program = program.split(':')
                    tech_list2.append(program[1].strip().lower())
                else:
                    tech_list2.append(program.strip().lower())

        employee_scores[employee_name]["Tech"] = tech_list2

for entry in employee_scores.items():
    if acrobat in entry[1]['Tech']:
        print(f"""=============================================================
{entry[0]}, {entry[1]["Title"]}
    - Reports to: {entry[1]["Reports To"]}
    - Phone Number: {entry[1]["Phone Number"]}
    - Email Address: {entry[1]["Email Address"]}
=============================================================

        """)
# target.close()
