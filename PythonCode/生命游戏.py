import numpy as np
lifepoint = np.random.randint(2,size=(18,18)).astype(np.uint8)
print('lifepoint')
newlifepoint=np.zeros_like(lifepoint)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('                                                        ')
rows,cols=lifepoint.shape
for i in range(rows-1):
    for  j in range(cols-1):
        lifestate=lifepoint[i,j]
        area=lifepoint[i-1:i+2,j-1:j+2]
        d=np.sum(area)-lifestate

        if lifestate:
            if d==2 or d==3:
                newlifepoint[i,j]=1
            else:
                newlifepoint[i,j]=0
        else:
            if d==3:
                newlifepoint[i,j]=1
print('newlifepoint')

class lifegame(object):
    def __init__(self):
        self.lifepoint=np.random.randint(2,size=(18,18)).astype(np.uint8)
        self.cols,self.rows=self.lifepoint.shape
    def __iter__(self):
        return self
    def next(self):
        newcopy=self.lifepoint.copy()
        for i in range(1,self.cols):
            for j in range(1,self.rows):
                lifestate=self.lifepoint[i,j]
                area=self.lifepoint[i-1:i+2,j-1:j+2]
                d=np.sum(area)-lifestate

                if lifestate:
                    if d==3 or d==2:
                        self.lifepoint[i,j]=1
                    else:
                        self.lifepoint[i,j]=0
                else:
                    if d==3:
                        self.lifepoint[i,j]=1

        for j in range(1,self.rows):
            edgelifestate1=newcopy[0,j]
            area1=newcopy[0:2,j-1:j+2]
            d1=np.sum(area1)-edgelifestate1
            if edgelifestate1:
                if d1==3 or d1==2:
                    self.lifepoint[0,j]=1
                else:
                    self.lifepoint[0,j]=0
            else:
                if d1==3:
                    self.lifepoint[0,j]=1

        for j in range(1, self.rows):
            edgelifestate2 = newcopy[self.cols-1, j]
            area2 = newcopy[self.cols-2:self.cols, j - 1:j + 2]
            d2 = np.sum(area2) - edgelifestate2
            if edgelifestate2:
                if d2 == 3 or d2 == 2:
                    self.lifepoint[self.cols-1, j] = 1
                else:
                    self.lifepoint[self.cols-1, j] = 0
            else:
                if d2 == 3:
                    self.lifepoint[self.cols-1, j] = 1
        for i in range(1, self.cols):
            edgelifestate3 = newcopy[i, 0]
            area3 = newcopy[i-1:i+2, 0:2]
            d3 = np.sum(area3) - edgelifestate2
            if edgelifestate3:
                if d3 == 3 or d3 == 2:
                    self.lifepoint[i, 0] = 1
                else:
                    self.lifepoint[i, 0] = 0
            else:
                if d3 == 3:
                    self.lifepoint[i, 0] = 1
        for i in range(1, self.cols):
            edgelifestate4 = newcopy[i,self.rows-1]
            area4 = newcopy[i :i+2, self.rows-2:self.rows]
            d4 = np.sum(area4) - edgelifestate4
            if edgelifestate3:
                if d4 == 3 or d4 == 2:
                    self.lifepoint[i, 0] = 1
                else:
                    self.lifepoint[i, 0] = 0
            else:
                if d4 == 3:
                    self.lifepoint[i, 0] = 1
        coner1=newcopy[0,0]
        areacorner1=newcopy[0:2,0:2]
        c1=np.sum(areacorner1)
        if coner1:
            if c1==3 or c1==2:
                self.lifepoint[0,0]=1
            else:
                self.lifepoint[0,0]=0
        else:
            if c1==3:
                self.lifepoint[0,0]=1
        corner2=newcopy[0,self.cols-1]
        areacorner2=newcopy[0:2,self.cols-2:self.cols]
        c2=np.sum(areacorner2)
        if corner2:
            if c2==3 or c2==2:
                self.lifepoint[0,self.cols-1]=1
            else:
                self.lifepoint[0,self.cols-1]=0
        else:
            if c2==3:
                self.lifepoint[0,self.cols-1]=1
        corner3=newcopy[self.cols-1,0]
        areacorner3=newcopy[self.cols-2:self.cols,0:2]
        c3=np.sum(areacorner3)
        if corner3:
            if c3==3 or c3==2:
                self.lifepoint[self.cols-1,0]=1
            else:
                self.lifepoint[self.cols-1,0]=0
        else:
            if c3==3:
                self.lifepoint[self.cols-1, 0]=1
        corner4 = newcopy[self.cols - 1, self.cols-1]
        areacorner4 = newcopy[self.cols - 2:self.cols, self.rows-2:self.rows]
        c4 = np.sum(areacorner4)
        if corner4:
            if c4 == 3 or c4 == 2:
                self.lifepoint[self.cols - 1, self.rows-1] = 1
            else:
                self.lifepoint[self.cols - 1, self.rows-1] = 0
        else:
            if c3 == 3:
                self.lifepoint[self.cols - 1, self.rows-1] = 1
        return self.lifepoint
a=lifegame()
for i in range(10):
    print(a.next())
    print('============================================')
