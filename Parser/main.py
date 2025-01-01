import time
import csv
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import os

def parse_jobs(url: str, max_items: int):
    create_csv()
    driver = webdriver.Chrome()  
    
    # Timeout of 10 seconds, value depends on your pc sprec, you can decrease it for better speed 
    wait = WebDriverWait(driver, 10)  
    driver.get(url)

    # Set to store unique links
    processed_links = set()  
    count_items = 0

    while count_items < max_items:
        try:
            # Click "Load more" button if available
            load_more_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.tw-btn.tw-btn-primary.tw-block.tw-btn-xl"))
            )
            actions = ActionChains(driver)
            actions.move_to_element(load_more_button).click().perform()
            time.sleep(2)  
        except Exception as e:
            print(f"'Load more' button unavailable: {str(e)}")
            break

        # Parse the current page
        soup = BeautifulSoup(driver.page_source, "lxml")
        postings = soup.find_all("a", class_="posting-list-item")

        job_list = []
        for posting in postings:
            if count_items >= max_items:
                break

            job_link = extract_job_link(posting)
            if not job_link or job_link in processed_links:
                continue

            processed_links.add(job_link)  # Add link to the set
            count_items += 1

            title = extract_job_title(posting)
            location = extract_location(posting)
            salary_min, salary_max = extract_salary(posting)
            technologies = extract_technologies(posting)
            company_name = extract_company_name(posting)
            seniority = get_seniority(job_link)

            # Add data to the list
            job_list.append([title, location, salary_min, salary_max, technologies, company_name, seniority, job_link])

        write_csv(job_list)

    driver.quit()

def extract_job_link(posting):
    job_link = posting.get("href")
    if job_link and job_link.startswith("/"):
        return f"https://nofluffjobs.com{job_link}"
    return None

def extract_job_title(posting):
    title_elem = posting.find("h3", class_="posting-title__position ng-star-inserted")
    return title_elem.text.strip() if title_elem else "Not specified"

def extract_location(posting):
    location_elem = posting.find("span", class_="tw-text-ellipsis tw-inline-block tw-overflow-hidden tw-whitespace-nowrap tw-max-w-[100px] md:tw-max-w-[200px] tw-text-right")
    return location_elem.text.strip() if location_elem else "Not specified"

def extract_salary(posting):
    salary_elem = posting.find_all("span", class_="posting-tag tw-cursor-pointer ng-star-inserted")
    if len(salary_elem) > 0:
        salary_range = salary_elem[0].text.strip()
        if "–" in salary_range:
            salary_min, salary_max = salary_range.split("\u2013")
            salary_min = salary_min.strip().replace("PLN", "").replace(" ", "")
            salary_max = salary_max.strip().replace("PLN", "").replace(" ", "")
        else:
            salary_min = salary_max = salary_range.replace("PLN", "").replace(" ", "")
    else:
        salary_min = salary_max = "Not specified"
    return salary_min, salary_max

def extract_technologies(posting):
    tech_elem = posting.find("div", class_="tiles-container desktop:tw-w-[59%]")
    if tech_elem:
        technologies = ", ".join([tech.text.strip() for tech in tech_elem.find_all("span")])
        return re.sub(r"\+1|\b(?:additional|other)\b", "", technologies).strip()
    return "Not specified"

def extract_company_name(posting):
    company_elem = posting.find("h4", class_="company-name tw-mb-0")
    return company_elem.text.strip() if company_elem else "Not specified"

def get_seniority(job_url: str):
    """Fetches seniority level from the job page."""
    response = requests.get(job_url)
    if response.status_code != 200:
        return "Failed to fetch seniority"

    soup = BeautifulSoup(response.text, "lxml")
    seniority_elem = soup.find("span", class_="mr-10 font-weight-medium ng-star-inserted")
    return seniority_elem.text.strip() if seniority_elem else "Not specified"

def create_csv():
    """Creates a CSV file with headers in the Data folder."""
    file_path = os.path.join('Data', 'nofluffjobs.csv')

    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Job Title",
            "Location",
            "Minimum Salary",
            "Maximum Salary",
            "Technologies",
            "Company",
            "Seniority Level",
            "Job Link"
        ])

def write_csv(jobs: list):
    """Appends job data to the CSV file in the Data folder."""
    file_path = os.path.join('Data', 'nofluffjobs.csv')

    with open(file_path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for job in jobs:
            writer.writerow(job)

if __name__ == "__main__":
    parse_jobs(url="https://nofluffjobs.com/pl/?criteria=python", max_items=500)
