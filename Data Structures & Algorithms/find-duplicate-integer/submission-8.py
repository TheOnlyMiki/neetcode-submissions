class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        题目：数组 nums 长度为 n + 1，元素都在 [1, n] 范围内，
             只有一个数字重复（可能重复多次），找出它。
        进阶要求：不修改数组，且只用 O(1) 额外空间。
        """

        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break

        return slow

        # ==================== Method 5 - 二分查找（对值域二分） ====================
        # 时间复杂度 O(n log n)，空间复杂度 O(1)，不修改数组 —— 满足进阶要求
        # 思路：不是对下标二分，而是对"答案可能的取值" [1, n] 二分
        #
        # 定义 count(mid) = 数组中 <= mid 的元素个数，设重复数为 d：
        # - mid < d 时：[1, mid] 里的数都不重复，最多各出现一次 → count(mid) <= mid
        # - mid >= d 时：d 多出现的次数一定能补上缺失的数还有富余 → count(mid) > mid
        #   （d 出现 k 次，则 [1, n] 中最多缺 k - 2 个数，
        #     count(mid) >= mid - (k - 2) + (k - 1) = mid + 1）
        # 所以 "count(mid) > mid" 是单调的：在 d 左边全为 False，从 d 开始全为 True
        # 问题变成：找第一个使 count(mid) > mid 成立的 mid
        # 例：nums = [1,3,4,2,2]，n = 4
        #     mid:        1  2  3  4
        #     count(mid): 1  3  4  5
        #     > mid ?     F  T  T  T   → 第一个 True 是 2

        left, right = 1, len(nums) - 1   # 值域 [1, n]，n = len(nums) - 1

        # 左闭右闭区间收缩，left == right 时就是答案
        while left < right:
            mid = (left + right) // 2

            # 统计 <= mid 的元素个数，每轮 O(n)
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count > mid:
                # [1, mid] 里"挤"进了太多数 → 重复数在 [left, mid] 中
                # mid 本身可能就是答案，所以 right = mid 而不是 mid - 1
                right = mid
            else:
                # [1, mid] 里没有重复 → 重复数在 [mid + 1, right] 中
                left = mid + 1

        return left

        # ==================== Method 4 - 快慢指针（Floyd 判圈） ====================
        # 时间复杂度 O(n)，空间复杂度 O(1)，不修改数组 —— 唯一满足全部要求的方法

        # 核心转化：把数组看成链表，下标 i 的"下一个节点"是 nums[i]，即 i → nums[i]
        # - 一共 n + 1 个下标，但值只有 [1, n] 共 n 种，必然有两个下标指向同一个值
        #   → 有两个节点的 next 相同 → 链表中一定有环
        # - 环的入口就是"被多个下标指向的那个值"，也就是重复的数字
        # - 值都 >= 1，没有任何下标会指向 0，所以从 0 出发一定在环外，保证能走到入口
        # 例：nums = [1,3,4,2,2]
        #     0 → 1 → 3 → 2 → 4 → 2 → 4 → ...   环为 2 ⇄ 4，入口是 2

        # ---------- 第 1 步：快慢指针找相遇点 ----------
        # slow 每次走一步，fast 每次走两步，二者必在环内相遇
        slow, fast = 0, 0

        while True:
            slow = nums[slow]          # 走一步
            fast = nums[nums[fast]]    # 走两步
            if slow == fast:
                break

        # ---------- 第 2 步：找环的入口 ----------
        # 设：起点到入口距离 a，入口到相遇点距离 b，环长 c
        #     相遇时 slow 走了 a + b，fast 走了 2(a + b)
        #     fast 比 slow 多走整数圈：(a + b) = k * c  ⇒  a = k * c - b
        # 含义：从相遇点再走 a 步，恰好回到入口（多走 k 圈减去 b）
        # 所以让一个指针从起点、一个从相遇点，同速前进，相遇处就是入口
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break

        # 入口节点的编号就是重复的数字
        return slow

        # ==================== Method 3 - 原地标记为负数 ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留
        # 时间复杂度 O(n)，空间复杂度 O(1)，但会修改数组（不符合题目进阶要求）
        # 思路：把"数字 x 出现过"记录在下标 x - 1 上，用负号作为标记

        for num in nums:
            # num 可能已经被之前的操作变成负数，所以要取绝对值才是原本的值
            i = abs(num) - 1      # 值 [1, n] 映射到下标 [0, n-1]

            # 该位置已经是负数，说明这个数之前出现过 → 就是重复数
            if nums[i] < 0:
                return abs(num)

            # 第一次出现，做标记
            nums[i] *= -1

        return -1   # 按题意一定有重复，不会走到这里

        # ==================== Method 2 - 排序后比较相邻元素 ====================
        # 时间复杂度 O(n log n)
        # sorted() 会生成新列表，空间 O(n)；若改用 nums.sort() 则会修改原数组
        # （而且 Python 的 Timsort 最坏也需要 O(n) 额外空间），都不满足进阶要求

        nums = sorted(nums)

        # 初始化为一个一定不等于 nums[0] 的值，避免第一次比较误判
        pre_num = nums[0] - 1

        # 排序后相同的数一定相邻，只需比较当前数与前一个数
        for num in nums:
            if num == pre_num:
                return num
            pre_num = num

        return

        # ==================== Method 1 - 哈希集合 ====================
        # 时间复杂度 O(n)，空间复杂度 O(n)
        # 思路：边遍历边记录见过的数，第一次遇到已见过的就是重复数

        record = set()

        for num in nums:
            if num in record:
                return num
            record.add(num)

        return