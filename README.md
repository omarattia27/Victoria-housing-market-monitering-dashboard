# Victoria-housing-market-monitering-dashboard
A dashboard that shows the general information about the rental market in Victoria BC

Kijiji scraber for all renatl ads:
scraber.py (parts of code example from https://medium.com/@kaineblack/web-scraping-kijiji-ads-with-python-ef81a49e0e9e was reused)

Facebook market scraber:
scraber2.py

NLP model to classify the Kijiji ad post to #bedrooms category:
*(Context)* Kijiji posts have no structure for tracking details (e.g. the number of bedrooms)

We will use posts from Facebook MarketPlace(which is structured and already categorized) for training machine learning model to classify the kijiji posts on basis of number of rooms.
