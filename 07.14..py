
# 문제 1:
# x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 출력하세요.
x = 2
n = 5
answer1 = [x * i for i in range(1, n + 1)]
print("문제 1 정답:", answer1)  # 출력: [2, 4, 6, 8, 10]

# -----------------------------------------------------

# 문제 2:
# 전화번호 문자열에서 뒤 4자리를 *로 가리세요.
phone_number = "01012347890"
answer2 = phone_number[:-4] + "****"
print("문제 2 정답:", answer2)  # 출력: "0101234****"

# -----------------------------------------------------

# 문제 3:
# 문자열에서 영단어를 숫자로 바꿔 출력하세요.
s = "77three4one"
number_map = {
    "zero": "0", "one": "1", "two": "2", "three": "3",
    "four": "4", "five": "5", "six": "6", "seven": "7",
    "eight": "8", "nine": "9"
}
for word, num in number_map.items():
    s = s.replace(word, num)
answer3 = int(s)
print("문제 3 정답:", answer3)  # 출력: 77341

# -----------------------------------------------------

# 문제 4:
# 행렬 덧셈 결과를 출력하세요.
arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]
answer4 = [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(arr1, arr2)]
print("문제 4 정답:", answer4)  # 출력: [[4, 6], [7, 9]]

# -----------------------------------------------------

# 문제 5:
# x가 하샤드 수인지 판단하세요.
x = 17
sum_of_digits = sum(int(digit) for digit in str(x))
answer5 = x % sum_of_digits == 0
print("문제 5 정답:", answer5)  # 출력: False

# -----------------------------------------------------

# 문제 6:
# seoul 리스트에서 "Kim"의 위치를 찾아 출력하세요.
seoul = ["Jane", "Kim"]
index = seoul.index("Kim")
answer6 = f"김서방은 {index}에 있다"
print("문제 6 정답:", answer6)  # 출력: "김서방은 1에 있다"

# -----------------------------------------------------

# 문제 7:
# 0부터 9까지의 숫자 중 numbers에 없는 숫자를 모두 더하세요.
numbers = [5, 8, 1, 0, 6, 9]
missing_numbers = set(range(10)) - set(numbers)
answer7 = sum(missing_numbers)
print("문제 7 정답:", answer7)  # 출력: 1