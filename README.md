# Election Analysis - Python Project for Module 3

## Project Overvew
A Board of Elections employee in Colorado asked me to complete an audit of election results for three counties. I was tasked with totaling the votes, figuring out the votes per candidate, listing the overall winner, and determining votes cast in each county. 

In order to do so, I followed these general steps: 

  1. Calculate total # of votes cast in the election
  2. Create a complete list of candidates in the election 
  3. Calculate the total # of votes for each candidate
  4. Calculate the % of votes each candidate received
  5. Determine the winner of the election based on the vote totals
  6. Calculate vote information by county

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election Results Summary
The analysis of the local election demonstrates: 

  - There were 369,711 votes cast in this election. 
    I arrived at this number by totalling the number of rows in the data source (election_results.csv). In order to total the rows of votes correctly, I started the count at the second row in the data source by skipping the row containing the data headers and then totalling the remaining rows:
    ```python
    with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)
    for row in reader:
        total_votes = total_votes + 1
    
  
  - There were three counties involved in the election, and here is the vote breakdown by county:
      - Jefferson County: 10.5% (38855 votes)
      - Denver County: 82.8% (306055 votes) 
      - Arapahoe County: 6.7% (24801 votes)
        Tabulating the total votes for each county required an `if`  statement under the controlling `for` statement that ran through each row in the data source after defining `county_name` as the second element in each row of the data source: 
     ```python
      county_name = row[1]
      ...
      if county_name not in county_list:        
         county_list.append(county_name)
         county_votes[county_name] = 0
      county_votes[county_name] += 1
    ```
  - Denver County had the largest number of votes. 
  
  - The candidates were: 
      - Charles Casper Stockham 
      - Diana DeGette
      - Raymon Anthony Doane
       Calculating the total number of votes for each candidate required a similar `if` statement after defining `candidate_name` as the third element in each row of the data source: 
      ```python
      candidate_name = row[2]
      ...
      if candidate_name not in candidate_options:        
          candidate_options.append(candidate_name)
          candidate_votes[candidate_name] = 0
      candidate_votes[candidate_name] += 1
      ``` 
  - The candidate results were: 
      - Charles Casper Stockham received 23.0% of the vote with 85,213 total votes.
      - Diana DeGette received 73.8% of the vote with 272,892 total votes. 
      - Raymon Anthony Doane received 3.1% of the vote with 11,606 total votes. 
       
  - The winner of the election was:
      - Diana DeGette, who received 73.85 of the vote with 272,892 total votes. 

## Challenge Summary
