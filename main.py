print("sveiks/a")
print("Si programma izdrukas vienkarsu rekinu koka laditei ar gravejumu")

klients = input("Pasutitaja vards,uzvards")
print("-"*50)
veltijums = input("Nepieciesamais veltijums")
print("-"*50)
izmers = input("Ladites izmers - platums,garums,augstums - milimetros(Raksti veselus skaitlus):")
print("-"*50)
materials = input("Kokmateriala cena EUR/n2:")
class rekins():
  def __init__(self,klients,veltijums,izmers,materials):
    self.klients=klients
    self.veltijums=veltijums
    self.izmers=izmers
    self.materials=materials

    self.teksta_gar =len(self.veltijums)
    self.ladites_izm =self.izmers.split(",")
    self.augstums = self.ladites_izm.split[0]

    self.garums = self.izmeri_
        

  def izdruka(self):
    
    print("\n\n")
    print("\033[1m'+Pasutitaja dati:"+"\033[0m")
    print("-"*50)
    print(f"\x1B[3mPasutitaja vards un uzvards:\1B[0m\033[1;32m{self.klients}\033[1;0m")
    print(f"\x1B[3mVeltijuma teksts:\x1B[0m\033[1;32m{self.klients}\033[1;0m")
    print(f"\x1B[3mVeltijuma teksts:\x1B[0m \033[1;32m{self.veltijums}\033[1;0m")
    print(f"\033[1;32m{self.platums}\033[1;0m\n\x1B[3mPlatums;\x1B[0m\033[1;32m{self.garums}\033[1;0m\n\x1B[3mGarums;\x1B[0m\033[1;32m{self.augstums}\033[1;0m")
    print(f"\x1B[3mMatteriala cena EUR/n2:\x1B[0m \033[1;32m{self.materials}\033[1;0m")
    print(f"\1B[3mIzmaksas;\x1B[0m \033[1,32m{self.aprekins()}\033[1;0m")

  def aprekins(self):

    pass

  def aprekins(self):
    darba_samaksa = 15
    PVN = 21
      






    pass




