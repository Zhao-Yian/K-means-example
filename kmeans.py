import matplotlib.pyplot as plt
import numpy as np

# 导入python包

colors = '#708090'
colors1 = '#00CED1'
colors2 = '#DC143C'


# 计算欧氏距离
def distance(node1, node2):
    x = node1[0] - node2[0]
    y = node1[1] - node2[1]
    dis = np.sqrt(x ** 2 + y ** 2)
    return dis


work_num = 100
gen_max = 20
try:
    work = np.load('work.npy')
except:
    # 生成包括work_num个列表的二维列表，每个列表俩元素，分别表示横纵坐标
    work = np.random.random([work_num, 2])
    # print(work)
    # print("---------------------------")
    # print(work.T[0])
    # print(work.T[1])
    np.save('work.npy', work)
plt.figure('work')
plt.scatter(work.T[0], work.T[1], marker='x', c=colors)
# plt.show()

center1 = work[np.random.randint(work_num / 2)]
center2 = work[np.random.randint(work_num / 2, work_num)]

check_flag = True
gen = 0

while check_flag and gen < gen_max:
    check_flag = False
    gen += 1
    part1 = []
    part2 = []

    for i in range(work_num):
        dis1 = distance(work[i], center1)
        dis2 = distance(work[i], center2)
        if dis1 > dis2:
            part2.append(i)
        else:
            part1.append(i)
    p1 = work[part1]
    p2 = work[part2]
    n_center1 = np.mean(p1, axis=0)
    n_center2 = np.mean(p2, axis=0)
    if (center1 != n_center1).all() or (center2 != n_center2).all():
        center1 = np.mean(p1, axis=0)
        center2 = np.mean(p2, axis=0)
        check_flag = True

plt.figure('done')
# print(p1)
plt.scatter(p1.T[0], p1.T[1], marker='x', c=colors1)
plt.scatter(p2.T[0], p2.T[1], marker='x', c=colors2)
plt.show()
