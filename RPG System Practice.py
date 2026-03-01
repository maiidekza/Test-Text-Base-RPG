import time
import random
import os

# นักรบ
WARRIOR_HP = 20
WARRIOR_ATK = 8

# จอมเวทย์
WIZARD_HP = 12
WIZARD_ATK = 15

# นักธนู
RANGER_HP = 15
RANGER_ATK = 10

# ผู้เล่น


class Class():
    def __init__(self, CharName, CharHP, CharAttack):
        self.CharName = CharName
        self.CharHP = CharHP
        self.CharAttack = CharAttack
        self.MaxHP = CharHP
        self.Level = 1
        self.Exp = 0
        self.MaxExp = 100

    def showdata(self):
        print("------------------------")
        print("\nคลาสของคุณคือ ", self.CharName)
        print("------------------------")
        print("พลังชีวิต : ", self.CharHP)
        print("พลังโจมตีพื้นฐาน : ", self.CharAttack)
        print("\n------------------------")

    def player_takedmg(self, dmg):
        self.CharHP = self.CharHP - dmg
        print("⚔️ โดนโจมตี", dmg, "ดาเมจ! เลือดเหลือ", self.CharHP)

    def gain_exp(self, amount):
        self.Exp += amount
        print(f"✨ ได้รับ {amount} EXP")
        while self.Exp >= self.MaxExp:
            self.Level += 1
            self.Exp -= self.MaxExp
            self.MaxExp = int(self.MaxExp * 1.2)
            self.MaxHP += 10
            self.CharHP = self.MaxHP
            self.CharAttack += 2
            print(
                f"🆙 LEVEL UP! เป็น Lv.{self.Level} (HP+10, ATK+2, เลือดเต็ม!)")
            time.sleep(1)


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
        print("------------------------")
        print("\nมีมอนสเตอร์ปรากฏตัว มันคือ!! :  ", self.MonName)
        print("------------------------")
        print("พลังชีวิต : ", self.MonHP)
        print("พลังโจมตีพื้นฐาน : ", self.MonAttack)
        print("\n------------------------")

    def monster_takedmg(self, dmg):
        self.MonHP = self.MonHP - dmg
        print(player.CharName, " ⚔️ โจมตี", dmg,
              "ดาเมจ! เลือดเหลือ", self.MonHP)


class Slime(Monster):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)
        super().showdata()


class Goblin(Monster):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)
        super().showdata()


class Dragon(Monster):  # Boss
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)


def clean():
    if os.name == 'nt':
        os.system('cls')
    else:
        pass


print('=========================')

print("\nขอต้อนรับเข้าสู่เกม Turn Base จำลองโดยไม้เด็กซ่าสุดหล่อ")
time.sleep(1)

print("ก่อนอื่นเราจะพาคุุณเลือกตัวละครที่คุณต้องการก่อน")
time.sleep(1)

print("โดยเรามีฮีโร่ให้ท่านเลือก 3 คลาสด้วยกัน")
time.sleep(1)

print('\n=========================')
print("\nคลาส นักรบ")
print(f"พลังชีวิต {WARRIOR_HP}")
print(f"พลังโจมตี {WARRIOR_ATK}")
print("มาพร้อมความสามารถ Second Wind")
print("สามารถฟื้นฟูพลังชีวิตได้อย่างต่อเนื่อง")

time.sleep(1)

print('\n=========================')
print("\nคลาส จอมเวทย์")
print(f"พลังชีวิต {WIZARD_HP}")
print(f"พลังโจมตี {WIZARD_ATK}")
print("แม้จะโจมตีได้รุนแรง แต่พลังชีวิตไม่สูงนัก")
print("สามารถโจมตีได้ด้วย Fireball")
print("สร้างความเสียหายได้มหาศาล")

time.sleep(1)

print('\n=========================')
print("\nคลาส นักธนู")
print(f"พลังชีวิต {RANGER_HP}")
print(f"พลังโจมตี {RANGER_ATK}")
print("มาพร้อมกับความสามารถ Double Shot")
print("โจมตีได้สองครั้งในเทิร์นเดียว")
print("สร้างความเสียหายได้ต่อเนื่อง")
time.sleep(1)

player = None

