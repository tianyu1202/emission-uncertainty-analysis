# emission-uncertainty-analysis
This notebook estimates the uncertainty range of an emission value using a log-normal distribution model.

## Method

1. Start from a baseline emission value (e.g., 3.60).
2. Simulate 10,000 noisy measurements using a Gaussian noise (10% std).
3. Apply log transformation and compute log-mean and log-std.
4. Generate synthetic emission values using log-normal distribution.
5. Estimate the 95% confidence interval.
6. Calculate relative uncertainty compared to original value.

## Requirements

- numpy
- scipy


