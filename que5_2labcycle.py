class publisher:
   def title(self):
    print("TITLE OF BOOK")
   def author(self):
    print("AUTHOR OF THE BOOK::abcdef")

class book(publisher):
   def title(self):
    print("BOOK NAME is python")

class python(book):
   def price(self):
    print("Price of the book::343")

   def no_of_page(self):
    print("NO_OF_PAGES:1000")


obj=python()
obj.title()
obj.author()
obj.price()
obj.no_of_page()