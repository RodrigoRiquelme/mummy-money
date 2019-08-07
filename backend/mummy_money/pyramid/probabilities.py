from math import log

from mummy_money.pyramid import Stats


class Probabilities:
    @staticmethod
    def find_another_member(investor):
        recruited = Stats.find_recruited_members(investor)
        return investor.experience * investor.charisma * (1 - log(10, 10))
