from bs4 import BeautifulSoup as soup
cleaned_text = soup.get_text(separator='\n', strip=True)

print(cleaned_text)
