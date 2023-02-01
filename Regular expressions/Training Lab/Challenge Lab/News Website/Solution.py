#Challenge Lab: News Website
import re

# Define the pattern to search for
date_pattern = r"(\d{2}[/-]\d{2}[/-]\d{4})"
author_pattern = r"Author: (\w+)"
keywords_pattern = r"Keywords: ([\w, ]+)"

# Read the news article
article = "Date: 01/01/2022\nAuthor: John\nKeywords: news, website, analysis\n\nThis is a sample news article.\nIt was written by John on 01/01/2022."

# Search for the date, author and keywords using the re.search() function
date_match = re.search(date_pattern, article)
author_match = re.search(author_pattern, article)
keywords_match = re.search(keywords_pattern, article)

# Extract the date, author and keywords from the matched strings
date = date_match.group(1)
author = author_match.group(1)
keywords = keywords_match.group(1)

# Replace the text in the article with the extracted information
article = re.sub(date_pattern, "", article)
article = re.sub(author_pattern, "", article)
article = re.sub(keywords_pattern, "", article)

# Split the article into a list of words
words = re.split(r"\W+", article)

# Print out the article, the list of words, the date, author and keywords
print("Article:\n", article)
print("Words:\n", words)
print("Date:", date)
print("Author:", author)
print("Keywords:", keywords)
