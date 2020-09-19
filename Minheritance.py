#class Grandfather:
 #   cricket=1
 #   music=6

#class Dad(Grandfather):
  #  cricket=23
   # music=9
  #  def cricdetail(self):
      #  return f"He play cricket{self.cricket}th level,and like music {self.music}th that times"

#class Son(Dad):
   # cricket=2
  #  music=8

 #   def cricdetail(self):
      #  return f"Wow to play"\
        #    f"He play cricket{self.cricket}th level,and like music {self.music}th that times"


#tukaram=Grandfather()
#vishwas=Dad()
#sanket=Son()
#print(sanket.cricdetail())

class Electronic_device:
   no_of_circuit=23


class Pocket_gadget(Electronic_device):
    put_in_pocket=3

class Phone(Pocket_gadget):
    call=34
    no_of_circuit = 34

    def phone(self):
        return f"we can call {self.call},taking ph from {self.no_of_circuit}"

ed=Electronic_device()
pg=Pocket_gadget()
ph=Phone()

print(ph.phone())


