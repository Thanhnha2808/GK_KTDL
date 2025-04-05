import requests
from bs4 import BeautifulSoup


page_url = 'https://vnexpress.net/cong-nghe/ai'


response = requests.get(page_url)
soup = BeautifulSoup(response.content, 'html.parser')

bai_viets = soup.find_all('a', class_='thumb')


for bai_viet in bai_viets[:5]: 
    url = article['href']
    title = article['title'] if article.get('title') else "Không tìm thấy tiêu đề"
    summary_tag = article.find_next('p', class_='description')
    summary = summary_tag.text.strip() if summary_tag else "Không có tóm tắt"
    
    
    response = requests.get(url)
    soup1 = BeautifulSoup(response.content, 'html.parser')
    date = soup1.find('span', class_='date')
    date_text = date.text.strip() if date else "Không tìm thấy ngày tháng"
    print(f"Title: {title}")
    print(f"URL: {url}")
    print(f"Summary: {summary}")
    print(f"Time: {date_text}")
    print('-' * 50)
