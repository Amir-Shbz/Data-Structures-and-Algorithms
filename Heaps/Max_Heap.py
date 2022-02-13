class Maxheap():
    def __init__(self):
        self.nodelist = []

    def insert(self, x):
        self.nodelist.append(x)

        l = len(self.nodelist)
        i = l - 1
        while i != 0:
            j = int((i+1)/2)
            if self.nodelist[j-1] < x:
                y = self.nodelist[j-1]
                self.nodelist[j-1] = x
                self.nodelist[i] = y
                i = j-1
            else:
                break

    def show(self):
        for i in self.nodelist:
            print(i, end=" ")
        print("\n")

    def delete(self):

        l = len(self.nodelist)
        self.nodelist[0] = self.nodelist[l-1]
        self.nodelist.pop()
        l -= 1

        j = 1
        while 2*j <= l:
            jleft = 2*j
            jright = 2*j+1

            if jleft <= l:
                if jright <= l:
                    if self.nodelist[jleft-1] > self.nodelist[jright-1]:
                        x = self.nodelist[j-1]
                        self.nodelist[j-1] = self.nodelist[jleft-1]
                        self.nodelist[jleft-1] = x
                        j = jleft

                    elif self.nodelist[jright-1] > self.nodelist[jleft-1]:
                        x = self.nodelist[j-1]
                        self.nodelist[j-1] = self.nodelist[jright-1]
                        self.nodelist[jright-1] = x
                        j = jright

                else:
                    x = self.nodelist[j-1]
                    self.nodelist[j-1] = self.nodelist[jleft-1]
                    self.nodelist[jleft-1] = x
                    j = jleft

        self.show()
