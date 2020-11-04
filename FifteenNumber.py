#coding:utf-8
import copy

class FiftheenNumber(object):

    def begin_number(self, nums):
        """检测初始节点是否符合要求 """
        for num in nums:
            if 0 not in num:
                return True
        return False

    def point(self, nums, tn):
        """返回节点tn数码的坐标"""
        a, b = 0, 0
        for i in range(len(nums)):
            if tn in nums[i]:
                a = i
                b = nums[i].index(tn)
        return a, b

    def compare_number(self, nums, target):
        """将当前节点与目标节点进行比较"""
        if nums == target:
            return True
        return False

    def move_left(self, nums):
        """0向左移动一位"""
        a, b = self.point(nums,0)
        if b == 0:
            return None
        nums[a][b],nums[a][b-1] = nums[a][b-1],nums[a][b]
        return nums

    def move_right(self,nums):
        """0向右移动一位"""
        a, b = self.point(nums,0)
        if b == len(nums[0])-1:
            return None
        nums[a][b], nums[a][b + 1] = nums[a][b + 1], nums[a][b]
        return nums

    def move_up(self, nums):
        """0向上移动一位"""
        a, b = self.point(nums,0)
        if a == 0:
            return None
        nums[a][b], nums[a-1][b] = nums[a-1][b], nums[a][b]
        return nums

    def move_down(self, nums):
        """0向下移动一位"""
        a, b = self.point(nums,0)
        if a == len(nums)-1:
            return None
        nums[a][b], nums[a+1][b] = nums[a + 1][b], nums[a][b]
        return nums

    def get_value(self, nums, target):
        """计算数码“不在位”的距离和"""
        # print(nums)
        wn = 0
        for i in range(1,16):
            x1, y1 = self.point(nums,i)
            x2, y2 = self.point(target,  i)
            wn += abs(x1-x2) + abs(y1-y2)
        return wn

    def get_value1(self,nums,target):
        """计算数码”不在位“个数之和"""
        wn = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if nums[i][j] != target[i][j]:
                    wn += 1
        return wn

    def bea_print(self,nums):
        """矩阵打印"""
        for num in nums:
            for i in num:
                print(i,end=" ")
            print("\n")
        print("\n")

if __name__ == '__main__':
    S0 = [[11, 9, 4, 15],
          [1, 3, 0, 12],
          [7, 5, 8, 6],
          [13, 2, 10, 14]]
    Sg = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 0]]
    # S0 = [[2,8,3],
    #       [1,0,4],
    #       [7,6,5]]
    # Sg = [[1,2,3],
    #       [8,0,4],
    #       [7,6,5]]
    fif = FiftheenNumber()
    # print(fif.get_value1(S0,Sg))
    fif.bea_print(S0)
    if fif.begin_number(S0) and fif.begin_number(Sg):
        open = []#定义OPEN表
        open.append(S0)
        last = [True,True,True,True]
        fn = []
        fn.append(fif.get_value(S0,Sg))
        closed = []#定义CLOSED表
        deep = [0]#保存节点深度
        i = 0
        while not fif.compare_number(open[fn.index(min(fn))],Sg):
            if not open:
                print("无解")
            yin = []
            # print(len(open))
            pon = open.pop(fn.index(min(fn)))#找到OPEN表中估值函数最小的节点
            # print(pon)
            deepv = deep[fn.index(min(fn))]
            deepv += 1
            # print(deepv)
            x = fn.pop(fn.index(min(fn)))
            if pon in closed:
                continue

            i += 1
            closed.append(pon)
            #节点扩展
            up = copy.deepcopy(pon)
            if fif.move_up(nums=up) and last[0]:
                fn.append(fif.get_value1(up, Sg)+deepv)
                open.append(up)
                yin.append("up")
                deep.append(deepv)
            down = copy.deepcopy(pon)
            if fif.move_down(down) and last[1]:
                fn.append(fif.get_value1(down, Sg)+deepv)
                open.append(down)
                yin.append("down")
                deep.append(deepv)
                # print(res1)
            left = copy.deepcopy(pon)
            if fif.move_left(left) and last[2]:
                fn.append(fif.get_value1(left, Sg)+deepv)
                open.append(left)
                yin.append("left")
                deep.append(deepv)
            right = copy.deepcopy(pon)
            if fif.move_right(right) and last[3]:
                fn.append(fif.get_value1(right, Sg)+deepv)
                open.append(right)
                yin.append("right")
                deep.append(deepv)
            fif.bea_print(open[fn.index(min(fn))])
        print(i)
