#Function to parse incidents.txt and return a list of incidents
def parse_incidents(filename):
    # Open File, 'r' means read mode and variable file_object to interact with the file.
    with open(filename,'r') as file_object:

        # List to store the incidents.
        all_incidents = [] # Empty list for now

        #Using for loop to read line-by-line, file_object acts like list of lines we can iterate over.
        for line in file_object:
            cleaned_line = line.strip() # Remove any extra space or newline characters.

            if not cleaned_line: # we will skip any empty lines
                continue
            if cleaned_line.startswith("#"):
                continue
            # we will skip any line (in which I have explictly put # in file to skip it, it is 1st line in our example txt file).

            columns = cleaned_line.split(',') # since we have a csv, we split them at comma (,)
            # print(len(columns)) # Used intially to check if each line has required number of columns (6 to be exact in our file).
            if len(columns)!=6:
                print(f'Warning! Skipping invalid line{cleaned_line}.')
                continue
            # Now after all the checks are done! we append the processed lines to our all_incidents list.
            all_incidents.append(columns)
    return all_incidents

#_____main_______
incidents = parse_incidents('incidents.txt')
#print(f'Our processed log file output: \n{incidents}')