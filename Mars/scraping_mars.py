def Scrape():
    from splinter import Browser
    from bs4 import BeautifulSoup
    from urllib.parse import urlsplit
    import pandas as pd
    import re
    import time
    import json

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    browser.visit(url)

    results = browser.html
    soup = BeautifulSoup(results, 'html.parser')

    results_raw = soup.find("div", class_="list_text")
    results_raw

    results_1 = soup.find("div", class_="content_title").text

    print(results_1)

    results_2 = soup.find("div", class_="article_teaser_body").text

    print(results_2)

    image_mining = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_mining)

    #Finding our base URL
    image_ore_1 = "{0.scheme}://{0.netloc}".format(urlsplit(image_mining))
    print(image_ore_1)

    click_path = "//*[@id=\"page\"]/section[3]/div/ul/li[1]/a/div/div[2]/img"
    results_3 = browser.find_by_xpath(click_path)
    img = results_3[0]
    img.click()
    time.sleep(5)

    featured_image = browser.html

    soup2 = BeautifulSoup(featured_image, "html.parser")
    image_ore_2 = soup2.find("img", class_="fancybox-image")

    string_image = str(image_ore_2)
    string_image

    #Some regex. Its a long story...
    string_image_2 = re.findall('{}(.*){}'.format('src="', '" style'), string_image)
    string_image_2[0]

    featured_img_url = image_ore_1 + string_image_2[0]
    print(featured_img_url)

    #Martian Weather Twitter
    martian_weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(martian_weather_url)

    martian_weather = browser.html
    soup3 = BeautifulSoup(martian_weather, "html.parser")

    temperature = soup3.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})
    mars_weather = soup3.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    print(mars_weather)

    mars_facts = "https://space-facts.com/mars/"

    fact_sheet = pd.read_html(mars_facts)
    fact_sheet[0]

    fact_sheet_df = fact_sheet[0]
    fact_sheet_df.columns = ["Measurement Type", "Measurement"]
    fact_sheet_df.set_index(["Measurement Type"])

    mars_table = fact_sheet_df.to_html()
    mars_table = mars_table.replace("\n", "")
    mars_table

    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemi_url)

    base_hemi = "{0.scheme}://{0.netloc}/".format(urlsplit(hemi_url))
    print(base_hemi)

    hemi_urls = []
    results_4 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[1]/a/img").click()
    time.sleep(2)
    open_cerberus = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    image_cerberus = browser.html
    soup = BeautifulSoup(image_cerberus, "html.parser")
    url_cerberus = soup.find("img", class_="wide-image")["src"]

    image_url_cerberus = base_hemi + url_cerberus
    print(image_url_cerberus)

    title_cerberus = soup.find("h2",class_="title").text
    print(title_cerberus)

    #Back and save
    press_back = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    cerberus = {"image title":title_cerberus, "image url": image_url_cerberus}
    hemi_urls.append(cerberus)

    results_5 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[2]/a/img").click()
    time.sleep(2)
    open_schiaparelli = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    image_schiaparelli = browser.html
    soup = BeautifulSoup(image_schiaparelli, "html.parser")
    url_schiaparelli = soup.find("img", class_="wide-image")["src"]

    image_url_schiaparelli = base_hemi + url_schiaparelli
    print(image_url_schiaparelli)

    title_schiaparelli = soup.find("h2",class_="title").text
    print(title_schiaparelli)

    #Back and save
    press_back_2 = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    schiaparelli = {"image title":title_schiaparelli, "image url": image_url_schiaparelli}
    hemi_urls.append(schiaparelli)

    #In case you are wondering why am repeating this from earlier: the clicking macro is a tad touchy.
    #Its working more reliably split up into two parts.

    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemi_url)

    base_hemi = "{0.scheme}://{0.netloc}/".format(urlsplit(hemi_url))
    print(base_hemi)

    results_6 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[3]/a/img").click()
    time.sleep(2)
    open_syrtis_major = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    image_syrtis_major = browser.html
    soup = BeautifulSoup(image_syrtis_major, "html.parser")
    url_syrtis_major = soup.find("img", class_="wide-image")["src"]

    image_url_syrtis_major = base_hemi + url_syrtis_major
    print(image_url_syrtis_major)

    title_syrtis_major = soup.find("h2",class_="title").text
    print(title_syrtis_major)

    #Back and save
    press_back_3 = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    syrtis_major = {"image title": title_syrtis_major, "image url": image_url_syrtis_major}
    hemi_urls.append(syrtis_major)

    results_7 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[4]/a/img").click()
    time.sleep(2)
    open_valles_marineris = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    image_valles_marineris = browser.html
    soup = BeautifulSoup(image_valles_marineris, "html.parser")
    url_valles_marineris = soup.find("img", class_="wide-image")["src"]

    image_url_valles_marineris = base_hemi + url_valles_marineris
    print(image_url_valles_marineris)

    title_valles_marineris = soup.find("h2",class_="title").text
    print(title_valles_marineris)

    #Back and save
    press_back_4 = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    valles_marineris = {"image title": title_valles_marineris, "image url": image_url_valles_marineris}
    hemi_urls.append(valles_marineris)

    print(hemi_urls)
    
    dict_master = {"Data": [results_1, results_2, featured_img_url, mars_weather, mars_table, hemi_urls]}

    return(dict_master)