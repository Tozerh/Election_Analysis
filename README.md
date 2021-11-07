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

## Election Results Summary & Analysis
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
        Tabulating the total votes for each county required an `if`  statement under the controlling `for` statement that ran through each row in the data source after defining `county_name` as the second element in each row of the data source. This `if` statement both added the county names to the list `county_list` while also creating three `key:value` pairs in the dicionary `county_votes{}` consisting of the name of each county and the number of times each of these counties appears in the data source: 
        
     ```python
      county_votes = {}
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
      
       Calculating the total number of votes for each candidate required a similar `if` statement as the votes per county, after defining `candidate_name` as the third element in each row of the data source. As above for the county data, the `if` statement below both creates a list of candidate names and also establishes three `key:value` pairs in the dictionary `candidate_options` for the name of each candidate and the total number of votes they recieved:
       
      ```python
      candidate_name = row[2]
      candidate_votes = {}
      ...
      if candidate_name not in candidate_options:        
          candidate_options.append(candidate_name)
          candidate_votes[candidate_name] = 0
      candidate_votes[candidate_name] += 1``` 
      
     
  - The candidate results were: 
      - Charles Casper Stockham received 23.0% of the vote with 85,213 total votes.
      - Diana DeGette received 73.8% of the vote with 272,892 total votes. 
      - Raymon Anthony Doane received 3.1% of the vote with 11,606 total votes. 
      
        Once vote totals were computed, the percentage of each vote cast for each candidate was found by dividing each candidates's vote count by the total number of votes cast. At this point in my code, each candidate's vote total had been written to the `key:value` pairs in the `candidate_options{}` dictionary, and the equation for percentage of the total vote looks like: 
       
       ```python
       c_votes = county_votes.get(county_name)
       
       c_vote_percentage = (float(c_votes)/(float(total_votes)))*100
       
       county_results = (
            f'{county_name}: {c_vote_percentage:.1f}% ({c_votes} votes).\n')
       
  (In the above snippet of code, `county_results` is being defined as a string literal so that it could be easily printed in the terminal and outputted to our results text file.) 
  
  - The winner of the election was:
      - Diana DeGette, who received 73.85 of the vote with 272,892 total votes. 
        
        

## Suggestions to Modify Code for Other Elections
There are a couple of suggestions that I might make for adapting this code for other elections:
  - Creating a way to check for duplicate votes being case by the same voter identification code in multiple counties.
  - Creating a method for sorting results and tracking margin of victory. 

### Checking for Duplicates
  Were this code to be adopted in other elections, I would suggest writing a section of code that returned any duplicates for voter identification numbers, which might indicate that a vote was counted twice accidentally. Employing this code would help to ensure that the election results could be confirmed relatively and reported as final relatively quickly. In order to code this, we might build an if statement at the end of our code that is similar to the `if` statements embedded in the `for` statement referenced above for counting candidate and county vote totals: 
  
  `python    for row in Read:
        voter_id = row[0]
        if voter_id not in voter_id_list: 
            voter_id_list.append(voter_id)
            voter_id_dict[voter_id] = 0
        voter_id_dict[voter_id] +=1
    if voter_id_dict[voter_id] > 1:
        dup_output[voter_id]
    print(dup_output)`
    
    
  The code above, when applied to the election results for this project, returns to the terminal the following output:  
###Sorting Results 
  
  Given that there are only three candidates in this election (and that this election was not particularly close) it's relaatively easy for an election worker to understand the results. In an election with many candidates (or maybe even a different election system like a "ranked choice" system) or one that is much closer in terms of the margin of victory, it might be more difficult for an election worker to easily determine who won. For example, the results printed in the code I provided for this project are only accurate to one decimal place. In a very close race, the margin of victory may be such that one decimal place results in an apparent tie between one or more candidates. In such a case, we would want to change our code to allow for more decimal places, like so: 
  ```     votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.4f}% ({votes:,})\n")
  ```
  By changing `:.1f}%` to `:.4f}%` we are able to generate results in percentages with more signifcant digits, allowing for a closer comparison of percentages in a very close race. 
  Similarly, there are often vote margin threshholds in elections that require the winning candidate to win by a certain number of votes. For example, in this election the winner might have been required to win by at least 1,000 votes without activating a manual recount. Capturing the difference in vote totals would be a useful metric to assist election officials in deciding how to proceed. In the current project, the vote totals are sufficiently disparate and the candidates sufficiently few that an election official would not necessarily need this additional code, but it is not difficult to imagine a hotly contested election in which this data could come i handy. 
  In order to code these changes, I would suggest adding the following code XXXXGIVE LOCATION>>> CAN YOU DO IT?>>>           
      
