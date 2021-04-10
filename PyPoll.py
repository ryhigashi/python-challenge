import os
import csv

ifile = "03-Python_hw_Instructions_PyPoll_Resources_PyPoll_Resources_election_data.csv"
ofile = "PyPoll.txt"

#Variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#opening and reading csv
with open(ifile, encoding='utf-8') as inputfile: 
	reader = csv.DictReader(inputfile)

	reader_header = next(reader)

	for row in reader:
		#The total number of votes cast
		total_votes = total_votes + 1

		#A complete list of candidates who received votes
		if (row["Candidate"]=="Khan"):
			khan_votes = khan_votes + 1
		elif (row["Candidate"] == "Correy"):
			correy_votes = correy_votes + 1
		elif (row["Candidate"] == "Li"):
			li_votes = li_votes + 1
		elif (row["Candidate"] == "O'Tooley"):
			otooley_votes = otooley_votes + 1


		#The percentage of votes each candidate won
khan_vote_percentage = khan_votes / total_votes
correy_vote_percentage = correy_votes / total_votes
li_vote_percentage = li_votes / total_votes
otooley_vote_percentage = otooley_votes / total_votes

		


		#The winner of the election based on popular vote.

max_votes = max(khan_votes,correy_votes,li_votes,otooley_votes)
if khan_votes == max_votes:
	election_winner = "Kahn"
elif correy_votes == max_votes:
	election_winner = "Correy"
elif li_votes == max_votes:
	election_winner = "Li"
elif otooley_votes == max_votes:
	election_winner ="Otooley"


output = 	(f"Election Results \n"
			f"---------------------------\n"
			f"Total Votes: {total_votes}\n"
			f"---------------------------\n"
			f"Kahn: {khan_vote_percentage:.3%} ({khan_votes})\n"
			f"Correy: {correy_vote_percentage:.3%} ({correy_votes})\n"
			f"Li: {li_vote_percentage:.3%} ({li_votes})\n"
			f"O'Tooley: {otooley_vote_percentage:.3%} ({otooley_votes})\n"
			f"---------------------------\n"
			f"Winner: {election_winner}\n"
			f"---------------------------")

print(output)

with open(ofile, 'w',) as txtfile:
	txtfile.write(output)