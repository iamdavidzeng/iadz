# -*- coding: utf-8 -*-
words = ["Hannibal", "Hanny", "Steeve"]


for index, word in enumerate(words[:]):
    print(index, word)
    print(words)
    if word == "Hannibal":
        words.pop(index)
        continue

# output:
# 0 Hannibal
# ['Hannibal', 'Hanny', 'Steeve']
# 1 Steeve
# ['Hanny', 'Steeve']

# 在第一轮的时候，会把index=0的元素踢出，
# 在第二轮的时候，words当中的元素已经发生了变化，
# 导致了index=1的元素变为了Steeve，所以会漏掉Hanny。
# 解决方法为重新创建一个对象用于枚举，而不去影响原来的数组。

# 0 Hannibal
# ['Hannibal', 'Hanny', 'Steeve']
# 1 Hanny
# ['Hanny', 'Steeve']
# 2 Steeve
# ['Hanny', 'Steeve']
