class User:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
    def show_profile(self):
        print(f"name:{self.name} and phone:{self.phone} ,email_id:{self.email}")
class Diver:
    def __init__(self,name,phone,driver_id,rating):
        self.name=name
        self.phone=phone
        self.driver_id=driver_id
        self.rating=rating
    def show_driver(self):
        print(f"name:{self.name}")
u1=User("vidya",8522012907,"manchalasrividya3@gmail.com")
u1.show_profile()
