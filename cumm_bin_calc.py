from scipy.stats import binom

n = int(input("Enter the value of n: "))
p = float(input("Enter the value of p: "))
k = int(input("Enter the value of k: "))

# Calculate cumulative probability P(X < k)
cumm_prob = binom.cdf(k - 1,n, p)

# Calculate P(X >= k)
prob_X_ge_k = 1 - cumm_prob

print(f"Binomial distribution sum for X >= k : {prob_X_ge_k}")