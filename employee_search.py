import re
import sys
import operator
import csv
from os.path import exists

employee_profiles = {}
matches = {}

# text to search for
software = 'adobe acrobat'

<<<<<<< HEAD
def get_file():
    f = input("""Enter the .csv you would like to parse (press CTRL-C to exit)
***This will only work with .csv pulled from DiscoverOrg
 - otherwise you'll have to dig into the code and change the fields ;)***
=======
# ask user for the input file
i_file = input("""Enter the .csv you would like to parse (press CTRL-C to exit)
***This will only work with .csv pulled from DiscoverOrg - otherwise you'll have to dig into the code and change the fields ;)***
>>>>>>> 4b7ae6a520c67ce78f0f447cd8184059b234bfb7
> """)
    return f

# ask user for the input file
i_file = get_file()

print(f"Searching for {i_file}...")

if exists(i_file) == True:
    print("File exists!\n")

    o_file = input("What would you like to name the output file? ")
    o_file = o_file + ".txt"

    target = open(o_file, 'w')

    with open(i_file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')

        for employee in reader:
            # create a blank list for technologies to be placed in
            tech_list2 = []

            # how would you use employee id as a unique identifier?
            employee_name = employee['Employee Full Name']
            employee_tech = employee['Employee Technologies (excludes HG Data technologies)']
            employee_title = employee['Employee Title']
            employee_seniority_level = employee['Employee Seniority Level']
            reports_to = employee['Employee Reports To']
            email = employee['Employee Email Address']
            phone_number = employee['Employee Direct Phone']

            # create the dictionary
            employee_profiles[employee_name] = {}
            employee_profiles[employee_name]["Title"] = employee_title
            employee_profiles[employee_name]["Seniority"] = employee_seniority_level
            employee_profiles[employee_name]["Reports To"] = reports_to
            employee_profiles[employee_name]["Email Address"] = email
            employee_profiles[employee_name]["Phone Number"] = phone_number
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

            employee_profiles[employee_name]["Tech"] = tech_list2

    for entry in employee_profiles.items():
        if software in entry[1]['Tech']:
            target.write(f"""
=============================================================
    {entry[0]}, {entry[1]["Title"]}
        - Reports to: {entry[1]["Reports To"]}
        - Phone Number: {entry[1]["Phone Number"]}
        - Email Address: {entry[1]["Email Address"]}
=============================================================

            """)

    target.close()

else:
    print("Could not find the file...\n")
