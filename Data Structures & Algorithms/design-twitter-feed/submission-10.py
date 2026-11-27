class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        
        self.tweetMap = defaultdict(deque)

        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:

        if len(self.tweetMap[userId]) == 10:
            self.tweetMap[userId].popleft()

        self.tweetMap[userId].append((self.timestamp, tweetId))

        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        output = []

        self.followMap[userId].add(userId)

        max_heap = []

        for user in self.followMap[userId]:
            if self.tweetMap[user]:
                recent, tweetId = self.tweetMap[user][-1]
                heapq.heappush(max_heap, (-recent, tweetId, len(self.tweetMap[user])-1, user))

        while len(output) != 10 and max_heap:

            recent, tweetId, i, user = heapq.heappop(max_heap)

            output.append(tweetId)

            if i != 0:
                recent, tweetId = self.tweetMap[user][i-1]
                heapq.heappush(max_heap, (-recent, tweetId, i-1, user))

        return output


    def follow(self, followerId: int, followeeId: int) -> None:

        if followeeId not in self.followMap[followerId]:
            self.followMap[followerId].add(followeeId)

        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        return
