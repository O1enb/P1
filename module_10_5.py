import datetime
from multiprocessing import Pool
import time


def read_info(name):
    all_data = []
    with open(name,'r',encoding='utf-8') as file:
        for line in file:
            all_data.append(line)


file_list = ['file 1.txt','file 2.txt','file 3.txt','file 4.txt']


if __name__ == '__main__':
    start = datetime.datetime.now()
    for file in file_list:
        read_info(file)
    end = datetime.datetime.now()
    print(end-start)


    start2 = datetime.datetime.now()
    with Pool(4) as pool:
        result = pool.map(read_info, file_list)
    end2 = datetime.datetime.now()
    print(end2-start2)




