import time

from selenium import webdriver
from selenium.webdriver.common.by import By

CAPS_URL = "https://script.google.com/a/macros/motional.com/s/AKfycbxMMR5oJ7rIDGGJTKCrskeb9xkO72uMzsYuPfevlvYGxnhnZeaE878Rdh_qqwtQXXaq/exec"
WAIT_TIME = 5


def main():
    """Main function with automation by selenium web driver"""
    # 1. Open CAPS webpage
    driver = webdriver.Chrome()
    driver.implicitly_wait(WAIT_TIME)
    driver.get(CAPS_URL)

    fire_start_ans = [
        "Eng fire warning lt",
        "push",
        "Throttle(s)",
        "off",
        "Fire ext",
        "discharge",
        "Eng master sws",
        "off",
        "Jfs sw",
        "off",
    ]
    amad_fire_ans = []
    abort_ans = []
    bleed_air_ans = []
    positive_g_ans = []
    negative_g_ans = []
    loss_brakes_ans = []

    all_ans = (
        fire_start_ans
        + amad_fire_ans
        + abort_ans
        + bleed_air_ans
        + positive_g_ans
        + negative_g_ans
        + loss_brakes_ans
    )

    try:
        driver.switch_to.frame("sandboxFrame")
        driver.switch_to.frame("userHtmlFrame")

        for i, val in enumerate(all_ans):
            field = driver.find_element(By.ID, f"txtCap_{i}")
            field.click()
            field.send_keys(val)

        time.sleep(WAIT_TIME)
    except Exception as err:
        print(f"Exception encountered - {err}")
        driver.quit()
    finally:
        print("Closing page")
        driver.quit()


if __name__ == "__main__":
    main()
