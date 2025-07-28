from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_case_dates(links):
    driver = webdriver.Firefox()
    driver.get("https://district.mphc.gov.in")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/en/case-status"]'))
    ).click()
    # ---- Initial setup to establish session/cookies ----
    # This dummy case search ensures the site initializes session state properly
    # Required before we can access case pages directly via links
    Select(driver.find_element(By.ID, "menu_dist1")).select_by_value("Indore")
    Select(driver.find_element(By.NAME, "selctype")).select_by_value("206")

    driver.find_element(By.ID, "caseno").send_keys("3943236")
    driver.find_element(By.NAME, "caseyear").send_keys("2016")
    driver.find_element(By.NAME, "search").click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "td"))
    )

    col = []

    for url in links:
        driver.get(url)

        try:
            # Wait until at least 13 <td> elements are loaded and the 13th one is not empty
            WebDriverWait(driver, 20).until(
                lambda d: len(d.find_elements(By.TAG_NAME, "td")) > 12 and
                        d.find_elements(By.TAG_NAME, "td")[12].text.strip() != ""
            )
            tds = driver.find_elements(By.TAG_NAME, "td")
            col.append([tds[12].text.strip()])
        except Exception:
            col.append(["Not Found"])

    driver.quit()
    return col
