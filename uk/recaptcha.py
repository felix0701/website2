from django.conf import settings
import requests

def validate_recaptcha(response):
  """Validates a reCAPTCHA response."""

  if response is None or response == "":
    return False

  secret_key = settings.RECAPTCHA_PRIVATE_KEY
  url = "https://www.google.com/recaptcha/api/siteverify"
  data = {
    "secret": secret_key,
    "response": response,
  }
  r = requests.post(url, data=data)
  result = r.json()

  if result["success"]:
    return True
  else:
    return False
