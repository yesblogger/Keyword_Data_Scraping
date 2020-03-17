import csv
from extract import dataFetcher

if __name__ == '__main__':
    # open the keyword.csv file and read the content
    with open('keyword.csv', mode='r', encoding='utf-8') as r_file:
        # creating a csv reader object
        reader = csv.reader(r_file)
        # creating a new file to write the output
        with open('rename.csv', mode='w', newline='', encoding='utf-8') as w_file:
            # creating the header
            header = ['Keyword', 'Volume', 'Competion', 'CPC']
            # creating a writer object for the new file
            writer = csv.DictWriter(w_file, fieldnames=header)
            # writing the first row of the file
            writer.writeheader()
            # creating driver instance
            driver = dataFetcher()
            # now iterating over the rows in keyword.csv file
            for row in reader:
                # passing the keyword to the fetch function
                driver.fetchData(row[0], writer)
            driver.endSession()
