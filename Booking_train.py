class train:
   def __init__(self,name,number,seats,fare):
    self.name=name
    self.number=number
    self.seats=seats
    self.fare=fare
   def show_seats(self):
    print("\nTrain:",self.name,"",self.number)
    print("available seats:",self.seats)
   def book_ticket(self,name,tickets):
        if tickets<=0:
            print("number of tickets.")
        elif tickets<=self.seats:
          self.seats=self.seats-tickets
          fare=tickets*self.fare
          print("\nSuccess:",tickets,"tickets booked for",name,"on",self.name,)
          print("Total fare:",fare)
          print("Remaining seats:",self.seats)
        else:
            print("\nSorry",name,"-only",self.seats,"seats available.")
train=train("Gomti Express",12419,60,800)
train.show_seats()
train.book_ticket("shubhi",10)
train.book_ticket("Supriya",12)
train.show_seats()
train.book_ticket("Saksham",15)