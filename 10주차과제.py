#25
key = input("키들을 입력하세요 : ")
value = input("값들을 입력하세요 : ")

keys = key.split()
values = list(map(int, value.split()))

my = dict(zip(keys, values))

if 'alpha' in my:
    del my['alpha']

print(my)

#26
park = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

english_score = park['english']
science_score = park['science']

print(f"English 점수: {english_score}")
print(f"Science 점수: {science_score}")

#27
kim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

for subject in kim:
    kim[subject] = 100

print(kim)

#28
lee = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

if 'english' in lee:
    del lee['english']

print(lee)

#29
lim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

for key, value in lim.items():
    print(f"과목: {key}, 점수: {value}")
    
#30
choi = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

high_scores_dict = {
    key: value
    for key, value in choi.items()
    if value >= 90
}

print(list(high_scores_dict.keys()))

#31
yoo = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

total_sum = sum(yoo.values())
count = len(yoo)

average = total_sum / count

print(f"4과목 평균 점수: {average:.2f}")