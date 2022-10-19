# 3.2.10
'''
counties = ["Arapahoe", "Denver", "Jefferson"]

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(counties_dict.get(county))

print("Alternate Method")

for voters in counties_dict.values():
    print(voters)

print("Get key and value")

for county, voters in counties_dict.items():
    print(county, voters)

print("Formated")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registerd voters.")
'''
'''
# Lists of dictionaries

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for i in range(len(voting_data)):
    print(voting_data[i]['county'])

print()
print("Retrieve registered voters count")
print()

for county_dict in voting_data:
    print(county_dict['registered_voters'])

print()
print("Retrieve only county name")
print()

for county_dict in voting_data:
    print(county_dict["county"])
'''
# 3.2.11
'''
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

# BECOMES
print()

for county, voters in counties_dict.items():
    print(f'{county} county ahs {voters} registered voters.')

candidate_votes = int(input("How many votes did you get? "))
total_votes = int(input("What was the total number of votes? "))
message = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes."
)

print(message)
'''
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(f'{county} county has {voters:,} registered voters.')

print()
print("From list of dictionaries")
print()

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(f'{county_dict["county"]} county has {county_dict["registered_voters"]} registered voters.')