import time

test = input("enter the url to a major news article to generate a summary")

if test:

    file = open('summary-service.txt', mode='w')

    time.sleep(5)

    file.write(test)

    file.close()

    time.sleep(5)

    with open('summary-service.txt') as f:
        lines_after = f.readlines()[1:]
        for lines in lines_after:
            print(lines)




