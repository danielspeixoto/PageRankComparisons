# Page Rank - A Monte Carlo approach

PageRank is a famous algorithm initially used by Google to rank web pages in their results. According to Google:

> PageRank works by counting the number and quality of links to a page to determine a rough estimate of how important the website is. The underlying assumption is that more important websites are likely to receive more links from other websites.

In this project we attempt to make the Page Rank faster by using a Monte Carlo Approach. According to Wikipedia, Monte Carlo is defined as: 
> Monte Carlo methods, or Monte Carlo experiments, are a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results.

## Dataset

Facebook Posts. Available at the [WeST website](https://west.uni-koblenz.de/).

- About 47 thousand users
- Approximately 1,750 thousand posts, about 37 per user.

## Algorithm 
Here we present the pseudocode of the approaches, you can view the implementation by checking the source code.

We define a function score() that returns the score for a vertex and N as the amount of vertices we have.

### Conventional Approach

```
A initial vertex S, gets a score of 1. The others get a score of 0.
While there is a vertex V with score above 1/N:
    For each vertex T reachable from V:
        T.score += 0.85 * score(V) / edge_count(V)
    V.score = 0.15 * score(V)
```

### Monte Carlo Approach

For the Monte Carlo approach the precision is defined by us. The more walks we perform, the better the results.

We define C as the amount of walks we will perform

```
From an initial vertex S, we perform C walks
For every walk W from 1 until N:
    do:
        rnd = Random number between 0 and 1
        we move to a random vertex T that can be reached
        T.score += 1
    while rnd < 0.85:

# The scores now need to be normalized
total_score = 0
For every vertex T:
    total_score += T.score

For every vertex T:
    T.score = T.score / total_score
```

## Results

We defined C as 20,000 and already noticed a very good speed up. We can get faster results by reducing C or more accurate by increasing it.

| Approach     | Mean Error | Mean Quadratic Error | Time Spent (ms) |
|--------------|------------|----------------------|-----------------|
| Conventional | -          | -                    | 4431.6          |
| Monte Carlo  | 0.008189   | 0.000245             | 545.2           |