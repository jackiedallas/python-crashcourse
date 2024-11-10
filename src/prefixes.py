# use .removeprefix() method to cut slice leading characters from a string
ssc_url = 'https://southernsummitconsulting.com'
prefix = 'https://'
simple_url = ssc_url.removeprefix(prefix)
print(simple_url)