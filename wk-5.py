# Base class
class Superhero:
    def __init__(self, name, power, strength):
        self.name = name
        self._power = power             # Protected attribute
        self.__strength = strength      # Private attribute

    def get_strength(self):
        return self.__strength

    def set_strength(self, value):
        if value > 0:
            self.__strength = value

    def introduce(self):
        print(f"I am {self.name}, and I can {self._power}!")

    def attack(self):
        print(f"{self.name} attacks with strength {self.__strength}!")

# Inherited class
class FlyingHero(Superhero):
    def __init__(self, name, strength, flight_speed):
        super().__init__(name, power="fly", strength=strength)
        self.flight_speed = flight_speed

    def attack(self):
        print(f"{self.name} dives from the sky at {self.flight_speed} km/h with strength {self.get_strength()}!")

# Another subclass
class InvisibleHero(Superhero):
    def __init__(self, name, strength):
        super().__init__(name, power="turn invisible", strength=strength)

    def attack(self):
        print(f"{self.name} disappears and strikes with stealth and strength {self.get_strength()}!")
