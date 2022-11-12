"""
Coding Bootcamp at the Monroe Township Library

Class 4 Project

You'll be given a list of new employees at a restaurant and are tasked with creating a database that contains
each employee's name, an ID number, and a randomly assigned job
You'll need to create a dictionary for each employee containing three keys: name, ID, and job
Then add each dictionary to the database (which is a list)

Things to consider:
    -You can make your program easier/cleaner by using a loop
    -Assign an ID number however you want, but you have to make sure IDs cannot be duplicated (no 2 employees should have the same ID)
    -Print out at least one of the items in the database list to make sure your program works as expected

For example, if we print out the first entry in our database, we should get something like this:

    print(database[0]) -> {"name" : "John", "id" : "001", "job" : "chef"}
"""

import random


employees = ["John", "Catherine", "Elisa"]
jobs = ["chef", "server", "custodian"]

database = []

#don't worry about understanding this yet, just use assign_job() when creating the job value for each person
#for example: {"job" : assign_job()}
def assign_job():
    """
    assigns a job randomly and updates the available jobs list
    """
    random.shuffle(jobs)
    job = jobs[0]
    jobs.remove(job)

    return job


for i in range(len(employees)):
    employee_info = {
        "name" : employees[i],
        "ID" : str(i+1).zfill(3),
        "job" : assign_job()
    }

    database.append(employee_info)


for i in database:
    print(i)
