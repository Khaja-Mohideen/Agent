import os
import re 
import urllib.parse 

KEYWORDS = (
  "gmail", "email", "email", "mail", 
  "write an email", "send an email", "draft an email",
  "compose an email", "write email", "send mail", "drafty mail",
  "compose mail"
)

def is_email_command(text):
  text = text.lower()
  return any(k in text for k in KEYWORDS)
