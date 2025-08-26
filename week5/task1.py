class Smartphone:
    def __init__(self, brand, model, color):
        self.brand =  brand
        self.model = model
        self.color = color
    
    #method for making a call
    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model} ..."
    
    #method to check phone details
    def phone_details(self):
        return f"Phone Details: Brand - {self.brand}, Model - {self.model}, Color - {self.color}"
    
# Inherited class from Smartphone
class Os(Smartphone):
    def __init__(self, brand, model, color, os_name, os_version):
       super().__init__(brand, model, color)
       self.os_name = os_name
       self.os_version = os_version
    
    #method to check OS details
    def os_details(self):
        return f"OS Details: Name - {self.os_name}, Version - {self.os_version}"
    

# Inherited class from Smartphone and polymorphic method (make_call)
class smartwatch(Smartphone):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)
    
    #method to check smartwatch details
    def smartwatch_details(self):
        return f"Smartwatch Details: Brand - {self.brand}, Model - {self.model}, Color - {self.color}"
    
    #polymorphic method (make_call)
    def make_call(self, number):
        # return super().make_call(number)
        return f"calling {number} through smartwatch..."
    

# Creating objects
phone1 = Smartphone("Apple", "iPhone 13", "Black")
os1 = Os("Google", "Pixel 6", "White", "Android", "12")
watch1 = smartwatch("Samsung", "Galaxy Watch 4", "Silver")

#calling methods
print(phone1.phone_details())
print(phone1.make_call("+1-342-800-6415"))
print(os1.os_details())

#calling inherited/polymorphic methods
print(watch1.make_call("+1-342-800-6415"))
