print ("Genius is someone who get a lemon from the Fate and start \
a lemonade stand with it.")
import os
import urllib.request
from bs4 import BeautifulSoup 

base_url = 'https://www.carusostjohn.com'  #http://bez-kock.de/projekte/
filepath = 'G:/ProgrammPractices/py/PythonApplication1/images/'

#Create soup
r = urllib.request.urlopen(base_url).read(); #create something like a filestream
soup = BeautifulSoup(r, "html5lib")
#print(soup.prettify()[0:2000]) # check if the soup is ready
#all_a = soup.body.find_all('a') #find out all Tags with the tagname 'a' in body branch
#    a = soup.body.a # find the first Tag named 'a' in body branch

#<a href="/projects/newport-street-gallery" title="Newport Street Gallery"><img src="/static/img/trans.gif" width="250" height="197" alt="Newport Street Gallery"></a>
#find out the tags contains the word 'title'
def has_title(tag):
    return tag.has_attr('title') 

some_tags = soup.find_all(has_title)
projects_links ={}  #{project_name: project_link}
for tag in some_tags:
    projects_links[tag['title']] = (base_url + tag['href'])

#download images to the local file folder
def download_images(project_name, project_link):
    page = urllib.request.urlopen(project_link).read();
    soup = BeautifulSoup(page, "html5lib")
    #<img src="/media/images/Untitled_11.jpg" alt="Newport Street Gallery - /media/images/Untitled_11.jpg" width="840" height="665">
    images = soup.find_all('img')
    imagelinks = []
    #download each image
    for image in images:
        imagelink = base_url + image['src']
        imagelinks.append(imagelink)
        directory = filepath #+ project_name 
        #check if the folder or file is already exist
        if not os.path.exists(directory):
            os.makedirs(directory)
        if not os.path.exists(directory + image['src'][13:]):
            urllib.request.urlretrieve(imagelink, directory +'/' + project_name + '_'+ image['src'][14:])
    print (project_name + " downloaded \n") 
    return;

project_names = projects_links.keys()
for project_name in project_names:
    download_images(project_name, projects_links[project_name])
