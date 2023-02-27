class Solution(object):
    def construct(self, grid):
        def quard(y, x, len):
            value = grid[y][x]
            flag = True
            root = Node(False, False, None, None, None, None)
            for i in range(len):
                for j in range(len):
                    if grid[y+i][x+j] != value:
                        flag = False
                        root.isLeaf = False
                        next_len = int(len / 2)
                        root.topLeft = quard(y, x, next_len)
                        root.topRight = quard(y, x + next_len, next_len)
                        root.bottomLeft = quard(y + next_len, x, next_len)
                        root.bottomRight = quard(y + next_len, x + next_len, next_len)
                        break
                if flag == False:
                    break
            if flag == True:
                root.isLeaf = True
                root.val = True if value == 1 else False
            return root


        len = int(grid.__len__())
        return quard(0, 0, len)