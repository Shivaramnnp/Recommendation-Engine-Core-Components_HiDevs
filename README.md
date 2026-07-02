# Recommendation Engine Core Components

A modular recommendation engine built in Python that demonstrates the core algorithms used by modern recommendation systems.

## Features

### 1. Similarity Calculator
Implements multiple similarity metrics:

- Cosine Similarity
- Jaccard Similarity
- Pearson Correlation

Handles edge cases such as:
- Empty vectors
- Zero vectors
- Empty sets

---

### 2. Candidate Generator

Generates recommendation candidates using multiple approaches:

- Collaborative Filtering
- Content-Based Filtering
- Popularity-Based Recommendation
- Hybrid Recommendation

Supports cold-start users and configurable candidate limits.

---

### 3. Recommendation Scorer

Ranks recommendation candidates using weighted scoring.

Supports multiple scoring functions including:

- Relevance
- Popularity
- Recency
- Custom scorers

Produces ranked recommendations with explanations.

---

### 4. Recommendation Evaluator

Evaluates recommendation quality using standard ranking metrics.

Implemented metrics:

- Precision@K
- Recall@K
- NDCG@K

Provides overall evaluation statistics.

---

## Project Structure

```
day29_project/
│
├── similarity.py
├── candidate_gen.py
├── scorer.py
├── evaluator.py
├── test.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
cd day29_project
```

(Optional)

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

Windows

```bash
venv\Scripts\activate
```

macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Run Tests

```bash
python test.py
```

---

## Concepts Demonstrated

- Recommendation Systems
- Similarity Algorithms
- Candidate Generation
- Ranking Algorithms
- Evaluation Metrics
- Object-Oriented Programming
- Modular Python Design

---

## Technologies Used

- Python 3.11+
- math
- heapq
- collections
- statistics
- unittest

---

## Future Improvements

- Matrix Factorization
- Neural Recommendation Models
- Approximate Nearest Neighbor Search
- Real User Dataset Support
- REST API Integration
- Database Support
- Personalized User Profiles

---

## Author

**Shivaram Patel**

LinkedIn:
https://www.linkedin.com/in/shivaramnnp/

GitHub:
https://github.com/Shivaramnnp

---

## License

This project is created for educational and learning purposes.