# 1. 주어진 정수 x와 자연수 n을 이용해, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 출력해주세요
x = 2
n = 5
answer = [x * i for i in range(1, n + 1)]
print("문제1 정답:", answer)

print("-" * 40)

# 2. 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 *으로 가린 문자열이 출력되도록 코드를 작성해주세요
phone_number = "01012347890"
masked = phone_number[:-4] + "****"
print("문제2 정답:", masked)

print("-" * 40)

# 3. 숫자의 일부 자릿수가 영단어로 바뀐 문자열 s가 주어졌을 때 s가 의미하는 원래 숫자를 출력하세요
s = "77three4one"
num_words = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
}
for word, digit in num_words.items():
    s = s.replace(word, digit)
print("문제3 정답:", s)

print("-" * 40)

# 4. 행렬 arr1과 arr2가 주어졌을 때, 행렬 덧셈의 결과를 출력하는 코드
arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]
result = []
for i in range(len(arr1)):
    row = []
    for j in range(len(arr1[0])):
        row.append(arr1[i][j] + arr2[i][j])
    result.append(row)
print("문제4 정답:", result)

print("-" * 40)

# 5. 양의 정수 x가 하샤드 수인지 검사하는 코드
x = 17
digit_sum = sum(int(d) for d in str(x))
is_harshad = x % digit_sum == 0
print("문제5 정답:", is_harshad)

print("-" * 40)

# 6. 배열 seoul의 element 중 "Kim"의 인덱스를 찾아 "김서방은 x에 있다" 출력
seoul = ["Jane", "Kim"]
idx = seoul.index("Kim")
print(f"문제6 정답: 김서방은 {idx}에 있다")

print("-" * 40)

# 7. 0부터 9까지의 숫자 중 numbers에 없는 숫자를 모두 더한 수 출력
numbers = [5, 8, 1, 0, 6, 9]
not_in = [i for i in range(10) if i not in numbers]
print("문제7 정답:", sum(not_in))
