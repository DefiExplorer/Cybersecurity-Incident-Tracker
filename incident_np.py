import incident_parser as inp
import numpy as np

def analyze_incidents(filename):
    incidents = inp.parse_incidents(filename) #getting the data from parser
    incident_array = np.array(incidents) # Creating 2D numpy array
    # Now below we take out the severity rating column rows for some calculations
    sev = incident_array[:,4].astype(int) # all rows and 4th column index wise...typecasting to integer.
    # Below loop just to check if numbers are getting stored.
    '''
    for _ in sev:
        print(_)
    '''
    # Now we calculate some stats, using numpy fast functions instead of manual loops
    average_sev = np.mean(sev)
    total_incidents = len(sev)
    unique_ips_count = len(np.unique(incident_array[:,3])) #IP data at 3rd column...index wise.
    # Getting names of critical incidents
    incident_names = incident_array[:,2] # All incidents names
    critical_incidents = [] # Empty list to store critical incidents
    # Used loop since column index will be same for severity rating and all incident name when we go 1 by 1.
    for index,value in enumerate(sev):
        if value >=4:
            critical_incidents.append(incident_names[index])

    return sev, average_sev, total_incidents, unique_ips_count, incident_names, critical_incidents
#-----main-----
list_analysed = analyze_incidents('incidents.txt')
# Below print just for debug purpose.
#print(list_analysed[-1],list_analysed[2],len(list_analysed[-1]),len(list_analysed[-2]))