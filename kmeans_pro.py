import numpy as np
import matplotlib.pyplot as plt 
import copy

class SOLVER():
    def __init__(self,task,k_num,max_gen):
        self.task = task
        self.task_num = len(task)
        self.k_num = k_num
        self.max_gen = max_gen
        self.gen = 0
        self.part = []
        self.center = []
        for i in range(self.k_num):
            choice = np.random.randint(i*self.task_num/k_num,(i+1)*self.task_num/k_num)
            self.center.append(task[choice])
            self.part.append([])
        self.check = True
        self.colors = ['#DC143C','#6495ED','#3CB371','#FFD700','#696969']

    def distance(self,node1,node2):
        x = node2[0]-node1[0]
        y = node2[1]-node1[1]
        dis = np.sqrt(x**2+y**2)
        return dis

    def do(self):
        self.check = False
        self.gen += 1
        self.part = [[] for i in range(self.k_num)]

        for i in range(self.task_num):
            fit = []
            for j in range(self.k_num):
                fit.append(self.distance(self.center[j],self.task[i]))
            self.part[np.argmin(fit)].append(i)

        for i in range(self.k_num):
            n_center = np.mean(self.task[self.part[i]],axis=0)
            if (self.center[i] != n_center).all():
                self.center[i] = copy.copy(n_center)
                self.check = True

    def get_color(self,i):
        return self.colors[i]

    


if __name__ == "__main__":
    try:
        work = np.load('work.npy')
    except:
        work = np.random.random([100,2])
        np.save('work.npy',work)
    kmeans = SOLVER(work,3,20)
    while(kmeans.gen<kmeans.max_gen and kmeans.check):
        kmeans.do()

    print('完成所需代数:')
    print(kmeans.gen)
    plt.figure('done')
    for i in range(kmeans.k_num):
        pop = kmeans.task[kmeans.part[i]]
        #print(pop.T[0])
        #print(pop.T[1])
        plt.scatter(pop.T[0],pop.T[1],c=kmeans.get_color(i),marker='x')
    plt.show()
