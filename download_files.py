from selenium import webdriver
import time
import os

if __name__ == "__main__":
    download_dir = "C:\\Users\\kaae-\\Desktop\\code\\springer_download\\downloads"
    with open("cleaned_data.txt", "r") as data:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {
            # Change default directory for downloads
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,  # To auto download the file
            "download.directory_upgrade": True,
            # It will not show PDF directly in chrome
            "plugins.always_open_pdf_externally": True
        })
        options.add_argument("--headless")

        driver = webdriver.Chrome(chrome_options=options)
        for row in data:
            if row[:4] == "http":
                print(row)
                driver.get(row)
                elem = driver.find_elements_by_tag_name("a")
                for a in elem:
                    href = a.get_attribute("href")
                    if ".pdf" in href[-4:]:
                        print(href)
                        # a.click()
                        break
                    # time.sleep(2)
                driver.get(href)
                i = True
                while i:
                    i = False
                    time.sleep(0.5)
                    for obj in os.listdir(download_dir):
                        if obj[-11:] == ".crdownload":
                            i = True

                #mystr = BeautifulSoup(driver.page_source)
                # print(mystr.prettify())

        print("Finishing download")
        # driver.close()
