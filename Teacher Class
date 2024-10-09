class Teacher:
    def __init__(self, first_name, last_name, age, subject, teacher_id, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.subject = subject
        self.teacher_id = teacher_id
        self.username = username

    def __str__(self):
        return f"Teacher Name: {self.first_name} {self.last_name}, Age: {self.age}, Subject: {self.subject}, ID: {self.teacher_id}, Username: {self.username}"
    
    # Method to save teacher info to a file
    def save_to_file(self, filename='teachers.txt'):
        with open(filename, 'a') as file:
            file.write(str(self) + '\n')
