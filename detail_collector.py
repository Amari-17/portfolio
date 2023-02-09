import json

class DetailCollector(object):
    """Gets all the data from stored files"""

    def __init__(self):
        self.skills = self.get_skills()
        self.projects = self.get_projects()
        self.contacts = self.get_contacts()

    def get_skills(self):           # gets skills as a list
        with open("\static\data\data_skills.txt") as skills_data:
            skills = skills_data.readlines()
        return skills

    def get_projects(self):         # gets projects as a json
        with open("\static\data\data_projects.json") as projects_data:
            projects = json.load(projects_data)
        return projects['projects']

    def get_contacts(self):         # gets contacts as a json
        with open("\static\data\data_contacts.json") as contacts_data:
            contacts = json.load(contacts_data)
        return contacts['contacts']
