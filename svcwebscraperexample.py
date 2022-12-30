# This Program scrapes all degree data on the Saint Vincent College
# website, as in the name and type(s) of said degree. After scraping
# data from the Saint Vincent College website, all scraped data is
# posted to a database: firebase.
#
# By Thomas McLaughlin

import requests
from firebase import firebase
from bs4 import BeautifulSoup

def main():
    URL = "https://www.stvincent.edu/academics/degree-explorer/index.html"
    page = requests.get(URL)
    complete_code = BeautifulSoup(page.content, "html.parser")

    section_results = complete_code.find(class_="explorer-results")

    degree_data_list = section_results.find_all("li", class_="explorer-results-row")

    dataBase = firebase.FirebaseApplication("https://NOTMYDATABASE-default-rtdb.firebaseio.com/", None)

    #skipping the first degree data due to being 'None'
    for degree_data_list in degree_data_list[1:]:
        name_degree = degree_data_list.find("span")
        degree_type = degree_data_list.find("a")
        data_fields = {'Name of Degree ': name_degree.text, 'Type of Degree(s) ': degree_type.text}
        dataBase.post('/SVC-Degree-Data/', data_fields) 
  
if __name__=="__main__":
    main()
    
