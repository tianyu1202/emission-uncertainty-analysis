import numpy as np
import scipy.stats as stats

# Original data and added noise
x = 3.60  # Assume original data
sigma = 0.12 * x  # Set standard deviation to 12% of the original data based on literature review
noise = np.random.normal(0, sigma, 10000)  # Generate 10,000 noise samples
samples = x + noise  # Generate new data points

# Compute log values, log mean, and log standard deviation
log_samples = np.log(samples)  # Log transformation
log_mean = np.mean(log_samples)  # Log mean
log_std = np.std(log_samples)  # Log standard deviation

# Generate log-normal distributed emission samples
log_normal_samples = np.random.lognormal(log_mean, log_std, 10000)

# Calculate 95% confidence interval
ci_lower, ci_upper = np.percentile(log_normal_samples, [2.5, 97.5])  # 95% CI

# Calculate uncertainty
uncertainty_lower = (ci_lower - x) / x  # Uncertainty relative to original value (lower bound)
uncertainty_upper = (ci_upper - x) / x  # Uncertainty relative to original value (upper bound)

print(f"Original value: {x}")
print(f"Log mean: {log_mean}")
print(f"Log standard deviation: {log_std}")
print(f"95% confidence interval: ({ci_lower}, {ci_upper})")
print(f"Uncertainty (lower bound): {uncertainty_lower * 100:.2f}%")
print(f"Uncertainty (upper bound): {uncertainty_upper * 100:.2f}%")
