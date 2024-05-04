import time

from selenium import webdriver
from selenium.webdriver.common.by import By

CAPS_URL = "https://script.google.com/a/macros/motional.com/s/AKfycbxMMR5oJ7rIDGGJTKCrskeb9xkO72uMzsYuPfevlvYGxnhnZeaE878Rdh_qqwtQXXaq/exec"
SHORT_WAIT_TIME = 3
LONG_WAIT_TIME = 10


def main():
    """Main function with automation by selenium web driver"""
    # 1. Open CAPS webpage
    driver = webdriver.Chrome()
    driver.implicitly_wait(LONG_WAIT_TIME)
    driver.get(CAPS_URL)

    fire_start_ans = [
        "eng fire warning lt",
        "push",
        "throttle(s)",
        "off",
        "fire ext",
        "discharge",
        "eng master sws",
        "off",
        "jfs sw",
        "off",
    ]
    amad_fire_ans = [
        "amad lt",
        "push",
        "fire ext",
        "discharge",
        "throttles",
        "off",
        "eng master sws",
        "off",
        "jfs sw",
        "off",
    ]
    abort_ans = ["throttles", "idle", "brakes", "apply", "hook", "as req"]
    bleed_air_ans = [
        "air source knob",
        "opp source",
        "throttle",
        "idle",
        "fire warning sys",
        "test",
        "air source knob",
        "off",
        "fire warning sys",
        "test",
    ]
    positive_g_ans = [
        "controls",
        "smoothly neutralize and release",
        "rudder",
        "smoothly opp roll/yaw",
        "speed brake",
        "retract",
        "throttles",
        "out of ab",
    ]
    negative_g_ans = [
        "controls",
        "smoothly neutralize laterally and apply half aft stick",
        "rudder",
        "smoothly opp yaw",
        "speed brake",
        "retract",
        "throttles",
        "out of ab and matched",
    ]
    loss_brakes_ans = [
        "hook",
        "down",
        "anti skid sw",
        "off or pulser",
        "emer brake/steer handle",
        "pull",
        "throttles",
        "off",
    ]

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

        driver.find_element(By.ID, "btn_chkAnswer").click()
        time.sleep(SHORT_WAIT_TIME)

        call_sign = driver.find_element(By.ID, "txtCallsign")
        call_sign.click()
        call_sign.send_keys("arc")

        driver.find_element(By.ID, "btn_submit").click()
        time.sleep(LONG_WAIT_TIME)
        print("Successfully submitted e-CAPs")
    except Exception as err:
        print(f"Exception encountered - {err}")
        driver.quit()
    finally:
        print("Closing page")
        driver.quit()


if __name__ == "__main__":
    main()
