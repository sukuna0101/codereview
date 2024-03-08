def find_factors(num):
  """Finds all factors of a number."""
  factors = []
  for i in range(1, num + 1):
    if num % i == 0:
      factors.append(i)
  return factors

# Example usage
factors = find_factors(10)
print(f"The factors of 10 are: {factors}")  # Output: The factors of 10 are: [1, 2, 5, 10]
