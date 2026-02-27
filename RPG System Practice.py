import time

#ผู้เล่น
class Class():
    def __init__(self,CharName,CharHP,CharAttack):
        self.CharName = CharName
        self.CharHP = CharHP
        self.CharAttack = CharAttack

    def showdata(self):
        print("คลาสของคุณคือ ",self.CharName)
        print("------------------------")
        print("พลังชีวิต : ",self.CharHP)
        print("พลังโจมตีพื้นฐาน : ",self.CharAttack)
        print("------------------------")
        print("------------------------")

class Warrior(Class):
    def __init__(self,name,hp,atk):
        super().__init__(name,hp,atk)
        super().showdata()

class Wizard(Class):
    def __init__(self,name,hp,atk):
        super().__init__(name,hp,atk)
        super().showdata()

class Ranger(Class):
    def __init__(self,name,hp,atk):
        super().__init__(name,hp,atk)
        super().showdata()

#มอนสเตอร์
class Monster():
    def __init__(self,MonName,MonHP,MonAttack):
        self.MonName = MonName
        self.MonHP = MonHP
        self.MonAttack = MonAttack

    def showdata(self):
        print("คลาสของคุณคือ ",self.MonName)
        print("------------------------")
        print("พลังชีวิต : ",self.MonHP)
        print("พลังโจมตีพื้นฐาน : ",self.MonAttack)
        print("------------------------")
        print("------------------------")

class Slime(Monster):
    def __init__(self,name,hp,atk):
        super().__init__(name,hp,atk)
        super().showdata()

class Goblin(Monster):
    def __init__(self,name,hp,atk):
        super().__init__(name,hp,atk)
        super().showdata()

print('=========================')
print("ขอต้อนรับเข้าสู่เกม Turn Base จำลองโดยไม้เด็กซ่าสุดหล่อ")
time.sleep(1)
print("ก่อนอื่นเราจะพาคุุณเลือกตัวละครที่คุณต้องการก่อน")
time.sleep(1)
print("โดยเรามีฮีโร่ให้ท่านเลือก 3 คลาสด้วยกัน")
time.sleep(1)
print('=========================')
print("คลาส นักรบ")
print("พลังชีวิต 15")
print("พลังโจมตี 8")
print("มาพร้อมความสามารถ Second Wind")
print("สามารถฟื้นฟูพลังชีวิตได้อย่างต่อเนื่อง")
time.sleep(1)
print('=========================')
print("คลาส จอมเวทย์")
print("พลังชีวิต 8")
print("พลังโจมตี 15")
print("แม้จะโจมตีได้รุนแรง แต่พลังชีวิตไม่สูงนัก")
print("สามารถโจมตีได้ด้วย Fireball")
print("สร้างความเสียหายได้มหาศาล")
time.sleep(1)
print('=========================')
print("คลาส นักธนู")
print("พลังชีวิต 10")
print("พลังโจมตี 10")
print("มาพร้อมกับความสามารถ Double Shot")
print("โจมตีได้สองครั้งในเทิร์นเดียว")
print("สร้างความเสียหายได้ต่อเนื่อง")
time.sleep(1)

player = None

while True:
    print("คุณจะเลือกเป็นคลาสไหน " \
    "1= Warrior " \
    "2 = Wizard " \
    "3 = Ranger")

    try:
        ChooseClass = int(input("โปรดระบุคลาสของท่าน :"))
    except ValueError:
        print("กรุณาใส่ตัวเลขเท่านั้น")
        continue

    if ChooseClass == 1:
        player = Warrior("นักรบ",15,8)
        break

    elif ChooseClass == 2:
        player = Wizard("จอมเวทย์",8,15)
        break

    elif ChooseClass == 3:
        player = Ranger("นักธนู",10,10)
        break

    else:
        print("คุณกรอกข้อมูลไม่ถูกต้อง")

print("\n...กำลังสร้างตัวละคร...")
time.sleep(1)
player.showdata() # เรียกใช้ Method จากตัว player ที่เราเพิ่งสร้าง
print("พร้อมสำหรับการผจญภัยแล้ว!")

