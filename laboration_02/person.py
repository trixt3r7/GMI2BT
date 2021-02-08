class Person:
    def __init__(self, fname, lname, username, email):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.email = email

    def person_to_dict(self):
        return {'fname': self.fname, 'lname': self.lname, 'username': self.username, 'email': self.email}
