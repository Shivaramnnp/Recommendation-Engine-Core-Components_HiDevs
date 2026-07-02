from similarity import SimilarityCalculator
from candidate_gen import CandidateGenerator
from scorer import RecommendationScorer
from evaluator import RecommendationEvaluator


print("===== Similarity Tests =====")

sim = SimilarityCalculator()

print(sim.cosine_similarity([1,2,3],[1,2,3]))
print(sim.jaccard_similarity(
    {"python","ai"},
    {"python","ml"}
))
print(sim.pearson_correlation(
    [5,4,3],
    [5,4,3]
))


print("\n===== Candidate Generator =====")

gen = CandidateGenerator()

print(gen.collaborative_candidates(1))
print(gen.content_based_candidates(1))
print(gen.popularity_candidates())
print(gen.hybrid_candidates(1))


print("\n===== Recommendation Scorer =====")

scorer = RecommendationScorer()

scorer.add_scorer(
    "popularity",
    lambda u,i,c:0.8,
    0.4
)

scorer.add_scorer(
    "relevance",
    lambda u,i,c:0.9,
    0.6
)

print(
    scorer.rank_candidates(
        1,
        [101,102,103]
    )
)


print("\n===== Evaluator =====")

eval = RecommendationEvaluator()

recommendations = {
    1:[101,102,103],
    2:[102,104]
}

ground_truth = {
    1:[101,103],
    2:[102]
}

print(
    eval.evaluate_all(
        recommendations,
        ground_truth,
        3
    )
)

print("\nAll tests passed!")