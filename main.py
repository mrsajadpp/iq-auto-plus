import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import subprocess


def convert_date(date):
    try:
        if "-" in date:
            date_parts = date.split("-")
            if len(date_parts) == 3:
                day = date_parts[2]
                month = date_parts[1]
                year = date_parts[0]
                return f"{day}{month}{year}"

        elif len(date) == 8 and date.isdigit():
            year = date[:4]
            month = date[4:6]
            day = date[6:8]
            return f"{day}{month}{year}"

        else:
            raise ValueError(
                f"Invalid date format: {date}. Expected either yyyymmdd or yyyy-mm-dd."
            )

    except Exception as e:
        raise ValueError(f"Error while converting date: {e}")


def load_data(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        exit(1)


def scroll_to_element(driver, element):
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element
    )
    time.sleep(1)


def fill_form(data):
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.manoramaquiz.in/")

        password = convert_date(data["dob"])
        password_field = wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        scroll_to_element(driver, password_field)
        password_field.send_keys(password)

        email_login_field = wait.until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
        scroll_to_element(driver, email_login_field)
        email_login_field.send_keys(data["email"])

        submit_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-button"))
        )
        scroll_to_element(driver, submit_button)
        submit_button.click()
        print(f"Login for {data['email']} successful.")

        # time.sleep(3)

        start_quiz_button = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".button-container .banner-button")
            )
        )
        start_quiz_button.click()

        # time.sleep(4)

        inputs = driver.find_elements(By.CSS_SELECTOR, ".answer-cells .answer-cell")

        answers = ["S", "I", "K", "K", "I", "M"]

        for i, value in enumerate(answers):
            inputs[i].send_keys(value)

        time.sleep(1)

        next_quiz_button = driver.find_element(By.CSS_SELECTOR, ".next-btn")
        scroll_to_element(driver, next_quiz_button)
        next_quiz_button.click()

        time.sleep(1)

        inputs_two = driver.find_elements(By.CSS_SELECTOR, ".answer-cells .answer-cell")

        answers_two = ["T", "U", "S", "H", "A", "R", "G", "A", "N", "D", "H", "I"]

        for i, value in enumerate(answers_two):
            inputs_two[i].send_keys(value)

        time.sleep(1)

        next_quiz_button = driver.find_element(By.CSS_SELECTOR, ".next-btn")
        scroll_to_element(driver, next_quiz_button)
        next_quiz_button.click()

        time.sleep(1)

        inputs_three = driver.find_elements(
            By.CSS_SELECTOR, ".answer-cells .answer-cell"
        )

        answers_three = [
            "A",
            "E",
            "W",
            "A",
            "T",
            "A",
            "N",
            "M",
            "E",
            "R",
            "E",
            "W",
            "A",
            "T",
            "A",
            "N",
        ]

        for i, value in enumerate(answers_three):
            inputs_three[i].send_keys(value)

        time.sleep(1)

        next_quiz_button = driver.find_element(By.CSS_SELECTOR, ".next-btn")
        scroll_to_element(driver, next_quiz_button)
        next_quiz_button.click()

        time.sleep(1)

        inputs_four = driver.find_elements(
            By.CSS_SELECTOR, ".answer-cells .answer-cell"
        )

        answers_four = ["M", "O", "R", "O", "C", "C", "O"]

        for i, value in enumerate(answers_four):
            inputs_four[i].send_keys(value)

        time.sleep(1)

        next_quiz_button = driver.find_element(By.CSS_SELECTOR, ".next-btn")
        scroll_to_element(driver, next_quiz_button)
        next_quiz_button.click()

        time.sleep(1)

        inputs_five = driver.find_elements(
            By.CSS_SELECTOR, ".answer-cells .answer-cell"
        )

        answers_five = ["P", "E", "R", "I", "Y", "A", "R"]

        for i, value in enumerate(answers_five):
            inputs_five[i].send_keys(value)

        time.sleep(1)

        next_quiz_button = driver.find_element(By.CSS_SELECTOR, ".submit-btn")
        scroll_to_element(driver, next_quiz_button)
        next_quiz_button.click()

    except Exception as e:
        print(f"An error occurred for {data['email']}: {e}")

    finally:
        time.sleep(2)
        driver.quit()
        print(f"Completed processing for {data['email']}")


if __name__ == "__main__":
    subprocess.call(["python3", "signup.py"])
    json_file_path = "user_data.json"
    form_data = load_data(json_file_path)

    for user in form_data:
        fill_form(user)
