#함수 안에서 선언한 변수의 효력 범위
#2. global 명령어 사용하기
#vartest_global.py

a = 1
def vartest():
    global a 
    a = a + 1
vartest()
print(a)

#단, 2번째 방법의 경우 외부 변수에 종속적인 함수는 좋은 함수가 아니기 때문에 가급적 43.py 파일에 있는 첫번째 방식을 택하는 것이 좋음