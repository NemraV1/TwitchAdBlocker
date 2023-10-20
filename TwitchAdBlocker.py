import time
from selenium import webdriver

# Replace with the path to your ChromeDriver executable
driver_path = 'chromedriver.exe path'

# URL of the Twitch channel you want to watch
twitch_url = 'The twitch channel url that you want'

# Initialize the Chrome driver with the correct argument
options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
driver = webdriver.Chrome(executable_path=driver_path, options=options)

# Function to block ads on Twitch
def block_ads():
    driver.get(twitch_url)
    time.sleep(5)  # Give the page some time to load

    try:
        ad = driver.find_element_by_css_selector('.video-ad--overlay')
        if ad:
            driver.execute_script('arguments[0].style.display = "none";', ad)
    except:
        pass

    # Continue watching the channel
    # You may need to adjust this selector based on Twitch's current structure
    watch_button = driver.find_element_by_css_selector('.player-controls__right-control-group button')
    if watch_button and 'Ad' in watch_button.text:
        watch_button.click()

# Main loop to continuously block ads
while True:
    block_ads()
    time.sleep(60)  # Check for ads every minute

# Close the browser when done
driver.quit()
