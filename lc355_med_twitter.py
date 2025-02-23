class Twitter:

    def __init__(self):
        self.db = dict()
        self.n_tweets = 0

    def _createUser(self, userId: int) -> None:
        if userId not in self.db:
            self.db[userId] = {
                'tweets': [],
                'following': {userId} # follow yourself
            }

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._createUser(userId)
        self.db[userId]['tweets'].append((self.n_tweets, tweetId))
        self.n_tweets += 1
        # can save on memory by deleting least recent tweets..?

    def getNewsFeed(self, userId: int) -> List[int]:
        self._createUser(userId)
        following = list(self.db[userId]['following'])
        all_tweets = []
        for followeeId in following:
            all_tweets += [(-twt[0], twt[1]) for twt in self.db[followeeId]['tweets']]
        heapify(all_tweets)
        
        ans = []
        i = 0
        LIMIT = 10
        while all_tweets and i < LIMIT:
            ans.append(heappop(all_tweets)[1])
            i += 1
        # print(self.db)
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self._createUser(followerId)
        self._createUser(followeeId)
        self.db[followerId]['following'].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._createUser(followerId)
        self._createUser(followeeId)
        try:
            self.db[followerId]['following'].remove(followeeId)
        except KeyError:
            print(f'{followerId} was not following {followeeId}')