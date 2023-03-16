#Class
class sculpt_studio:
    def __init__(self,instructor,location,courses,products):
        self.instructor = instructor
        self.location = location
        self.courses = courses
        self.products = products
    def display(self):
        print("Instructor's name: " + self.instructor)
        print("location: " + self.location)
        print("courses available: " + self.courses)
        print("products available: " + self.products)
    def website_courses(self,other_courses, contact_info):
        self.other_courses = other_courses
        self.contact_info = contact_info
    def display_website(self):
        print("Courses available on webiste: " + self.other_courses)
        print("Contact Information: " + self.contact_info)
    def training(self, training):
        if(training == "online"):
            print("You will be trained online")
        elif(training == "physical"):
            print("You will be given physical classes")
            
#Menu 
choice = 0
while(choice != 4):
    sculpture_studio = sculpt_studio("Pam England", "London", "Sculpturing", "Pots")
    sculpture_studio.website_courses("Sculpting ", "PamSculpt@gmail.com")
    sculpture_studio2 = sculpt_studio("Morgan Freeman", "Masachussetts", "Graphic designing", "illustrations")
    sculpture_studio2.website_courses("Graphic Designing ", "Morga@gmail.com")
    print("    MENU SYSTEM     \n")
    print("1: Show information for your required studio\n")
    print("2: Display all the website extra courses, products and information\n")
    print("3: Choose your method of training\n")
    print("4: exit")
    choice = int(input("Input your choice: "))
    if(choice == 1):
        studio_name = input("Enter the studio's name: ")
        if(studio_name == "sculpture"):
            print(sculpture_studio.display())
        elif(studio_name == "graphics"):
            print(sculpture_studio2.display())
    elif(choice == 2):
        studio_name = input("Enter the studio's name: ")
        if(studio_name == "sculpture"):
            print(sculpture_studio.display_website())
        elif(studio_name == "graphics"):
            print(sculpture_studio2.display_website())
    elif(choice == 3):
        course = input("First input the type of course you want Sculpture/graphics: ")
        training = input("Enter your method of getting trained Online/Physical: ")
        if(course == "sculpture"):
            sculpture_studio.training(training)
        elif(course == "graphics"):
            sculpture_studio2.training(training)
        
