import pyshorteners  # Import the pyshorteners library for URL shortening

def shorten_url(long_url):
  """
  This function shortens a given URL using the TinyURL API.

  Args:
      long_url (str): The URL to be shortened.

  Returns:
      str: The shortened URL.

  Raises:
      Exception: If there's an error shortening the URL.
  """

  try:
    # Create a Shortener object using the TinyURL service
    shortener = pyshorteners.Shortener()
    # Shorten the long URL using the TinyURL service
    short_url = shortener.tinyurl.short(long_url)
    # Return the shortened URL
    return short_url
  except Exception as e:
    # If an error occurs during shortening, raise a descriptive exception
    raise Exception(f"Error shortening URL: {e}")

# Example usage:
url_to_shorten = input("Enter the URL to shorten: ")
shortened_url = shorten_url(url_to_shorten)
print("Shortened URL:", shortened_url)
