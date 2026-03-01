import time
import random

# ผู้เล่น


class Class():
    def __init__(self, CharName, CharHP, CharAttack):
        self.CharName = CharName
        self.CharHP = CharHP
        self.CharAttack = CharAttack

    def showdata(self):
        print("คลาสของคุณคือ ", self.CharName)
        print("------------------------")
        print("พลังชีวิต : ", self.CharHP)
        print("พลังโจมตีพื้นฐาน : ", self.CharAttack)
        print("------------------------")
        print("------------------------")

    def player_takedmg(self, dmg):
        self.CharHP = self.CharHP - dmg
        print("โดนโจมตี", dmg, "ดาเมจ! เลือดเหลือ", self.CharHP)


class Warrior(Class):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)
        super().showdata()


class Wizard(Class):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)
        super().showdata()


class Ranger(Class):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)
        super().showdata()


# มอนสเตอร์
class Monster():
    def __init__(self, MonName, MonHP, MonAttack):
        self.MonName = MonName
        self.MonHP = MonHP
        self.MonAttack = MonAttack

    def showdata(self):
        print("มีมอสเตอร์ปรากฏตัว มันคือ!! :  ", self.MonName)
        print("------------------------")
        print("พลังชีวิต : ", self.MonHP)
        print("พลังโจมตีพื้นฐาน : ", self.MonAttack)
        print("------------------------")
        print("------------------------")

    def monster_takedmg(self, dmg):
        self.MonHP = self.MonHP - dmg
        print("โดนโจมตี", dmg, "ดาเมจ! เลือดเหลือ", self.MonHP)


class Slime(Monster):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)
        super().showdata()


class Goblin(Monster):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)
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
    print("คุณจะเลือกเป็นคลาสไหน "
          "1= Warrior "
          "2 = Wizard "
          "3 = Ranger")

    try:
        ChooseClass = int(input("โปรดระบุคลาสของท่าน :"))
    except ValueError:
        print("กรุณาใส่ตัวเลขเท่านั้น")
        continue

    if ChooseClass == 1:
        player = Warrior("นักรบ", 15, 8)
        break

    elif ChooseClass == 2:
        player = Wizard("จอมเวทย์", 8, 15)
        break

    elif ChooseClass == 3:
        player = Ranger("นักธนู", 10, 10)
        break

    else:
        print("คุณกรอกข้อมูลไม่ถูกต้อง")

print("\n...กำลังสร้างตัวละคร...")
time.sleep(1)
player.showdata()  # เรียกใช้ Method จากตัว player ที่เราเพิ่งสร้าง
print("พร้อมสำหรับการผจญภัยแล้ว!")

enemy = None

print("มอนสเตอร์ปรากฏตุวแล้ว!!!")

enemy = Slime("สไลม์", 50, 3)

time.sleep(1)

print("การต่อสู้เริ่มขึ้น", player.CharName, " vs ", enemy.MonName)

time.sleep(1)

while True:
    print(f"\n--- เทิร์นของ {player.CharName} ---")
    print(f"เลือดของคุณ: {player.CharHP} | เลือดศัตรู: {enemy.MonHP}")
    print("เลือก การกระทำของคุณ")
    print("คุณจะเลือกเป็นคลาสไหน "
          "1= Attack "
          "2 = Skill "
          "3 = Run")
    action = input()

    if action == "3":
        print("คุณวิ่งหนีหัวซุกหัวซุน... (จบการต่อสู้)")
        break

    if action == "1":
        print(f">>> คุณโจมตีใส่ {enemy.MonName}!")
        damage_to_deal_player = random.randint(
            player.CharAttack * 1, player.CharAttack * 2)
        # เรียกใช้งานฟังชั่นคำนวนดาเมจ
        enemy.monster_takedmg(damage_to_deal_player)

    if action == "2":
        # ตรวจสอบว่า "ผู้เล่นเป็นอาชีพอะไร?"
        if isinstance(player, Warrior):
            heal_amount = 5
            player.CharHP = player.CharHP + heal_amount
            print(
                f" Warrior ใช้ Second Wind! ฟื้นฟูเลือด {heal_amount} หน่วย (เลือดปัจจุบัน: {player.CharHP})")

        elif isinstance(player, Wizard):
            fireball_dmg = 20
            print(f" Wizard ร่าย Fireball! ตูมมม!!! ({fireball_dmg} dmg)")
            enemy.monster_takedmg(fireball_dmg)

        elif isinstance(player, Ranger):
            double_shot = player.CharAttack * 2
            print(f" Ranger ยิง Double Shot! ดอกศรคู่! ({double_shot} dmg)")
            enemy.monster_takedmg(double_shot)

    time.sleep(1)

    if enemy.MonHP <= 0:
        print(f"\n ชัยชนะ! {enemy.MonName} ถูกกำจัดแล้ว")
        break

    print(f"\n--- เทิร์นของ {enemy.MonName} ---")
    time.sleep(1)

    print(f">>> {enemy.MonName} สวนกลับ!")
    enemy_damage = max(0, random.randint(
        enemy.MonAttack - 3, enemy.MonAttack + 1))

    # เรียกใช้ฟังก์ชันเจ็บตัวของผู้เล่นที่คุณเขียนไว้
    player.player_takedmg(enemy_damage)
    time.sleep(1)

    # เช็คว่าเราตายหรือยัง?
    if player.CharHP <= 0:
        print("\n คุณพ่ายแพ้... Game Over")
        break
