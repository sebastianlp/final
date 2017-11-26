import csv
import os
from shutil import copyfile

class UserModel():
    def get_file_name(self):
        return './users/users.csv'
    
    def authenticate(self, username, password):
        ifile = open(self.get_file_name(), "r")
        reader = csv.reader(ifile)

        # el csv tiene el formato: usuario,password
        # asi que, en row[0] tengo el usuario y en row[1] la password
        for row in reader:
            if row[0] == username:
                if row[1] == password:
                    return True
        
        return False

    def register(self, username, password):
        with open(self.get_file_name(), 'r') as readFile, open(self.get_file_name(), 'a') as writeFile:
            reader = csv.reader(readFile)
            writer = csv.writer(writeFile)
            for row in reader:
                if row[0] == username:
                    return False
            writer.writerow([username, password])
            return True
    
    def changePassword(self, username, oldPassword, newPassword):
        copyfile(self.get_file_name(), './users/users.copy.csv')
        with open(self.get_file_name(), 'r') as readFile, open('./users/users.copy.csv', 'w') as writeFile:
            reader = csv.reader(readFile)
            writer = csv.writer(writeFile)
            for row in reader:
                if row[0] == username:
                    if row[1] == oldPassword:
                        writer.writerow([row[0], newPassword])
                        os.remove(self.get_file_name())
                        os.rename('./users/users.copy.csv', self.get_file_name())
                        return True
            
            return False