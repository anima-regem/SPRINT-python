import random, string, pyperclip

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
sym = string.punctuation

all = lower + upper + digit + sym

len = random.randint(8,12)

password = "".join(random.sample(all,len))

pyperclip.copy(password)
print(f"Password Copied to clipboard {password}")
