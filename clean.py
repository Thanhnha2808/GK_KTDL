{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bd2acb76-fa24-4677-b9c6-e26ab39be330",
   "metadata": {},
   "outputs": [],
   "source": [
    "# clean_data.py\n",
    "from bs4 import BeautifulSoup\n",
    "from datetime import datetime\n",
    "import re\n",
    "\n",
    "def clean_article(article):\n",
    "    # Loại bỏ HTML nếu còn sót (dùng BeautifulSoup hoặc regex)\n",
    "    article['title'] = BeautifulSoup(article['title'], 'html.parser').get_text(strip=True)\n",
    "    article['summary'] = BeautifulSoup(article['summary'], 'html.parser').get_text(strip=True)\n",
    "\n",
    "    # Chuẩn hóa thời gian (ví dụ: 'Thứ năm, 4/4/2024' → datetime)\n",
    "    try:\n",
    "        article['time'] = datetime.strptime(article['time'], 'Thứ %A, %d/%m/%Y').isoformat()\n",
    "    except Exception:\n",
    "        article['time'] = None\n",
    "\n",
    "    # Loại bỏ các khoảng trắng thừa\n",
    "    article['author'] = re.sub(r'\\s+', ' ', article['author']).strip()\n",
    "\n",
    "    return article\n",
    "\n",
    "def clean_articles(articles):\n",
    "    return [clean_article(article) for article in articles]\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    from crawl_vnexpress import crawl_articles\n",
    "    raw_articles = crawl_articles()\n",
    "    clean_articles_list = clean_articles(raw_articles)\n",
    "\n",
    "    for article in clean_articles_list:\n",
    "        print(article)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca204a3b-a6ec-49e7-b66c-3e65e56af7d8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
