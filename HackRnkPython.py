# def reverse_words_order_and_swap_cases(sentence):
#     listsent = sentence.split()
#     listsent.reverse()
#     s = " "
#     s = s.join(listsent)
#     s = s.swapcase()
#     print(s)


# reverse_words_order_and_swap_cases('This is a test')
# class Multiset:
#     Multiset = []
#     Result = []
#     def __init__(self, valu):

#     def add(self, val):
#         Multi.append(val)

#     def remove(self, val):
#             Multi.remove(val)

#     def query(self, val):
#         if val in Multi:
#             result.append(True)
#         else:
#             result.append(False)

#     def size(self):
#         return
# -------------------------------------
def descending_order(num):
    if num > 10:
      n = [int(x) for x in str(num)]
      n.sort(reverse = True)
      s = ""
      s=s.join(n)
      print(s)
    else:
      print(num)

descending_order(15)
