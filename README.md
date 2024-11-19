README

To REQUEST data from the microservice: simply write a url beginning with http(s) to the text file ‘summary-service.txt’. The microservice will automatically look for that text in the file, as long as they’re in the same directory and the code is being run in a Python console. After it finds the url, it will parse the news article page and write the first 2 lines of the body article to the same file and replace the url you wrote to request it.


Example call in Python:


    test = input("enter the url to a major news article to generate a summary")

    if test:

      file = open('summary-service.txt', mode='w')
    
      file.write(test)



To RECEIVE data from the microservice: extract the plain text from the file that is written after the initial program call. Please allow at least 10 seconds for it to write, as the program has built-in time delays to account for the time taken to access the web page.


Example call in Python:

    with open('summary-service.txt') as f:

      lines_after = f.readlines()[1:]
    
      for lines in lines_after:
    
          print(lines)
        

![image](https://github.com/user-attachments/assets/7eadbc9b-6f81-48a2-be10-27c5b25b9c4d)
