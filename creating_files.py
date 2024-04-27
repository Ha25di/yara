############################ For Math Categories in math.json ############################
# import json
# # List of desired categories
# categories_list = [
#     "math.PR", "math.SG", "math.AP", "math.OC", "math.AT",
#     "math.DG", "math.AC", "math.AG", "math.GT", "math.CO",
#     "math.RT", "math.IT", "math.CA", "math.ST", "math.QA",
#     "math.NT", "math.CV", "math.LO"
# ]

# # Initialize a dictionary to keep track of counts per category
# category_counts = {category: 0 for category in categories_list}

# # Prepare to collect entries
# entries = []

# # Open the input file and process each line
# with open('arxiv-metadata-oai-snapshot.json', 'r') as file:
#     for line in file:
#         # Convert JSON line to dictionary
#         data = json.loads(line)
        
#         # Get the categories from the current entry
#         entry_categories = data['categories'].split()

#         # Check if any of the categories in the entry match the desired categories
#         for category in entry_categories:
#             if category in categories_list and category_counts[category] < 100:
#                 entries.append(data)
#                 category_counts[category] += 1
                
#                 # If 100 entries are collected for this category, break the loop
#                 if category_counts[category] == 100:
#                     break

#         # Stop processing if all categories have 100 entries
#         if all(count == 100 for count in category_counts.values()):
#             break

# # Write the collected entries to a new file
# with open('math.json', 'w') as outfile:
#     json.dump(entries, outfile, indent=4)

# print("Data extraction complete. Filtered entries saved to 'math.json'.")

######################################################################################################




############################ For Physics Categories in physics.json ############################

# import json

# # List of desired categories
# categories_list = [
#     "astro-ph", "cond-mat.supr-con", "cond-mat.str-el", "cond-mat.mes-hall",
#     "cond-mat.stat-mech", "cond-mat.mtrl-sci", "hep-lat", "physics.flu-dyn",
#     "physics.plasm-ph", "quant-ph", "nucl-th", "nucl-ex", "gr-qc",
#     "physics.optics", "physics.chem-ph", "physics.gen-ph", "physics.comp-ph",
#     "physics.soc-ph"
# ]

# # Initialize a dictionary to keep track of counts per category
# category_counts = {category: 0 for category in categories_list}

# # Prepare to collect entries
# entries = []

# # Open the input file and process each line
# with open('arxiv-metadata-oai-snapshot.json', 'r') as file:
#     for line in file:
#         # Convert JSON line to dictionary
#         data = json.loads(line)
        
#         # Get the categories from the current entry
#         entry_categories = data['categories'].split()

#         # Check if any of the categories in the entry match the desired categories
#         for category in entry_categories:
#             if category in categories_list and category_counts[category] < 100:
#                 entries.append(data)
#                 category_counts[category] += 1
                
#                 # If 100 entries are collected for this category, break the loop
#                 if category_counts[category] == 100:
#                     break

#         # Stop processing if all categories have 100 entries
#         if all(count == 100 for count in category_counts.values()):
#             break

# # Write the collected entries to a new file
# with open('physics.json', 'w') as outfile:
#     json.dump(entries, outfile, indent=4)

# print("Data extraction complete. Filtered entries saved to 'physics.json'.")

######################################################################################################



############################ For Computer Science Categories in computer_science.json ############################

# import json

# # List of desired categories
# categories_list = [
#     "cs.NE", "cs.AI", "cs.IT", "cs.NI", "cs.PF",
#     "cs.CR", "cs.LG", "cs.CE", "cs.MS", "cs.SC",
#     "cs.HC", "cs.CV", "cs.DB", "cs.SE", "cs.SY",
#     "cs.DC", "cs.PL", "cs.OS"
# ]

# # Initialize a dictionary to keep track of counts per category
# category_counts = {category: 0 for category in categories_list}

# # Prepare to collect entries
# entries = []

# # Open the input file and process each line
# with open('arxiv-metadata-oai-snapshot.json', 'r') as file:
#     for line in file:
#         # Convert JSON line to dictionary
#         data = json.loads(line)
        
#         # Get the categories from the current entry
#         entry_categories = data['categories'].split()

#         # Check if any of the categories in the entry match the desired categories
#         for category in entry_categories:
#             if category in categories_list and category_counts[category] < 100:
#                 entries.append(data)
#                 category_counts[category] += 1
                
#                 # If 100 entries are collected for this category, break the loop
#                 if category_counts[category] == 100:
#                     break

