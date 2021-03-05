# Data Mining from the E-commerce site

Computer Systems -> Input Devices -> VR Headsets
https://www.newegg.com/VR-Headsets/SubCategory/ID-3629


'''Get the contents of the page we’re looking at by requesting the URL'''
requests.get()

''' Get the response'''
response.status_code

''' Variable 'page' is created to store the request.get action
response.content

''' Parse html
BeautifulSoup(page, 'html.parser')

''' time.sleep(0.5)
 function from Python’s time module will control the loop’s rate
 by pausing the execution of the loop for a specified amount of seconds.

''' sleep(randint())
 function from Python’s random module will vary the amount
 of waiting time between requests — within the specified interval

''' Handling exceptions
>>> try:
...     this_fails()
... except ZeroDivisionError as err: #type of error
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero

''' select finds multiple instances and returns a list
''' the lens og the list = 1
''' it means in every list only one element and its index = [0]
container.select('.item-title')[0]


