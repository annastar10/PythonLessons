class Unit:
    def __init__(self, name, tribe):
        self._name = name
        self._tribe = tribe
        self._intelligence = 1
        self._force = 1
        self._agility = 1
        self._health = 100

    def __repr__(self):
        return f"strength: {self._force}, agility: {self._agility}, intelligence: {self._intelligence}, health: {self._health}"

    def heal(self):
        if self._health < 91:
            self._health += 10
        elif self._health >= 91:
            self._health = 100

    def improve_base_skill(self):
        raise NotImplementedError

    @property
    def intelligence(self):
        return self._intelligence

    @property
    def tribe(self):
        return self._tribe

    @property
    def force(self):
        return self._force

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def agility(self):
        return self._agility


class Mage(Unit):
    def __init__(self, name, tribe):
        super(Mage, self).__init__(name=name, tribe=tribe)

    def improve_base_skill(self):
        if self.intelligence < 10:
            self._intelligence += 1


class Archer(Unit):
    def __init__(self, name, tribe):
        super(Archer, self).__init__(name=name, tribe=tribe)

    def improve_base_skill(self):
        if self.agility < 10:
            self._agility += 1


class Knight(Unit):
    def __init__(self, name, tribe):
        super(Knight, self).__init__(name=name, tribe=tribe)

    def improve_base_skill(self):
        if self.force < 10:
            self._force += 1


wizard = Mage("sada", "asdad")
wizard.improve_base_skill()
wizard.improve_base_skill()
wizard.improve_base_skill()
print("Wizard: ", wizard)

knight = Knight("asdasd", "asdasd")
knight.improve_base_skill()
knight.improve_base_skill()
knight.improve_base_skill()
print("Knight: ", knight)

arch = Archer("sdfassd", "asdasfw")
arch.improve_base_skill()
arch.improve_base_skill()
arch.improve_base_skill()

print("Archer: ", arch)