#         # Stop processing if all categories have 100 entries
#         if all(count == 100 for count in category_counts.values()):
#             break

# # Write the collected entries to a new file
# with open('computer_science.json', 'w') as outfile:
#     json.dump(entries, outfile, indent=4)

# print("Data extraction complete. Filtered entries saved to 'cs_categories.json'.")

######################################################################################################


############################ For Quantitative Biology Categories in biology.json ############################

# import json

# # List of desired categories
# categories_list = [
#     "q-bio.NC", "q-bio.PE", "q-bio.QM", "q-bio.MN", 
#     "q-bio.BM", "q-bio.SC", "q-bio.CB", "q-bio.OT"
# ]

# # Initialize a dictionary to keep track of counts per category
# category_counts = {category: 0 for category in categories_list}

# # Prepare to collect entries
# entries = []

# # Open the input file and process each line
# with open('arxiv-metadata-oai-snapshot.json', 'r') as file:
#     for line in file:
#         # Convert JSON line to dictionary
#         data = json.loads(line)
        
#         # Get the categories from the current entry
#         entry_categories = data['categories'].split()

#         # Check if any of the categories in the entry match the desired categories
#         for category in entry_categories:
#             if category in categories_list and category_counts[category] < 100:
#                 entries.append(data)
#                 category_counts[category] += 1
                
#                 # If 100 entries are collected for this category, break the loop
#                 if category_counts[category] == 100:
#                     break

#         # Stop processing if all categories have 100 entries
#         if all(count == 100 for count in category_counts.values()):
#             break

# # Write the collected entries to a new file
# with open('biology.json', 'w') as outfile:
#     json.dump(entries, outfile, indent=4)

# print("Data extraction complete. Filtered entries saved to 'biology.json'.")

######################################################################################################


############################ For Quantitative Finance Categories in finance.json ############################

# import json

# # List of desired categories
# categories_list = [
#     "q-fin.CP", "q-fin.ST", "q-fin.PR"
# ]

# # Initialize a dictionary to keep track of counts per category
# category_counts = {category: 0 for category in categories_list}

# # Prepare to collect entries
# entries = []

# # Open the input file and process each line
# with open('arxiv-metadata-oai-snapshot.json', 'r') as file:
#     for line in file:
#         # Convert JSON line to dictionary
#         data = json.loads(line)
        
#         # Get the categories from the current entry
#         entry_categories = data['categories'].split()

#         # Check if any of the categories in the entry match the desired categories
#         for category in entry_categories:
#             if category in categories_list and category_counts[category] < 100:
#                 entries.append(data)
#                 category_counts[category] += 1
                
#                 # If 100 entries are collected for this category, break the loop
#                 if category_counts[category] == 100:
#                     break

#         # Stop processing if all categories have 100 entries
#         if all(count == 100 for count in category_counts.values()):
#             break

# # Write the collected entries to a new file
# with open('finance.json', 'w') as outfile:
#     json.dump(entries, outfile, indent=4)

# print("Data extraction complete. Filtered entries saved to 'finance.json'.")

######################################################################################################


############################ For Statistics Categories in statistics.json ############################

# import json

# # List of desired categories
# categories_list = [
#     "stat.TH", "stat.ME", "stat.AP",  # Statistics categories
#     "nlin.CD", "nlin.PS", "nlin.SI"  # Nonlinear sciences categories
# ]

# # Initialize a dictionary to keep track of counts per category
# category_counts = {category: 0 for category in categories_list}

# # Prepare to collect entries
# entries = []

# # Open the input file and process each line
# with open('arxiv-metadata-oai-snapshot.json', 'r') as file:
#     for line in file:
#         # Convert JSON line to dictionary
#         data = json.loads(line)
        
#         # Get the categories from the current entry
#         entry_categories = data['categories'].split()

#         # Check if any of the categories in the entry match the desired categories
#         for category in entry_categories:
#             if category in categories_list and category_counts[category] < 100:
#                 entries.append(data)
#                 category_counts[category] += 1
                
#                 # If 100 entries are collected for this category, break the loop
#                 if category_counts[category] == 100:
#                     break

#         # Stop processing if all categories have 100 entries
#         if all(count == 100 for count in category_counts.values()):
#             break

# # Write the collected entries to a new file
# with open('statistics.json', 'w') as outfile:
#     json.dump(entries, outfile, indent=4)

# print("Data extraction complete. Filtered entries saved to 'statistics.json'.")

######################################################################################################