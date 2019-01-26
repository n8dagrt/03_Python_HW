# The total number of votes cast

  # A complete list of candidates who received votes

  # The percentage of votes each candidate won

  # The total number of votes each candidate won

  # The winner of the election based on popular vote.


# Load Dependencies

import csv
import os

# Load files for input and output

file_to_load = os.path.join("Resources", "votedata.csv")
file_to_output = os.path.join("Text Output Analysis", "vote_analysis_outcome.txt")

# Total Vote Counter
allvotes = 0

# Candidate Options and Vote Counters
options = []
votes = {}

# Winning Candidate and Winning Count Tracker
winner = ""
winnercount = 0
# Candidate Options and Vote Counters
options = []
votes = {}
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as votedata:
    reader = csv.reader(votedata)

    # Read the header
    header = next(reader)

    # For each row...
    for row in reader:

        # Run the loader animation
        print(". ", end=""),

        # Add to the total vote count
        allvotes = allvotes + 1

        # Extract the candidate name from each row
        Canditates = row[2]

        # If the candidate does not match any existing candidate...
        # (In a way, our loop is "discovering" candidates as it goes)
        if Canditates not in options:

            # Add it to the list of candidates in the running
            options.append(Canditates)

            # And begin tracking that candidate's voter count
            votes[Canditates] = 0

        # Then add a vote to that candidate's count
        votes[Canditates] = votes[Canditates] + 1

# Create text results and create text file

with open(file_to_output, "w") as txt_file:
    
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    
    txt_file.write(election_results)

    # Count the votes to find the winner
    
    
    for candidate in candidate_votes:

        
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(WinnerCanditateInfo)