# import requests
# # from bs4 import BeautifulSoup
# # import csv

# # # Step 1: Fetch and parse the webpage
# # url = "https://www.basketball-reference.com/players/j/jamesle01/gamelog/2025"
# # response = requests.get(url)
# # soup = BeautifulSoup(response.text, 'html.parser')

# # # Step 2: Extract data
# # books = []
# # for book in soup.find_all('article', class_='product_pod'):
# #     title = book.h3.a['title']
# #     price = book.find('p', class_='price_color').text
# #     books.append({'Title': title, 'Price': price})

# # # Step 3: Save data to a CSV file
# # with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
# #     writer = csv.DictWriter(file, fieldnames=['Title', 'Price'])
# #     writer.writeheader()
# #     writer.writerows(books)

# # print("Data saved to books.csv")

# # Using BeautifulSoup
# from bs4 import BeautifulSoup

# # Step 1: Fetch and parse the webpage
# url = "https://www.basketball-reference.com/players/j/jamesle01/gamelog/2025"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# # # Target the div by class
# # target = soup.find('div', class_='go367056303')
# # print(target.text)  # Prints the content inside this div


# target = soup.find('div', class_='bbr')   
# if target:
#     print(target.text)
# else:
#     print("Element not found!")


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the webpage
url = "https://www.basketball-reference.com/players/j/jamesle01/gamelog/2004"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    exit()

# Step 2: Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Locate the game log table
table = soup.find('table', id='pgl_basic')

# Step 4: Extract headers
headers = [th.getText() for th in table.find('thead').find_all('th')]
headers = headers[1:]  # Skip the first header as it's a row number

# Step 5: Extract game data
rows = table.find('tbody').find_all('tr')
game_data = []

for row in rows:
    if row.get('class') and 'thead' in row.get('class'):
        continue  # Skip header rows within the body
    cols = row.find_all('td')
    if not cols:
        continue  # Skip rows without data
    game = [col.getText() for col in cols]
    game_data.append(game)

# Step 6: Create DataFrame and save to CSV
df = pd.DataFrame(game_data, columns=headers)
df.to_csv('lebron_james_2004_gamelog.csv', index=False)
print("Data saved to lebron_james_2004_gamelog.csv")