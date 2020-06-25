import re


phone_text = "This is my number 31-687-916-179 and i use it since 3 years"
email_text = "This is my e-mail ondereren83@gmail.com and i use it for 10 years sonereren@hotmail.com"

pattern_phone = r"\d{2}-\d{3}-\d{3}-\d{3}"
pattern_email = r"\w+@\w+.\w+"

result_phone = re.findall(pattern_phone, phone_text)
result_email = re.findall(pattern_email, email_text)

print(result_phone)
print(f"address: {[email.split('@')[0] for email in result_email]} provider: {[email.split('@')[1] for email in result_email]}")
