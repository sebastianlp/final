import csv

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