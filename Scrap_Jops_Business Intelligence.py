# Scrap_Jobs_business_intelligence

import requests
from bs4 import BeautifulSoup
import pandas as pd


def Scrap_business_intelligence():
    Title_lst, links_list, occupations_lst, Companies_lst, Specs_lst, Location_lst = [
    ], [], [], [], [], []
    URL = "https://wuzzuf.net/search/jobs/?a=navbg%7Cspbg&q=business%20intelligence"
    res = requests.get(URL)
    soup = BeautifulSoup(res.content, "html")
    PagesCount = soup.find_all("li", {"class": "css-8neukt"})
    Pages = [P.text for P in PagesCount][0]
    PagesStr = [int(s) for s in Pages.split() if s.isdigit()]
    MaxPage = PagesStr[2]
    for i in range(MaxPage):
        RES = requests.get(
            "https://wuzzuf.net/search/jobs/?a=navbg%7Cspbg&q=business%20intelligence&start="+str(i))
        SOP = BeautifulSoup(RES.content, "html")
        Title = SOP.find_all("h2", {"class": "css-m604qf"})
        links = SOP.find_all("h2", {"class": "css-m604qf"})
        occupations = SOP.find_all("div", {"class": "css-1lh32fc"})
        Companies = SOP.find_all("a", {"class": "css-17s97q8"})
        Specs = SOP.find_all("div", {"class": "css-y4udm8"})
        Location = SOP.find_all("span", {"class": "css-5wys0k"})
        for i in range(len(Title)):
            Title_lst.append(Title[i].a.text)
            links_list.append("https://wuzzuf.net"+links[i].a["href"])
            occupations_lst.append(occupations[i].a.text)
            Companies_lst.append(Companies[i].text)
            Specs_lst.append(Specs[i].a.text)
            Location_lst.append(Location[i].text)
        Scraped_Data = {}
        Scraped_Data["titles"] = Title_lst
        Scraped_Data["Companies"] = Companies_lst
        Scraped_Data["occupations"] = occupations_lst
        Scraped_Data["Location"] = Location_lst
        Scraped_Data["Specs"] = Specs_lst
        Scraped_Data["Link"] = links_list
        Scraped_Data

    df = pd.DataFrame(Scraped_Data)
    df.to_csv("N_Scrap_business_intelligence2.csv", index=True)
    print("Jobs Scraped Sucsessfully (business_intelligence)")
    return df


if __name__ == "__main__":
    Scrap_business_intelligence()
