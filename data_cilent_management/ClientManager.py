import csv


class ClientManager:
    @staticmethod
    def is_already_registered_email(email):
        with open('data/users.csv', mode='r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if email == row[1]:
                    return True
        return False

    @staticmethod
    def is_already_registered_username(username):
        with open('data/users.csv', mode='r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if username == row[0]:
                    return True
        return False
