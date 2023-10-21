import httpx

# def means "define a function"
# you can call this function whatever you want, but in python
# we use snake_case for function names, as opposed to camelCase
def what_is_my_ip():
    # make an http GET request over the internet to a free API
    # service that returns the caller's IP address
    
    # httpx will give us a response object back when we make a request
    response = httpx.get('https://api.ipify.org')
    
    # <Response [200]> means the request was successful
    print(f"Response from the API: {response}")
    
    """
    this little f"text {variable}" thing above is called an "f-string"
    it's a way to make a string with variable values stitched into it
    
    This is a multi-line comment, it's useful for writing
    documentation for your code. You can also use it to
    comment out code that you don't want to run:
    
    print("This won't run, because it's commented out")
    """
    
    # print("you won't see this either, because it's commented out")
    
    
    # i just want to see my IP, so i'll get the text from the response object
    ip = response.text
    
    # Print the IP address to the standard output
    print(f"My IP address is: {ip}")
    
# this is where the program starts executing, its called an "entry point"
# you should always have an entry point in any program you're going to execute
if __name__ == '__main__':
    # call the function we defined above
    what_is_my_ip()
    
    # run this program with `python hello_python.py`
    # you should see your IP address printed out