from modules.gsheet_reader import read_links_from_column_j
from modules.selenium_scraper import scrape_case_dates
from modules.gsheet_uploader import upload_to_google_sheet

if __name__ == "__main__":
    # 1. Read links from column J in spreadsheet
    links = read_links_from_column_j()
    print("Links fetched:", links)

    # 2. Use those links to scrape case status dates
    col = scrape_case_dates(links)
    print("Scraped case dates:", col)

    # 3. Upload those dates back to the sheet (starting from G2)
    upload_to_google_sheet(col)
    print("Upload complete.")
