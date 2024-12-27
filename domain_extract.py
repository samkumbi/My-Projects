# App name   => Domain Extractor 
# Programmer => Sam Kumbi

# App description
# ---------------
# This program extracts and prints the domain name from a URL.

# Get the URL from the user
url = input("Type in the URL: ")

# Split the URL
split_url = url.split('/')

# Display the URL
print("\nHere's the domain name")
print(split_url[2])
print("")