{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "bdab76db-48df-4f17-88d1-2f7a252cb70b",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "def crawl_articles():\n",
    "    url = \"https://vnexpress.net/cong-nghe/ai\"\n",
    "    response = requests.get(url)\n",
    "    soup = BeautifulSoup(response.text, \"html.parser\")\n",
    "\n",
    "    articles = []\n",
    "    items = soup.select(\".box-category-item\")[:5]  # lấy 5 bài đầu tiên\n",
    "\n",
    "    for item in items:\n",
    "        title_tag = item.select_one(\"h3.title-news a\")\n",
    "        title = title_tag.get_text(strip=True) if title_tag else None\n",
    "        article_url = title_tag['href'] if title_tag else None\n",
    "\n",
    "        summary_tag = item.select_one(\"p.description\")\n",
    "        summary = summary_tag.get_text(strip=True) if summary_tag else None\n",
    "\n",
    "        time_tag = item.select_one(\"span.time\")\n",
    "        time = time_tag.get_text(strip=True) if time_tag else None\n",
    "\n",
    "        # Vào trang bài viết để lấy tên tác giả\n",
    "        author = None\n",
    "        if article_url:\n",
    "            article_res = requests.get(article_url)\n",
    "            article_soup = BeautifulSoup(article_res.text, \"html.parser\")\n",
    "            author_tag = article_soup.select_one(\"p.Normal[style*='text-align:right']\")\n",
    "            author = author_tag.get_text(strip=True) if author_tag else \"Không rõ\"\n",
    "\n",
    "        articles.append({\n",
    "            \"title\": title,\n",
    "            \"url\": article_url,\n",
    "            \"summary\": summary,\n",
    "            \"time\": time,\n",
    "            \"author\": author\n",
    "        })\n",
    "\n",
    "    return articles\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    articles = crawl_articles()\n",
    "    for art in articles:\n",
    "        print(art)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d649f437-ff51-4a5c-8c72-dd99799e4375",
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
