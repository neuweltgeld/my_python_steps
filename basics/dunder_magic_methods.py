class Sum(list):
    def __add__(self,other):
        if len(self) == len(other):
            result = []
            for i in range(len(self)):
                result.append(self[i] + other[i])
            return result
        else:
            print("elmayla armutu mu topluyon ?")

    def __sub__(self,other):
        if len(self) == len(other):
            result = []
            for i in range(len(self)):
                result.append(self[i] - other[i])
            return result
        else:
            print("elmayla armutu mu çıkarıyon ?")


list1 = Sum([1,2,3])
list2 = Sum([4,5,6])

print(list1 + list2)
print(list1 - list2)
