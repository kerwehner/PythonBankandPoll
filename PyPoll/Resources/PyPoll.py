# import libraries
import csv
import os

# load and output
# file_to_load = csvpath = "election_data.csv"
# file_to_output = csvpath = "election_analysis.txt"
file_to_load = os.path.join("election_data.csv")
file_to_output = os.path.join("election_analysis.txt")

# track parameters
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

# extract Data from election_data.csv to create three columns: `Voter ID`, `County`, and `Candidate`
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

# read each row of data after the header and loop through rows
    for row in reader:
        print(". ", end=""),
        total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
with open(file_to_output, "w") as txt_file:

# print the final vote count to terminal
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")
        txt_file.write(voter_output)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    
# export the final vote count to a text file
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)