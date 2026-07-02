import math


class RecommendationEvaluator:

    def precision_at_k(self, recommendations, relevant_items, k):

        if not recommendations:
            return 0

        top = recommendations[:k]

        hits = len(set(top) & set(relevant_items))

        return hits / k

    def recall_at_k(self, recommendations, relevant_items, k):

        if not relevant_items:
            return 0

        top = recommendations[:k]

        hits = len(set(top) & set(relevant_items))

        return hits / len(relevant_items)

    def ndcg_at_k(self, recommendations, relevant_items, k):

        dcg = 0

        for i, item in enumerate(recommendations[:k]):
            if item in relevant_items:
                dcg += 1 / math.log2(i + 2)

        ideal = min(len(relevant_items), k)

        idcg = sum(1 / math.log2(i + 2)
                   for i in range(ideal))

        if idcg == 0:
            return 0

        return dcg / idcg

    def evaluate_all(self, recommendations_dict,
                     ground_truth_dict,
                     k=5):

        precision = []
        recall = []
        ndcg = []

        for user, recs in recommendations_dict.items():

            truth = ground_truth_dict.get(user, [])

            precision.append(
                self.precision_at_k(recs, truth, k)
            )

            recall.append(
                self.recall_at_k(recs, truth, k)
            )

            ndcg.append(
                self.ndcg_at_k(recs, truth, k)
            )

        n = len(recommendations_dict)

        if n == 0:
            return {
                "precision": 0,
                "recall": 0,
                "ndcg": 0
            }

        return {
            "precision": round(sum(precision)/n,3),
            "recall": round(sum(recall)/n,3),
            "ndcg": round(sum(ndcg)/n,3)
        }