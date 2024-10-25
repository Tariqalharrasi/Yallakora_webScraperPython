import requests
from bs4 import BeautifulSoup
import csv


date = input("Enter the date (MM/DD/YYYY): ")
page = requests.get(f"https://www.yallakora.com/match-center/?date={date}")


def main(page):

    src = page.content
    sope = BeautifulSoup(src, "lxml")
    
    match_details = []
    
    
    champions = sope.find_all("div",{'class': 'matchCard'})

    def info_match(champions):
        champions_title = champions.contents[1].find('h2').text.strip()
        all_matches = champions.contents[3].find_all("div",{'class': "item finish liItem"})
        num_of_matches = len(all_matches)

        for i in range(num_of_matches):
            team_a = all_matches[i].find("div",{'class': "teams teamA"}).text.strip()
            team_b = all_matches[i].find("div",{'class': "teams teamB"}).text.strip()

            match_score = all_matches[i].find("div",{'class': "MResult"}).find_all("span",{'class': "score"})
            score = f"{match_score[0].text.strip()} -- {match_score[1].text.strip()}"

            match_time = all_matches[i].find("div",{'class': "MResult"}).find("span",{'class': "time"}).text.strip()


            match_details.append({
                "نوع البطولة": champions_title, 
                "الفريق الاول": team_a,
                "الفريق الثاني": team_b,
                "وقت المبارة":match_time,
                "النتيجة":score,
            })

    for i in range(len(champions)):
        info_match(champions[i])
    
    keys = match_details[0].keys()

    with open('results/match-details.csv','w') as output_file:
        dict_writer = csv.DictWriter(output_file,keys)
        dict_writer.writeheader()
        dict_writer.writerows(match_details)
        print("file created...")
main(page)
