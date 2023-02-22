secret_number = 10
attempts = 0
attempt_limit = 3

while attempts < attempt_limit:
	guess = int(input("Guess the number? "))
	attempts += 1
	if guess == secret_number:
		print("You win!")
	  break
else:
  print("You lost!")
