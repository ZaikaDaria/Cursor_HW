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

class CellPhone:
    def __init__(self):
        self.screen = Screen('6.5"')

class Screen:
    def __init__(self):