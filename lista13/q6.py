# print(sorted([input("Digite um número: ") for i in range(10)]))

nums = [float(input("Digite um número: ")) for i in range(10)]

nums = list(map(lambda a: (float(a) == int(a) and int(a) or a), nums))

print()
print("Em ordem decrescente:")
print(*sorted(nums, reverse=True), sep=", ")