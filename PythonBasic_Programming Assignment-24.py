# Solution 1
def amplify(number):

    if not type(number) == int:
        raise TypeError("Please enter an integer.")

    amplified_list = [i*10 if i%4 == 0 else i for i in range(1, number+1)]
    return amplified_list

# Solution 2
def unique(numbers_list):

    for j in numbers_list:
        if type(j) != int and type(j) != float:
            raise TypeError("Please provide a list with numbers- int or float")

    for number in numbers_list:
        if numbers_list.count(number) > 1:
            print(number)

# Solution 3
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        area = 3.14 * (self.radius**2)
        return area

    def getPerimeter(self):
        perimeter = 2 * 3.14 * self.radius

# Solution 4
def sort_by_length(list_strings):

    for k in list_strings:
        if type(k) != str:
            raise TypeError("Please provide a list of string data type.")

    list_strings.sort(key=len)
    return list_strings

# Solution 5
def is_triplet(num_1, num_2, num_3):
    if ((num_1 ** 2) + (num_2 ** 2) == (num_3 ** 2)) or ((num_2 ** 2) + (num_3 ** 2) == (num_1 ** 2)) or ((num_3 ** 2) + (num_1 ** 2) == (num_2 ** 2)):
        return True
    else:
        return False








