#Project Parameters:

# Elements required: 
#   Total number of votes cast
#   A complete list of candidates who received votes
#   Total number of votes each candidate received
#   Percentage of votes each candidate won
#   The winner of the election based on popular votes

# Opening with open and closing with close

    # election_data = open(file,'r')
    #need to perform analysis

    #Close the file
    #election_data.close()

# import csv
# import os
# import datetime
# # Assign a variable to a file and load the path using chaining.
# file_to_load = os.path.join('Resources','election_results.csv')
# # Open he results and read the file.
# with open(file_to_load) as election_data:
# # Print the file object.
#     print(election_data)
#     print(os.path.dirname(file_to_load))
#     print(os.path.lexists(file_to_load))
#     print(os.path.expanduser(file_to_load))
#     print(os.path.expandvars(file_to_load))
#     print(datetime.datetime.fromtimestamp(os.path.getctime(file_to_load)))

#Open and write to file without WITH statement
# import csv
# import os
# file_to_save = os.path.join('analysis','election_analysis.txt')
# open(file_to_save,'w')
# # open the file as a text file 
# outfile = open(file_to_save,'w')
# # Write some data into the file - possible bc of the 'w' in the open statement in ln 38
# outfile.write("Yes, we have no bananas.")
# # close the file
# outfile.close()


# #  $$$$$$ Open and write to file using WITH statement $$$$$$
import csv
import os

#Create filename variable to a direct or indirect path
file_to_save = os.path.join('Analysis','election_analysis.txt')

# Using with statement, open the file as a text file
with open(file_to_save,'w') as txt_file:
    # Write three counties to the file with escape sequence to intiate line breaks
    txt_file.write('Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson')


# Begin 
file_to_load = os.path.join('Resources','election_results.csv')

 # initialize accumulator for votes - placed before open file so that it always starts at 0
total_votes = 0 

# new list for candidate names
candidate_list = []
candidate_votes = {}
winning_candidate = ''
winning_count = 0
winning_percentage = 0

# Open the results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # read the header row.
    headers = next(file_reader)

    # print each row in csv
    for row in file_reader:
        total_votes += 1 
        candidate_name = row[2]
        if candidate_name not in candidate_list:
            # add candidate name to the list
            candidate_list.append(candidate_name)

            # being tracking candidate's vote count
            candidate_votes[candidate_name] = 0 
        candidate_votes[candidate_name] += 1
    with open(file_to_save,'w') as txt_file:
        election_results = (
            f'Election Results\n'
            f'--===--===--===--===---===\n'
            f'Total Votes: 369,711\n'
            f'--===--===--===--===---===\n'
        )
        print(election_results)
        txt_file.write(election_results)
    # loop through candidate list 
        for candidate_name  in candidate_votes:
            # retrieve vote count for a candidate (calls the value associated with the name)
            votes = candidate_votes[candidate_name]
            # calc % of vote for each candidate
            vote_percentage = float(votes) / float(total_votes) * 100
            # print statement
            # print (f"{candidate_name} received {vote_percentage:.1f}% of the vote.")

            # to do: print out each candidate's name, vote count, and percentage of votes to the terminal.
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            txt_file.write(candidate_results)
            print(candidate_results, end='')
            if (votes>winning_count) and (vote_percentage > winning_percentage): 
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name
            
        winning_candidate_summary = (
            f'----------------------------------------------\n'
            f'Winner: {winning_candidate}\n'
            f'Winning Vote Count: {winning_count:,}\n'
            f'Winning Percentage: {winning_percentage:.1f}%\n'
            f'----------------------------------------------'
        )
        # print(winning_candidate_summary)

        


# print(total_votes)
# print(candidate_list) 
# print(candidate_votes)



