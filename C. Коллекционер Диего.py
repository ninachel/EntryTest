stickers = int(input())
numbers0 = set(map(int, input().split()))
people = int(input())
numbers1 = [set(range(people)) for people in list(map(int, input().split()))]

for i in numbers1:
    print(len(numbers0 & i))

# for i in range(people):
#     p = numbers1[i]
#     result = []
#     for number in sorted(set(numbers0)):
#         if number < p:
#             result.append(number)
#     print(len(set(result)))

# k = 0  # счетчик на коллекционеров
# for person in range(people):
#     p = numbers1[k]  # наименьший номер наклейки, не интересующий коллекционера
#     k += 1
#     numbers2 = []
#     for number in numbers0:
#         if number < p:
#             numbers2.append(number)
#     print(len(set(numbers2)))
