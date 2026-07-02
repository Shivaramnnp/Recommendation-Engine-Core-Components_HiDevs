import math


class SimilarityCalculator:
    def cosine_similarity(self, vec1, vec2):
        if len(vec1) != len(vec2) or len(vec1) == 0:
            return 0.0

        dot = sum(a * b for a, b in zip(vec1, vec2))
        mag1 = math.sqrt(sum(a * a for a in vec1))
        mag2 = math.sqrt(sum(b * b for b in vec2))

        if mag1 == 0 or mag2 == 0:
            return 0.0

        return dot / (mag1 * mag2)

    def jaccard_similarity(self, set1, set2):
        if not set1 and not set2:
            return 1.0

        union = set1 | set2
        if not union:
            return 0.0

        return len(set1 & set2) / len(union)

    def pearson_correlation(self, ratings1, ratings2):
        if len(ratings1) != len(ratings2) or len(ratings1) == 0:
            return 0.0

        n = len(ratings1)

        mean1 = sum(ratings1) / n
        mean2 = sum(ratings2) / n

        num = sum((a - mean1) * (b - mean2)
                  for a, b in zip(ratings1, ratings2))

        den1 = math.sqrt(sum((a - mean1) ** 2 for a in ratings1))
        den2 = math.sqrt(sum((b - mean2) ** 2 for b in ratings2))

        if den1 == 0 or den2 == 0:
            return 0.0

        return num / (den1 * den2)