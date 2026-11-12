class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)

        best = right

        while left <= right:
            k = (left + right) // 2

            count = 0
            for pile in piles:
                count += math.ceil(pile/k)

            if count > h:
                left = k + 1
            else:
                best = k
                right = k - 1

        return best

























        
        # 1. 初始化二分查找的边界
        # 速度最小值是 1，最大值是香蕉堆中数量最多的一堆
        left, right = 1, max(piles)
        best_k = right  # 记录最终符合条件的最小速度，初始值设为最大可能速度

        # 2. 开始二分查找
        while left <= right:
            # 取当前的中间值作为测试速度 k
            k = (left + right) // 2
            cur_h = 0
            
            # 3. 计算在当前速度 k 下，吃完所有香蕉所需的总小时数
            for pile in piles:
                # 每一堆需要向上取整，也可以写成更高效的：cur_h += (pile + k - 1) // k
                cur_h += math.ceil(pile / k)

            # 4. 根据耗时调整二分查找的区间
            if cur_h > h:
                # 耗时超过了限制时间 h，说明速度 k 太小了，需要加快速度
                left = k + 1
            else:
                # 耗时满足要求（<= h），k 是一个可行解
                best_k = k       # 记录这个可行解
                right = k - 1    # 尝试寻找有没有更小的可行速度

        # 5. 返回记录下来的最小满足条件的速度
        return best_k
        # 时间复杂度 O(N log M)
        # 其中 N 是 piles 的长度，M 是 piles 中的最大值 max(piles)。
        # 二分查找的区间大小为 M，因此循环执行 log M 次；每次循环内部都需要遍历整个 piles 数组计算总耗时，耗时 O(N)。
        #
        # 空间复杂度 O(1)
        # 算法只使用了常数级别的额外空间（如 left, right, best_k, k, cur_h 等变量），不随输入规模增长。