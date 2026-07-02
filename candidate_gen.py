class CandidateGenerator:

    def __init__(self):
        self.user_history = {
            1: [101, 102],
            2: [102, 103],
            3: [103, 104]
        }

        self.popular_items = [101, 102, 103, 104, 105]

    def collaborative_candidates(self, user_id):
        if user_id not in self.user_history:
            return self.popular_items[:5]

        result = set()

        history = set(self.user_history[user_id])

        for uid, items in self.user_history.items():
            if uid != user_id and history.intersection(items):
                result.update(items)

        result -= history

        return list(result)[:20]

    def content_based_candidates(self, user_id):
        if user_id not in self.user_history:
            return self.popular_items[:5]

        result = []

        for item in self.user_history[user_id]:
            result.append(item + 100)

        return result[:20]

    def popularity_candidates(self):
        return self.popular_items[:20]

    def hybrid_candidates(self, user_id):
        combined = (
            self.collaborative_candidates(user_id)
            + self.content_based_candidates(user_id)
            + self.popularity_candidates()
        )

        seen = set()
        result = []

        for item in combined:
            if item not in seen:
                seen.add(item)
                result.append(item)

        return result[:20]