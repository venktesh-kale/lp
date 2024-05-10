def greet(name, year):
    print("Hello my name is :", name)
    print("I was created in :", year)

def remind_name():
    print("Please remind your name : ")
    name = input()
    print("What a great name you have ! ", name)

def guess_age():
    print("Let me guess your age : ")
    print("Enter reminder of your age by dividing it by 3, 5 and 7 : ")
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())

    age = (rem3 * 70 + rem5 * 21 + rem7 * 15)% 105
    print("Your age is : ", age)

def count():
    cnt  = int(input("I can count to any number please enter any number to count : "))
    for i in range (cnt+1):
        print(i)

def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")

    answer = 2
    guess = int(input())
    while guess != answer:
        print("Please, try again.")
        guess = int(input())

def end():
    print('Congratulations, have a nice day!')

greet('bot', '2024')
remind_name()
guess_age()
count()
test()
end()