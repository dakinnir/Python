'''

Calculating a team scores from a specific season using the urllib module
and regular expression for scraping the data

Webscraping --
'''

#                   Approach

#1. Import necessary modules, ssl, re, urllib.request
#2. Bypass the mac issues with urllib using ssl
#3. Connect to the web by opening the webpage with urlopen
#4. Read the website and store it in a variable
#5. Use re.findall to search for pattern in webpage
#6. Create an empty dictionary to increment count of W and L
#6. Iterate over the content obtained from loading the web
#7. Increment the value of the key
#8. Output message wins and losses




#imporing modules necessary
import ssl, re, urllib.request
#certificate error work around for macs
context = ssl._create_unverified_context()

#create a pageloader function
def pageload(url):
    with urllib.request.urlopen(url, context=context) as l:
        webpage = l.read().decode(errors='replace')
        #pattern searching for
        results = re.findall("(?<=div class='schedule_game_results'><div>).+?(?=</div>)", webpage)
    return results
url = 'http://cgi.soic.indiana.edu/~dpierz/mbball.html'
content = pageload(url)

print('2017-2018 Season Stats')
for item in content:
    if len(item) < 10:
        print('\t',item)
    else:
        pass

results_dict = {"W": 0, "L": 0}
#iterate over the content obtained from loading the web
for result in content:
    #check if the result is a W or L
    if "W" in result:
        results_dict['W'] += 1
    elif "L" in result:
        #populating the dictionary by incrementing
        results_dict['L'] += 1
#output message wins and losses
print('\nResults of the Hoosiers 2017-2018 Men\'s Basketball Schedule:')
print('Wins:', results_dict["W"])
print('Losses:', results_dict["L"])
print('\n')

# for item in content:
#     print(item)

# CalculatING the total difference in points scored in all the games
#(a game that finished 68-71 would have a difference of 3 points, 85-52 a difference of 33 points etc)
difference_inPoints = 0
for scores in content:
    #set the values
    home_scores = scores[2:4]
    away_scores = scores[5:7]
    if home_scores == 'di' or away_scores == 'di':
        pass
    else:
        #calculate the difference
        difference_inPoints += abs(int(home_scores) - int(away_scores))
print('Total Difference:', difference_inPoints)
