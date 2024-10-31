class UserAccount:
    def __init__(self,username,email,password):
        self.username=username
        self.email=email
        self.password=password
    def set_password(self,new_password):
        self.password=new_password
    def check_password(self,password):
        print(password==self.password)
k=UserAccount('name','email','123')
UserAccount.check_password(k,'321')
UserAccount.set_password(k,'321')
UserAccount.check_password(k,'321')