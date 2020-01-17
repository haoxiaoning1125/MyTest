from time import sleep
from tqdm import tqdm
from tqdm._tqdm import trange


if __name__ == '__main__':
    for i in tqdm(range(100)):
        sleep(0.01)

    for i in trange(100):
        sleep(0.01)

    tl = tqdm(list('letters'))
    for c in tl:
        tl.set_description('Now get {}'.format(c))
        sleep(1)
