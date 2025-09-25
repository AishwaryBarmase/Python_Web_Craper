import requests
from bs4 import BeautifulSoup
import os

def scrape_and_save_rediff_headlines():

    url = 'https://www.rediff.com/news'
    headlines_list = []

    try:
        response = requests.get(url)

        response.raise_for_status()


        soup = BeautifulSoup(response.content, 'html.parser')


        all_links = soup.find_all('a')

        for link in all_links:
            href = link.get('href', '')
            headline_text = link.text.strip()


            if ('/news/' in href or '/headlines/' in href or '/stories/' in href) and len(headline_text) > 20:

                if headline_text not in headlines_list:
                    headlines_list.append(headline_text)

        if not headlines_list:
            print("No headlines found. The website's structure may have changed, or there were no headlines available.")
            return

        documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
        output_file = os.path.join(documents_path, 'rediff_headlines.txt')

        with open(output_file, 'w', encoding='utf-8') as f:
            for headline in headlines_list:
                f.write(headline + '\n')

        print(f"Successfully scraped {len(headlines_list)} headlines.")
        print(f"Headlines saved to: {output_file}")

    except requests.exceptions.RequestException as e:

        print(f"An error occurred while connecting to the website: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    scrape_and_save_rediff_headlines()
