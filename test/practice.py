


class Practice:

    def find_min_max(self, list1):

        min_num = list1[0]
        # max = list1[-1]

        for i in range(len(list1)):
            if min_num<=list1[i]:
                number = min_num

        print(number)
        max = sorted(list1)
        print(max[-1])



    def longest_subs(self, str1):

        str1 = str1.split(" ")

        longest = len(str1[0])

        print(str1)
        for i in range(len(str1)):

            lenth = len(str1[i])

            if longest>=lenth:
                long_sub = longest
                sub = str1[i]
            print(long_sub, sub)


    def print_string(self):
        import re
        import pandas as pd
        str2 = ["hello", "india"]

        output = "hello india"
        s = ""
        for i in range(len(str2)):
            s = s + "".join(str2[i])

        print(s)












practice = Practice()
# practice.find_min_max([1,2,10,5,6])
#
# practice.longest_subs("this partha sen and I am in interview call")

practice.print_string()

