import csv

class Department:
    def __init__(self, name, leader, power):
        self.name = name
        self.leader = leader
        self.power = power

    def __str__(self):
        return f"{self.name} - Leader: {self.leader}, Power: {self.power}"


class Government:
    def __init__(self):
        self.departments = []

    def load_from_csv(self, filename):
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                self.departments = []
                for row in reader:
                    if len(row) == 3:
                        dept = Department(row[0], row[1], row[2])
                        self.departments.append(dept)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found.")


    def view_departments(self):
        if not self.departments:
            print("No departments to display.")
        else:
            for dept in self.departments:
                print(dept)

    def selection_sort_by_name(self):
        n = len(self.departments)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if self.departments[j].name < self.departments[min_index].name:
                    min_index = j
            self.departments[i], self.departments[min_index] = self.departments[min_index], self.departments[i]

    def bubble_sort_by_leader(self):
        n = len(self.departments)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.departments[j].leader > self.departments[j + 1].leader:
                    self.departments[j], self.departments[j + 1] = self.departments[j + 1], self.departments[j]
