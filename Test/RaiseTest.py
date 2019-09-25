import random

def random_weight_float(w):
    # r = random.random()
    r=20
    for i in range(len(w)):
        r -= w[i]
        if r <= 0:
            return i
    raise Exception("aaa")
    # raise

if __name__ == '__main__':
    list=[1,2,3]
    try:
        print(random_weight_float(list))
    except Exception as e:
        print(e)
