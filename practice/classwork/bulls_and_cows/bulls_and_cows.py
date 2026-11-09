def is_valid_secret(code):
    if len(code) != 4:
         return False
    if not code.isdigit():
         return False
    if code == 0:
        return False 


    def bulls(secret, guess):
        count = 0
        for i in range (0, 4, 1):
            if secret[i] == guess [i]:
                return i + 1
            return 0;

    def bulls (secret, guess):
        matching = 0
        for digit in guess:
            if digit in secret:
                matching += 1 

        return matching - bulls(secret, guess)

    def cows(secret, guess):
        matching = 0

        for digit in guess:
            if digit in secret:
                matching += 1

            return matching - bulls(secret, guess)


