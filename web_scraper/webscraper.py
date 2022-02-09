from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys
import requests
from bs4 import BeautifulSoup


pokemondb_url = "https://pokemondb.net/pokedex/national"
response = requests.get(pokemondb_url)
nationaldex_page = response.text
soup = BeautifulSoup(nationaldex_page, "html.parser")
print(soup.prettify())
pokemon_name_soup = soup.find_all(name="a", class_="ent-name")
pokemon_name_list = [pokemon_name.text.strip() for pokemon_name in pokemon_name_soup]

#Will eventually work on scraping these pieces of data
# pokemon_type_soup = soup.find_all(name="small a")
# pokemon_type_list = [pokemon_type.text.strip() for pokemon_type in pokemon_type_soup]
#
# pokemon_number_soup = soup.find_all(name="a", class_="ent-name")
# pokemon_number_list = [pokemon_type.number.strip() for pokemon_type in pokemon_number_soup]
#
# pokemon_img_soup = soup.find_all(name="a", class_="ent-name")
# pokemon_img_list = [pokemon_img.text.strip() for pokemon_img in pokemon_img_soup]


# print(pokemon_type_soup)
#
# print(pokemon_name_list)