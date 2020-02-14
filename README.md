# QUTEFS-emailscrapper
Michael wanna spam entertaiment business and ask for sponsership, so he thew me under the bus to scrape, This uses google places api to get entertaiments, then get their website and scrape their emails with regex, store them in mongo and then I manualy export them into csv and json, cleaned it up a bit and then sent him an array, have fun michael talking to 96 business in 3km raduis around QUT


Step 1:

python3 setup.py

Step 2:

go to run.py:
YOUR_API_KEY = 'your google api key' # your google place api, (with billing api enabled)
where = 'QUT, Queensland' # Where would you be?
search = 'festival'  "what you would put in a google map search bar"
mongoadd = "mongodb://localhost:27017/"    # your mongo address
mydb = myclient["qutefs"] # mongo cluster name
mycol = mydb["scrape"] #mongo database name

Step 3:

You realize you need to intall mongod, mongodb compass and create a cluster and database, I called my cluster qutefs and my database scrape.

you realize you need to setup your google places api and also enable billing api go you go and try to find out what to do, goodluck, btw.

Step 4:

python3 run.py

Step 5:

Export all the json or csv or a just a blob of text with all the email in them, go to email.py and replace them with tex, remember to keep the ''' <blob of data> ''' format, this will clean up all the non and repetitive emails and output an array, and leave the rest to someone named Michael.  
