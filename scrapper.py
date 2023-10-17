from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import filedialog

def get_product_image_url(asin):

    driver = webdriver.Chrome()


    # Navigate to the Amazon product page using the ASIN
    url = f'https://www.amazon.com/dp/{asin}'
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'lxml')

    driver.quit()

    # Find the div tag with the "imgTagWrapperId" class
    image_div = soup.find('div', {'id': 'imgTagWrapperId'})

    if image_div:
        # Find the image URL within the div tag
        image_url = image_div.find('img')['src']

        return image_url
    else:
        return "error"
    

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        df = pd.read_excel(file_path)
        elements = df['ASIN'].to_list()
        urls = []
        for element in elements:
            urls.append(get_product_image_url(element))
        df = df.assign(urls=urls)
        df.to_excel('asin+url.xlsx')
        root.destroy()

root = tk.Tk()
select_file_button = tk.Button(root, text="Select Excel File", command=select_file)
select_file_button.pack()
root.mainloop()
