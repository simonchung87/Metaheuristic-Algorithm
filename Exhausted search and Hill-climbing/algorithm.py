#### ES for One-max problem ####

import time
def binary_add_one(x):
  return bin(int(x,2)+1)[2:].zfill(100) ##將vector從二進制轉換成十進制加一再轉換成二進制（向右走1步）

def evaluate(vector1, vector2):
    return vector1.count("1") <= vector2.count("1") ##判斷新的solution是否好過當前的最優解


vector = "0" * 100 ##初始化變數
best_solution = "0" * 100

start_time = time.time() ##紀錄開始時間
running_time = 1

while int(time.time()-start_time) < running_time and int(vector, 2) < 2^100: ##條件是只要時間沒有超過running_time且vector沒有超過範圍就會一直運行
  if evaluate(best_solution, vector):
    best_solution = vector
  vector = binary_add_one(vector)

print(best_solution)
print(best_solution.count("1")) ##數最後有多少個1

#### 輸出結果：0000000000000000000000000000000000000000000000000000000000000000000000111111111111111111111111111111（30個1）

#### HC for One-max problem ####

import random
import numpy as np
import matplotlib.pyplot as plt


def binary_minus_one(x):
  return bin(int(x,2)-1)[2:].zfill(100) ##將vector從二進制轉換成十進制減一再轉換成二進制（向左走1步）

max_iteration = 10
max_run = 30
record = np.zeros((max_run, max_iteration), dtype='int') ##紀錄信息

for i in range(max_run):
  vector = bin(random.randint(0,int("1"*100, 2)))[2:].zfill(100) ##隨機生成數字轉換成2進制作為初始變量
  for j in range(max_iteration):
    if evaluate(vector, binary_add_one(vector)):
      vector = binary_add_one(vector)
    elif evaluate(vector, binary_minus_one(vector)):
      vector = binary_minus_one(vector)
    record[i,j] = vector.count("1")

average_record = np.mean(record, axis = 0) ##取30次平均
plt.plot(range(10), average_record, '-') ##畫出收斂圖
