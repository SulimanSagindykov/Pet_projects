import pyshorteners

url = input("The URL to shorten: ")

variable = pyshorteners.Shortener(api_key='e508503270241cc9dc43e953fd50d725746e894e')
shortened_url = variable.bitly.short('https://www.google.com')

print(f"The Shortened URL: {shortened_url}")