# 출력
string_msg = "Spring is beginning"
int_val = 3
string_val = "3"

print(string_msg)
print(int_val + 10)
print(string_val + "10")

# 피타고라스 정리
a = int(input())
c = int(input())

b_square = c*c - a*a
print(b_square)

# 나이계산
year = int(input())
age_type = input()

if age_type == "Korea": answer = 2030 - year + 1
elif age_type == "Year": answer = 2030 - year

print(answer)
