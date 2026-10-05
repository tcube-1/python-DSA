# class Student:
#   name = ""
#   age = 0
#   gender = ""
#   def display(self,name="", age=0, gender=""):
#     self .name =name
#     self .age =age
#     self .gender=gender
#     print(f"My name is {self.name}, age is {self.age}, and gender is {self.gender}")


# s1 = Student()
# s2 = Student()


# s1.display('tinku',25,"Male")

class Movie:
  
  def __init__(self, movie_name:str="", total_seats:int=500, tickets_price:int=250) -> None:
    self.movie_name     = movie_name
    self.total_seats    = total_seats
    self.tickets_price  = tickets_price
    self.booked_seats = 0
    self.total_bill = 0

  @property
  def available_seats(self)->int:
      return self.total_seats - self.booked_seats
  
  def book_ticket(self,seat_booked:int=0) -> bool:
    if seat_booked <= 0:
      print(f"Input is not vaild:{seat_booked},Please enter no.of seats")
      return False
    if seat_booked >= self.available_seats:
      print(f"Booking Failed! You can only book from available seats{self.available_seats}")
      return False
    self.booked_seats += seat_booked
    self.total_bill = seat_booked * self.tickets_price
    print(f"Success! {seat_booked} ticket booked for Movie name {self.movie_name}, total Bill:Rs.{self.total_bill}/-")
    return True

  def get_status(self)->str:
    return (
        f"\n* Movie Ticket Booking Status *\n"
        f"-------- {self.movie_name} ---------\n"
        f"Total Capacity  : {self.total_seats}\n"
        f"Available Seats : {self.available_seats}\n"
        f"Booked Seats    : {self.booked_seats}\n"
        f"Calculated Bill : {self.booked_seats} * {self.tickets_price}\n"
        f"--------------------------------------\n"
        f"Total Bill      : {self.total_bill}\n"
        f"--------------------------------------\n")

b1 = Movie("VARANASI")
b1.book_ticket(50)
print(b1.get_status())

