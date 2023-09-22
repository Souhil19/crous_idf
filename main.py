import requests
from bs4 import BeautifulSoup
import time
import requests
from lxml import html
import time
from datetime import datetime

if __name__ == '__main__':


    delay=30
    import requests
    from lxml import html
    import time

    # URL of the web page
    url = "https://trouverunlogement.lescrous.fr/tools/31/search?bounds=1.4462445_49.241431_3.5592208_48.1201456"

    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using lxml and XPath
            root = html.fromstring(response.text)

            # Define the XPath to the h2 element
            xpath_to_h2 = "/html/body/div/main/div[2]/div[2]/div[2]/div[1]/div/div/h2"  # or "//*[@id='main']/div[2]/div[2]/div[2]/div[1]/div/div/h2"

            # Use XPath to find the h2 element
            h2_element = root.xpath(xpath_to_h2)

            if h2_element:
                print(h2_element[0].text + ' '+current_time)
                # Check if the text content of the h2 element is different from '0'
                if h2_element[0].text != 'Aucun logement trouvÃ©':
                    print("Found a result different from '0' in the h2 element. Stopping the script.")
                    break
                else:
                    print("No result different from '0' found in the h2 element. Retrying in {} seconds.".format(delay))
            else:
                print("No h2 element with the specified XPath found on the page. Retrying in {} seconds.".format(delay))
        else:
            print(
                f"Failed to fetch the page. Status code: {response.status_code}. Retrying in {delay} seconds.".format(delay))

        # Wait for the specified delay before the next check
        time.sleep(delay)





