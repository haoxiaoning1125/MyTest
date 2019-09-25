import random

if __name__ == '__main__':
    print(random.random())

    print(random.choice([1,2,3,4]))

    print(random.sample([1,2,3,4],2))
    try:
        print(random.sample([1,2,3,4],5))
    except Exception as e:
        print(e)

    print(random.randint(1,10))

    print(random.uniform(1.1,5.5))