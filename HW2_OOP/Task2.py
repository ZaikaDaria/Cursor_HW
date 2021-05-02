print('-----------composition-----------')
class Person:
    def __init__(self, head, body):
        left_arm = Arm('this is the left one')
        right_arm = Arm('this is the right one')
        self.arms = [left_arm, right_arm]
        self.head = head
        self.body = body


class Arm:
    def __init__(self, hand):
        self.hand = hand


person = Person('round', 'fit')
for per in person.arms:
    print(per.hand)


print('-----------aggregation-----------')
class CellPhone:
    def __init__(self, screen):
        self.screen = screen


class Screen:
    def __init__(self, screen_size):
        self.screen_size = screen_size


medium = Screen('Medium')
my_cellphone = CellPhone(medium)
print(medium.screen_size)
print(my_cellphone.screen.screen_size)
