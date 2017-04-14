"""
题目描述：在经典的汉诺塔问题中，有 3 个塔和 N 个可用来堆砌成塔的不同大小的盘子。要求盘子必须按照从小到大的顺序从上往下堆 （如，任意一个盘子，其必须堆在比它大的盘子上面）。同时，你必须满足以下限制条件：


(1) 每次只能移动一个盘子。
(2) 每个盘子从堆的顶部被移动后，只能置放于下一个堆中。

(3) 每个盘子只能放在比它大的盘子上面。


请写一段程序，实现将第一个堆的盘子移动到最后一个堆中。
"""


class Tower(object):
    # create three towers (i from 0 to 2)
    def __init__(self, i):
        self.disks = []

    # Add a disk into this tower
    def add(self, d):
        if len(self.disks) > 0 and self.disks[-1] <= d:
            print("Error placing disk %s" % d)
        else:
            self.disks.append(d)

    # @param {Tower} t a tower
    # Move the top disk of this tower to the top of t.
    def move_top_to(self, t):
        # Write your code here
        if len(self.disks) > 0:
            t.disks.append(self.disks.pop())

    # @param {int} n an integer
    # @param {Tower} destination a tower
    # @param {Tower} buffer a tower
    # Move n Disks from this tower to destination by buffer tower
    def move_disks(self, n, destination, buffer):
        # Write your code here
        if n == 0:
            return
        if n == 1:
            self.move_top_to(destination)
        else:
            self.move_disks(n - 1, buffer, destination)
            self.move_top_to(destination)
            buffer.move_disks(n - 1, destination, self)

    def get_disks(self):
        return self.disks


"""
Your Tower object will be instantiated and called as such:
towers = [Tower(0), Tower(1), Tower(2)]
for i in xrange(n - 1, -1, -1): towers[0].add(i)
towers[0].move_disks(n, towers[2], towers[1])
print towers[0], towers[1], towers[2]
"""
