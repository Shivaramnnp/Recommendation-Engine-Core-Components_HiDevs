class RecommendationScorer:

    def __init__(self):
        self.scorers = []

    def add_scorer(self, name, function, weight):
        self.scorers.append((name, function, weight))

    def calculate_score(self, user_id, item_id, context):

        total = 0
        total_weight = 0

        explanations = []

        for name, func, weight in self.scorers:
            value = func(user_id, item_id, context)
            total += value * weight
            total_weight += weight

            explanations.append(f"{name}:{value:.2f}")

        if total_weight == 0:
            score = 0
        else:
            score = total / total_weight

        return {
            "score": round(score, 3),
            "explanation": ", ".join(explanations)
        }

    def rank_candidates(self, user_id, candidates, limit=5):

        scored = []

        for item in candidates:
            data = self.calculate_score(user_id, item, {})
            scored.append((item, data["score"], data["explanation"]))

        scored.sort(key=lambda x: x[1], reverse=True)

        return scored[:limit]