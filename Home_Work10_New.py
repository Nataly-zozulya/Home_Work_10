class Hero:

    def __init__(self, name, health, rang, power, protection, shield_limit, sword_limit):
        self.name = name
        self.health = health
        self.rang = rang
        self.power = power
        self.protection = protection
        self.shield_limit = shield_limit
        self.sword_limit = sword_limit

    def get_health(self):
        return self.__health

    def set_health(self, value):
        if value > 100:
            value = 100
        if value < 0:
            value = 0

        self.__health = value

    health = property(get_health, set_health)

    def get_rang(self):
        return self.__rang

    def set_rang(self, value_2):
        if value_2 > 3:
            value_2 = 3

        if value_2 < 1:
            value_2 = 1

        self.__rang = value_2

    rang = property(get_rang, set_rang)

    def get_power(self):
        return self.__power

    def set_power(self, value_3):
        if value_3 > (self.health // 10):
            value_3 = (self.health // 10)
        if value_3 < 0:
            value_3 = 0

        self.__power = value_3

    power = property(get_power, set_power)

    def hit(self, harm):
        if harm == self.health <= 5:
            return Exception
        else:
            return self.__power

    def use_shield(self, shield):
        if shield <= self.shield_limit:
            return self.protection + 30
        else:
            return Exception

    def use_sword(self, sword):
        if sword <= self.sword_limit:
            return self.power + 20
        else:
            return Exception

hero_1 = Hero("Ivan", 2, 3, 9, 100, 15, 20)
print("Сила після використання меча:", hero_1.use_shield(11))
print("Захист після використання щита:", hero_1.use_sword(14))


from abc import ABC, abstractmethod

class Shop(ABC):

    @abstractmethod
    def buy(self):
        raise NotImplementedError

    @abstractmethod
    def sell(self):
        raise NotImplementedError

class Shop_1(Shop):

    def buy(self):
        print("Shop_1 buy")

    def sell(self):
        print("Shop_1 sell")

s1 = Shop_1()


class Arena:

    def __init__(self, number, staff, trophy):
        self.number = number
        self.staff = staff
        self.trophy = trophy

    def round(self, heroes):
        if 30 > heroes > 1:
            return heroes
        else:
            return Exception

    def tournament_organization(self):
        return self.trophy

arena_1 = Arena(1, 200, 2000)
print("Кіл-ть гравців у поєдинку:", arena_1.round(15))
print("Скільки отримає переможець", arena_1.tournament_organization())