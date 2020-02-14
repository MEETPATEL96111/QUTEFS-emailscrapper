

#initial input

YOUR_API_KEY = 'your google api key' # your google place api, (with billing api enabled)
where = 'QUT, Queensland' # Where would you be?
search = 'festival'  "what you would put in a google map search bar"
mongoadd = "mongodb://localhost:27017/"    # your mongo address
#init email scraping 
#! python3
import re, urllib.request, time


# regex to match email
emailRegex = re.compile(r'''
#example :
#something-.+_@somedomain.com
(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])
''', re.VERBOSE)
        
#Extacting Emails
def extractEmailsFromUrlText(urlText):
    extractedEmail =  emailRegex.findall(urlText.replace('%20',''))
    return extractedEmail
#HtmlPage Read Func
def htmlPageRead(url):
    try:
        headers = { 'User-Agent' : 'Mozilla/68.0' }
        request = urllib.request.Request(url, None, headers)
        response = urllib.request.urlopen(request,timeout=15)
        urlHtmlPageRead = response.read()
        urlText = urlHtmlPageRead.decode()
        email = extractEmailsFromUrlText(urlText)
        return email
    except:
        pass
    
#EmailsLeechFunction
def emailsLeechFunc(url):
    try:
        email = htmlPageRead(url)
        return email    
    except urllib.error.HTTPError as err:
        if err.code == 404:
            try:
                url = 'http://webcache.googleusercontent.com/search?q=cache:'+url
                email = htmlPageRead(url)
                return email
            except:
                pass
        else:
            pass    
      
#init mongo'
import pymongo 
myclient = pymongo.MongoClient(mongoadd)
mydb = myclient["qutefs"]
mycol = mydb["scrape"]

#mongo sigma
def sigma(_id,name,local_phone_number,website,url,email,email0):
    print(email,email0)
    bson={"_id" : _id, "name": name,"local_phone_number":local_phone_number,"website":website, "url":url,"email":email, "email0":email0 }
    mycol.insert_one(bson)


# init google places
from googleplaces import GooglePlaces, types, lang
google_places = GooglePlaces(YOUR_API_KEY)

# You may prefer to use the text_search API, instead.
query_result = google_places.nearby_search(
        location=where, keyword=search,
        radius=30000)
# If types param contains only 1 item the request to Google Places API
# will be send as type param to fullfil:
# http://googlegeodevelopers.blogspot.com.au/2016/02/changes-and-quality-improvements-in_16.html



# get data from api json list
if query_result.has_attributions:
    print (query_result.html_attributions)


for place in query_result.places:
    # Returned places from a query are place summaries.
    name = place.name
    # print (place.geo_location)
    _id = place.place_id

    # The following method has to make a further API call.
    place.get_details()
    # Referencing any of the attributes below, prior to making a call to
    # get_details() will raise a googleplaces.GooglePlacesAttributeError.
    # print (place.details) # A dict matching the JSON response from Google.
    local_phone_number = place.local_phone_number
    website = place.website


    # try to scrape email from the website
    # if wordpress, it might be in example.com/contact , sometimes both
    con = str(website)+"contact"
    url = place.url
    email0 = emailsLeechFunc(website)
    email = emailsLeechFunc(con)


    try:   # insert all data
        sigma(_id,name,local_phone_number,website,url,email,email0)
    except:
        print(name, "in list")
    print(name)

    # # Getting place photos

    # for photo in place.photos:
    #     # 'maxheight' or 'maxwidth' is required
    #     photo.get(maxheight=500, maxwidth=500)
    #     # MIME-type, e.g. 'image/jpeg'
    #     photo.mimetype
    #     # Image URL
    #     photo.url
    #     # Original filename (optional)
    #     photo.filename
    #     # Raw image data
    #     photo.data


# Are there any additional pages of results?
if query_result.has_next_page_token:
    query_result_next_page = google_places.nearby_search(
            pagetoken=query_result.next_page_token)


