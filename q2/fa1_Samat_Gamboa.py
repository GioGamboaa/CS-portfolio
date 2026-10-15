''' 
Giovanni Roliz S. Gamboa 07# 9-Samat
'''

class Publication:
    
    def __init__(self, name, author):
        self.name = name
        self.author = author 
        
    def display_info(self):
        print(f"Title: {self.name}")
        print(f"Author: {self.author}")
        
class Book(Publication):
    
    def __init__(self, name, author, number):
        self.name = name
        self.author = author
        
    def set_number_of_pages(self, number):
        if number < 0:
            number = number *-1
        self.number = number
        print("Number of pages must be positive.")
        
    def display_info(self):
        print(f"Title: {self.name}")
        print(f"Author: {self.author}")
        
    def get_number_of_pages(self):
        print(f"Number of pages: {self.number}")
        
        
class Magazine(Publication):
    
    def __init__(self, name, author, number):
        self.name = name
        self.author = author
        self.number = number
        
    def display_info(self):
        print(f"Title: {self.name}")
        print(f"Author: {self.author}")
        
    def get_issue_number(self):
        print(f"Issue number:{self.number}")
            
        
        
        
        
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)


print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)  #setting invalid value on attribute
book1.display_info()
print(book1.get_number_of_pages())
        
print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())
