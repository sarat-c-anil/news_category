import feedparser
url="https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms"
feed=feedparser.parse(url)
if feed.status == 200:
    # Iterate through the entries in the feed
    for entry in feed.entries:
        # Get the title and link of each entry
        title = entry.title
        link = entry.link
        
        # Print the title and link of each entry
        print(f"Title: {title}")
        print(f"Link: {link}")
        print("-" * 50)

else:
    # Print an error message if the feed parsing was not successful
    print("Error parsing the RSS feed")