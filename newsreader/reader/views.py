import feedparser
from django.shortcuts import render

def display_news(request, category):
    # Define RSS feed URLs for different categories
    rss_feeds = {
        'sports': 'https://timesofindia.indiatimes.com/rssfeeds/4719148.cms',
        'business': 'https://www.bbc.com/news/business/rss.xml',
        'world':'https://timesofindia.indiatimes.com/rssfeeds/296589292.cms',
        'education':'https://timesofindia.indiatimes.com/rssfeeds/913168846.cms',
        # Add more categories and corresponding RSS feed URLs
    }

    # Check if the requested category has a defined RSS feed URL
    if category in rss_feeds:
        rss_url = rss_feeds[category]
        feed = feedparser.parse(rss_url)
        entries = feed.entries  # List of entries (articles) in the feed
        context = {'entries': entries, 'category': category}
        return render(request, 'news.html', context)
    else:
        return render(request, 'error.html', {'message': 'Category not found'})