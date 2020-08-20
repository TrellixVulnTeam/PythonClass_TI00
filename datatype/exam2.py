#exam2.py

#%%
# A : 90 , B:80, C:70 의 형태를 dict 구조로 생성한 후 key : value 형태로
# 출력한다.
dict1 = {"A" : 90, "B" : 80, "C" : 70}
print(dict1)

#%%
# 위의 dict에서 B 키에 해당하는 값만 출력한다.
print(dict1["B"])

#%%
# B 키 값을 삭제한 후 전체 dict를 출력한다.
del dict1["B"]
print(dict1)

#%%
# 다음 항목을 dict 로 생성하기
# 성인 - 10000, 청소년 - 7000, 아동 - 3000
dict2 = {"성인" : 10000, "청소년" : 7000, "아동" : 3000}

#%%
# 위에서 선언한 dict 에 소아 - 0 항목 추가한 후 출력하기
dict2["소아"] = 0
print(dict2)

#%%
# 위에서 선언한 dict 의 key 값만 출력하기
print(dict2.keys())

#%%
# 위에서 선언한 dict 의 value 값만 출력하기
print(dict2.values())

#%%
# foods 라는 딕셔너리를 생성하고 각 음식에 맞는 value를 출력하기
# foods = {
#   "떡볶이":"오뎅",
#   "짜장면":"단무지",
#   "라면":"김치",
#   "피자":"피클",
#   "맥주":"땅콩",
#   "치킨":"맥주",
#   "삼겹살":"상추"
# }
foods = {
  "떡볶이":"오뎅",
  "짜장면":"단무지",
  "라면":"김치",
  "피자":"피클",
  "맥주":"땅콩",
  "치킨":"맥주",
  "삼겹살":"상추"
}
# print(foods.values())

# 사용자에게 좋아하는 음식을 고르게 한 후 그 음식과 궁합이 맞는
# 음식 출력하기(반복문)

while True:
    food = input(str(list(foods.keys())) + " 중 좋아하는 것은? : ")
# 입력값이 '끝' 이라는 글자가 들어오면 반복문 종료
    if food == "끝":
        print("프로그램 종료")
        break
    elif food in foods:
        print("%s의 궁합음식은 %s 입니다." % (food, foods[food]))
# 키 값이 없는 음식을 고르면 "다른 음식을 선택해 주세요" 출력하기
    else:
        print("다른 음식을 선택해 주세요")
        continue

