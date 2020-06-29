import requests
from bs4 import BeautifulSoup
import pandas
import csv
import sqlite3
def database(dbname):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("CREATE TABLE imdbmovies (Release_Year TEXT , Title TEXT )" )
    conn.close()

def upload(info,dbname):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("INSERT INTO movies VALUES(?,?)",info)
    conn.commit()
    conn.close()
dbname = 'movies.db'


print("\nThis program prints TOP 250 movies from IMDB website\n")
tri_url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
requ= requests.get(tri_url)
content=requ.content

soup= BeautifulSoup(content,'html.parser')
movies=soup.find_all("td",{"class":"titleColumn"})

scr_info_list=[]
for mov in movies:
    movie_dict={}
    movie_dict["Release_Year"]= mov.find("span",{"class":"secondaryInfo"}).text
    movie_dict["Title"]= mov.find("a",{"gref":""}).text
    scr_info_list.append(movie_dict)
    info = tuple(movie_dict.values())
    upload (info,dbname)

conn  = sqlite3.connect ('movies.db')
cur = conn.cursor ()
x = cur.execute ("SELECT * FROM movies")

for i in x :
    print (i)
    
conn.commit ()
conn.close ()

output:
This program prints TOP 250 movies from IMDB website

('(1957)', 'Kumonosu-jô')
('(1957)', 'Kumonosu-jô')
('(1957)', 'Kumonosu-jô')
('(1994)', 'The Shawshank Redemption')
('(1972)', 'The Godfather')
('(1974)', 'The Godfather: Part II')
('(2008)', 'The Dark Knight')
('(1957)', '12 Angry Men')
('(1993)', "Schindler's List")
('(2003)', 'The Lord of the Rings: The Return of the King')
('(1994)', 'Pulp Fiction')
('(1966)', 'Il buono, il brutto, il cattivo')
('(2001)', 'The Lord of the Rings: The Fellowship of the Ring')
('(1999)', 'Fight Club')
('(1994)', 'Forrest Gump')
('(2010)', 'Inception')
('(1980)', 'Star Wars: Episode V - The Empire Strikes Back')
('(2002)', 'The Lord of the Rings: The Two Towers')
('(1999)', 'The Matrix')
('(1990)', 'Goodfellas')
('(1975)', "One Flew Over the Cuckoo's Nest")
('(1954)', 'Shichinin no samurai')
('(1995)', 'Se7en')
('(1997)', 'La vita è bella')
('(2002)', 'Cidade de Deus')
('(1991)', 'The Silence of the Lambs')
('(1946)', "It's a Wonderful Life')
