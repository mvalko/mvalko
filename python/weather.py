from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://weather.com/weather/5day/08640"
soup = BeautifulSoup(urlopen(url), 'html.parser')

for desc in soup.find_all('td'):
  print(desc.text)
