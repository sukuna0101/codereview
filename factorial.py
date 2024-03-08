def factorial(n):
  """Calculates the factorial of a number."""
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

# Example usage
result = factorial(10)
print(f"The factorial of 10 is: {result}")
