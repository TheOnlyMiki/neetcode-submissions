class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        题目：给定平面上的点 points 和整数 k，返回离原点 (0, 0) 最近的 k 个点（顺序任意）。

        小提示：
        - 只比较远近，不需要真正的距离，用平方和 x² + y² 即可，省掉开根号也避免浮点误差。
          （所以 euclideanDistance 其实返回的是"距离的平方"，起名 squaredDistance 会更准确）
        - 三种方法对比：
          · Method 1 堆：O(n log k)，不修改数组，适合数据流（数据一个个到来）
          · Method 2 / 3 快速选择：平均 O(n)，但必须一次拿到全部数据，且会打乱数组顺序
        - Method 2 / 3 固定选区间末尾作为 pivot：如果输入已经按距离排好序（或逆序），
          每次分区只能排除一个元素，退化成 O(n²)，递归深度也会达到 n，
          n = 10^4 时可能超过 Python 默认递归上限 1000 而报错。
          改进方法：在 pivot_val 那行之前加两行，随机选一个元素换到末尾：
              pivot_i = random.randint(l, r)
              points[pivot_i], points[r] = points[r], points[pivot_i]
          或者把递归改成 while 循环（每次只往一边走，属于尾递归，可以直接改写）。
        - Method 2 用哈希表预先算好距离，本意是避免重复计算，
          但每次查表都要新建元组 (x, y) 并计算哈希，开销不比直接算 x² + y² 小，
          还额外多了 O(n) 空间，所以实际上不会更快。
          （重复的点会映射到同一个 key，但距离相同，不影响正确性）
        - 堆解法和 LeetCode 703（数据流中第 K 大元素）是同一个技巧的"镜像"：
          · 找前 k 大 → 大小为 k 的最小堆
          · 找前 k 小（最近）→ 大小为 k 的最大堆
        - 快速选择模板可以直接用于 LeetCode 215（数组中第 K 个最大元素）。
        - 其他写法：
          · 排序：sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]，O(n log n)，最简单
          · 标准库：heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)，内部也是堆
        """

        # ==================== Method 3 - 快速选择（Quickselect，递归，末尾作 pivot） ====================
        # 时间复杂度：平均 O(n)，最坏 O(n²)（输入已按距离有序时）
        # 空间复杂度：递归栈平均 O(log n)，最坏 O(n)
        #
        # 思路：快速排序的"半边版"
        # 快排每次分区后要递归处理左右两边；快速选择只处理"目标所在的那一边"，另一边直接丢掉。
        #
        # ---------- 核心操作：分区（partition）----------
        # 选一个元素作为基准 pivot（这里固定选区间末尾），把区间重新排列成：
        #     [ 比 pivot 近的点 ]  pivot  [ 不比 pivot 近的点 ]
        #                          ↑
        #                        下标 p
        # 分区后 pivot 就落在它"排好序后应该在的位置 p"上，
        # 左边都比它近，右边都不比它近（但左右两边内部仍然无序）。
        #
        # ---------- 怎么"选" ----------
        # 目标：让前 k 个位置（下标 0 ~ k-1）恰好放着最近的 k 个点，
        # 也就是让某次分区的 p 正好等于 k - 1：
        # - p == k - 1：左边 k - 1 个都比 pivot 近，加上 pivot 正好 k 个 → 完成
        # - p <  k - 1：最近的 k 个还没凑够，目标在右边 → 只对右半边继续分区
        # - p >  k - 1：左边已经超过 k 个，目标在左边 → 只对左半边继续分区
        #
        # 例：距离为 [5, 1, 8, 3, 9, 2]，k = 3（目标下标 2）
        #     若 pivot = 3：分区后 [1, 2, 3, 5, 9, 8]，p = 2 == k - 1，结束，前 3 个即答案
        #     若 pivot = 8：分区后 [5, 1, 3, 2, 8, 9]，p = 4 > 2，
        #                 只在左边 [5, 1, 3, 2] 里继续找，右边 [9] 完全不用管
        #
        # ---------- 为什么平均是 O(n) ----------
        # 假设 pivot 大致把区间分成两半，每轮只处理一半：n + n/2 + n/4 + … ≈ 2n → O(n)
        # 快排两边都要处理，每层总量都是 n，共 log n 层 → O(n log n)
        # 最坏情况：每次都选到最大或最小值，每轮只排除一个元素 → O(n²)
        #
        # 注意：
        # - 会修改原数组 points 的顺序，如果不允许修改输入，需要先复制一份
        # - 返回的 k 个点之间是无序的（本题允许）；要求有序时还需再排序这 k 个
        # - 这里用 Lomuto 分区，写法最简单；有大量重复距离时效率会下降，
        #   可以换成 Hoare 分区或三路分区（< pivot、== pivot、> pivot）优化

        def euclideanDistance(i, j):
            # 返回距离的平方，足够用来比较远近
            return i**2 + j**2

        def quickSelect(l, r):
            """
            在 points[l..r] 中分区并递归，直到 pivot 落在下标 k-1 处，返回该下标。
            不变量：目标下标 k-1 始终在 [l, r] 区间内，所以 l == r 时一定就是 k-1，不会越界。
            """
            # 选区间末尾作为 pivot
            pivot_val = euclideanDistance(points[r][0], points[r][1])

            # store：下一个"比 pivot 近的点"应该放的位置
            # 循环中始终保持 points[l..store-1] 都比 pivot 近
            store = l
            for i in range(l, r):
                if euclideanDistance(points[i][0], points[i][1]) < pivot_val:
                    points[store], points[i] = points[i], points[store]
                    store += 1

            # 把 pivot 从末尾换到 store，它左边全是更近的点
            points[store], points[r] = points[r], points[store]

            # 根据 pivot 的最终位置，决定往哪一边继续
            if store > k - 1:
                # 左边已经超过 k 个，只在左半边继续找
                return quickSelect(l, store - 1)
            elif store < k - 1:
                # 左边还不够 k 个，只在右半边继续找
                return quickSelect(store + 1, r)
            else:
                # 前 k 个位置正好是最近的 k 个点
                return store

        quickSelect(0, len(points)-1)

        return points[:k]

        # ==================== Method 2 - 快速选择 + 哈希表预存距离 ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留
        # 时间复杂度：平均 O(n)，最坏 O(n²)
        # 空间复杂度 O(n)：哈希表存所有点的距离，另有递归栈
        # 思路与 Method 3 相同，只是事先把每个点的距离算好存进字典，分区时直接查表

        # (x, y) → x² + y²；列表不能作字典的 key，所以转成元组
        record = { (i, j) : i**2 + j**2 for i, j in points }

        def quickSelect(l, r):
            """
            在 points[l..r] 中分区并递归，直到 pivot 落在下标 k-1 处，返回该下标。
            """
            # 选区间末尾作为 pivot，查表得到它的距离
            pivot = (points[r][0], points[r][1])
            pivot_val = record[pivot]

            # store：下一个"比 pivot 近的点"应该放的位置
            # 循环中始终保持 points[l..store-1] 都比 pivot 近
            store = l
            for i in range(l, r):
                if record[(points[i][0], points[i][1])] < pivot_val:
                    points[store], points[i] = points[i], points[store]
                    store += 1

            # 把 pivot 从末尾换到 store，它左边全是更近的点
            points[store], points[r] = points[r], points[store]

            # 根据 pivot 的最终位置，决定往哪一边继续
            if store > k - 1:
                return quickSelect(l, store - 1)
            elif store < k - 1:
                return quickSelect(store + 1, r)
            else:
                return store

        quickSelect(0, len(points)-1)

        return points[:k]

        # ==================== Method 1 - 大小为 k 的最大堆 ====================
        # 时间复杂度 O(n log k)：前 k 个建堆 O(k)，其余每个点最多一次 O(log k) 的堆操作
        # 空间复杂度 O(k)：堆中只存 k 个元素
        # 思路：维护一个大小为 k 的最大堆，保存"目前最近的 k 个点"：
        #      - 堆顶是这 k 个点里离原点最远的
        #      - 新点比堆顶更近 → 把堆顶踢掉，换成新点
        #      - 新点不比堆顶近 → 进不了前 k 近，丢弃
        #      Python 只有最小堆，所以把距离取负存入，最远的点 → 最小的负数 → 在堆顶
        # 堆中存 (负距离, 下标 i)：距离相同时比较 i，i 各不相同，不会比较到更后面的内容

        distances = []

        # ---------- 第 1 步：先把前 k 个点放进堆 ----------
        for i in range(k):
            distances.append((-(points[i][0]**2 + points[i][1]**2), i))

        # 一次性建堆，O(k)，比逐个 push 更快
        heapq.heapify(distances)

        # ---------- 第 2 步：遍历剩下的点，比堆顶更近就替换 ----------
        for i in range(k, len(points)):
            distance = -(points[i][0]**2 + points[i][1]**2)

            # 取负后数值越大表示离原点越近
            # distance > 堆顶 ⇔ 新点比"当前 k 个里最远的点"更近
            if distance > distances[0][0]:
                # 先 push 新点再 pop 堆顶（最远的点），一次 O(log k)
                heapq.heappushpop(distances, (distance, i))

        # ---------- 第 3 步：根据下标取回原始的点 ----------
        output = []

        for _, i in distances:
            output.append(points[i])

        return output