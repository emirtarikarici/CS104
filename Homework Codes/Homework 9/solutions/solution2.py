class TeaCup:
    def __init__(self, volume, temperature, lemon):
        self.volume = volume
        self.temperature = temperature
        self.lemon = lemon

    # methodA -> decrease_temperature
    def decrease_temperature(self, temperature):
        self.temperature -= temperature

    # methodB -> increase_temperature
    def increase_temperature(self, temperature):
        self.temperature += temperature

    # methodC -> increase_volume
    def increase_volume(self, volume):
        self.volume += volume

    # methodD -> put_lemon
    def put_lemon(self):
        self.lemon = True

    # methodE -> remove_lemon
    def remove_lemon(self):
        self.lemon = False

    def report(self):
        print("The volume of the cup is ", self.volume, " liters.", sep="")
        print("The tea is at ", self.temperature, " degrees centigrade.", sep="")
        print("There is", " no " if self.lemon else " ", "lemon in the cup.", sep="")


# State 1
tea_cup = TeaCup(.1, 30., False)
assert tea_cup.volume == .1
assert tea_cup.temperature == 30.
assert not tea_cup.lemon
tea_cup.report()
# State 2
tea_cup.increase_temperature(20.)
assert tea_cup.volume == .1
assert tea_cup.temperature == 50.
assert not tea_cup.lemon
tea_cup.report()
# State 1
tea_cup.decrease_temperature(20.)
assert tea_cup.volume == .1
assert tea_cup.temperature == 30.
assert not tea_cup.lemon
tea_cup.report()
# State 3
tea_cup.increase_volume(0.1)
assert tea_cup.volume == .2
assert tea_cup.temperature == 30.
assert not tea_cup.lemon
tea_cup.report()
# State 4
tea_cup.put_lemon()
assert tea_cup.volume == .2
assert tea_cup.temperature == 30.
assert tea_cup.lemon
tea_cup.report()
# State 3
tea_cup.remove_lemon()
assert tea_cup.volume == .2
assert tea_cup.temperature == 30.
assert not tea_cup.lemon
tea_cup.report()
