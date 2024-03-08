def is_prime(num):
  """Checks if a number is prime."""
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

prime_numbers = []
for num in range(1, 26):
  if is_prime(num):
    prime_numbers.append(num)

print(f"Prime numbers between 1 and 25: {prime_numbers}")