while True:
    print("\nคุณจะเลือกเป็นคลาสไหน "
          "\n1 = Warrior "
          "\n2 = Wizard "
          "\n3 = Ranger")

    try:
        ChooseClass = int(input("โปรดระบุคลาสของท่าน :"))
    except ValueError:
        print("กรุณาใส่ตัวเลขเท่านั้น")
        continue

    if ChooseClass == 1:
        player = Warrior("นักรบ", WARRIOR_HP, WARRIOR_ATK)
        clean()
        break

    elif ChooseClass == 2:
        player = Wizard("จอมเวทย์", WIZARD_HP, WIZARD_ATK)
        clean()
        break

    elif ChooseClass == 3:
        player = Ranger("นักธนู", RANGER_HP, RANGER_ATK)
        clean()
        break

    else:
        print("คุณกรอกข้อมูลไม่ถูกต้อง")

print("\n...กำลังสร้างตัวละคร...")
time.sleep(1)
print("พร้อมสำหรับการผจญภัยแล้ว!")

enemy = None

print("มอนสเตอร์ปรากฏตุวแล้ว!!!")

time.sleep(1)

Stage = 1

while True:
    if player.CharHP <= 0:
        print("\n💀 คุณเสียชีวิตแล้ว... จบเกม!")
        break
    elif Stage == 1:
        enemy = Slime("Slime", 20, 5)
        print("ด่านที่ 1: ป่าสไลม์")
    elif Stage == 2:
        enemy = Goblin("Goblin", 40, 10)  # เก่งขึ้น!
        print("ด่านที่ 2: ถ้ำก็อบลิน")
    elif Stage == 3:
        enemy = Dragon("Boss Dragon", 100, 12)
        print("\n🌋 Stage 3: รังมังกร (BOSS)")
    else:
        print("คุณพิชิตเกมนี้แล้ว! ยินดีด้วย!")
        break  # จบเกม

    print("การต่อสู้เริ่มขึ้น", player.CharName, " vs ", enemy.MonName)

    while True:
        time.sleep(5)
        print("===========================================================================================")
        print(f"\n--- เทิร์นของ {player.CharName} ---")
        print(f"เลือดของคุณ: {player.CharHP} | เลือดศัตรู: {enemy.MonHP}")
        print("เลือก การกระทำของคุณ")
        print(f"\n1= Attack พลังโจมตี ปัจจุบัน : {player.CharAttack}"
              "\n2 = Skill "
              "\n3 = Run")
        action = input("ป้อนตัวเลขเพื่อเลือกคำสั่ง : ")

        if action == "3":
            print("คุณวิ่งหนีหัวซุกหัวซุน... (จบการต่อสู้)")
            break

        if action == "1":
            clean()
            print(f">>> คุณโจมตีใส่ {enemy.MonName}!")
            damage_to_deal_player = random.randint(
                player.CharAttack, player.CharAttack + 2)
            # เรียกใช้งานฟังชั่นคำนวนดาเมจ
            if random.randint(1, 8) <= 4:
                print("\n💥 การโจมตี ติดคริติคอล!!! (Critical Hit!)")
                damage_to_deal_player = damage_to_deal_player * 2
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
                print(
                    f" Ranger ยิง Double Shot! ดอกศรคู่! ({double_shot} dmg)")
                enemy.monster_takedmg(double_shot)

        time.sleep(1)

        if enemy.MonHP <= 0:
            print(f"\n ชัยชนะ! {enemy.MonName} ถูกกำจัดแล้ว")
            print(f"ชนะด่าน {Stage} แล้ว!")
            exp_gain = 50 * Stage
            player.gain_exp(exp_gain)
            heal_amount = 10
            player.CharHP += heal_amount
            print(f"ได้พักผ่อน... เลือดเพิ่มขึ้น {heal_amount}")
            Stage += 1
            time.sleep(1)
            break

        print(f"\n--- เทิร์นของ {enemy.MonName} ---")
        time.sleep(1)

        print(f">>> {enemy.MonName} สวนกลับ!")
        enemy_damage = max(0, random.randint(
            enemy.MonAttack - 4, enemy.MonAttack + 0))
        if random.randint(1, 20) <= 5:
            print("\nคุณหลบการโจมตีได้ ! ! ! บ้าน่า ! ! ! ")
            enemy_damage = 0

        player.player_takedmg(enemy_damage)
        time.sleep(1)

        # เช็คว่าเราตายหรือยัง?
        if player.CharHP <= 0:
            break
