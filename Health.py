# its Esfand 2nd 1400. 1:28' a.m.this is the first program i have coded  completly by help of God and myself. Happy and Congrats me!
A_count = int(input())
A_age = []
A_hight = []
A_weight = []
for i in range(1):
    A_age = list(map(int, input().split()))
    if len(A_age) != A_count:
        print("invalid amount of numbers")
        break
    A_hight = list(map(int, input().split()))
    if len(A_hight) != A_count:
        print("invalid amount of numbers")
        break
    A_weight = list(map(int, input().split()))
    if len(A_weight) != A_count:
        print("invalid amount of numbers")
        break
B_count = int(input())
B_age = []
B_hight = []
B_weight = []
for i in range(1):
    B_age = list(map(int, input().split()))
    if len(B_age) != B_count:
        print("invalid amount of numbers")
        break
    B_hight = list(map(int, input().split()))
    if len(B_hight) != B_count:
        print("invalid amount of numbers")
        break
    B_weight = list(map(int, input().split()))
    if len(B_weight) != B_count:
        print("invalid amount of numbers")
        break

class ClassA:
    def __init__(self, age, hight, weight):
        self.age = age
        self.hight = hight
        self.weight = weight

    def age_avg(self):
        self.age = sum(A_age)
        age_avg = float(self.age / A_count)
        return age_avg

    def hight_avg(self):
        self.hight = sum(A_hight)
        hight_avg = float(self.hight / A_count)
        return hight_avg

    def weight_avg(self):
        self.weight = sum(A_weight)
        weight_avg = float(self.weight / A_count)
        return weight_avg

class ClassB:
    def __init__(self, age, hight, weight):
        self.age = age
        self.hight = hight
        self.weight = weight

    def age_avg(self):
        self.age = sum(B_age)
        age_avg = float(self.age / B_count)
        return age_avg

    def hight_avg(self):
        self.hight = sum(B_hight)
        hight_avg = float(self.hight / B_count)
        return hight_avg

    def weight_avg(self):
        self.weight = sum(B_weight)
        weight_avg = float(self.weight / B_count)
        return weight_avg
def compare(lst1, lst2, lst3, lst4):
    avg1 = sum(lst1) / len(lst1)
    avg2 = sum(lst2) / len(lst2)
    if avg1 == avg2:
        avg1 = sum(lst3) / len(lst3)
        avg2 = sum(lst4) / len(lst4)
        if avg1 == avg2:
            print("Same")
        elif avg1 > avg2:
            print("B")
        else:
            print("A")
    elif avg1 > avg2:
        print("A")
    else:
        print("B") 

A = ClassA(A_age, A_hight, A_weight)
B = ClassB(B_age, B_hight, B_weight)
print(A.age_avg())
print(A.hight_avg())
print(A.weight_avg())
print(B.age_avg())
print(B.hight_avg())
print(B.weight_avg())
compare(A_hight, B_hight, A_weight, B_weight)