'''
We will use our incident_parser.py file to get the raw data for SQLite. We should have original data stored in a database.
Any processed data is not a good idea to store hence incident_np.py file is not used.
In Simple Terms: "SQL needs raw data!"
'''
# Python has inbuilt SQLite module
import sqlite3 as sq3
from incident_parser import parse_incidents
# Got to know about this Library for better output display format specially for tablular data.
from tabulate import tabulate

# We will create a function named managed_incidents
def managed_incidents(filename):
    incidents = parse_incidents(filename) # Our parser function will return list of lists.
    # Setting up Database now -->
    conn = sq3.connect('incidents.db') # Creates (if doesn't exist)/ Connects to database named incidents.db
    c = conn.cursor() # This cursor will help us to provide sql queries.
    # We drop/clear table with same name if exists (Optional thing to do)
    c.execute('DROP TABLE IF EXISTS incidents')

    # Now we create a table with columns that match our log-data.
    c.execute('''CREATE TABLE IF NOT EXISTS incidents (date TEXT,time TEXT,incident_type TEXT,ip_address TEXT,
              severity_rating INTEGER,target_system TEXT)
              ''')
# Recommended format for sql column names is to use snake_case to avoid spaces or camelCase, keeping all letters lowercase is preferred.
    # Now we also use the concept of Transaction in SQL (checkpoint,rollback,commit) and start with inserting data.
    try:
        # All insertion will happen in a single transaction, if anything fails we rollback!
        for row in incidents:
            sev = int(row[4]) # since we know severity rating is at index no 4.
            if sev<1 or sev >5:
                raise ValueError(f'Invalid {sev} in {row}!')
            else:
                
                c.execute('INSERT INTO incidents VALUES (?,?,?,?,?,?)', row)
        '''
        #c.executemany('INSERT INTO incidents VALUES (?,?,?,?,?,?)', incidents)
        I had to perform check on each row severity rating value, therefore didn't do this.
        Alternate way was to store validated rows into new_list and than executemany('',new_list) was possible.
        '''
        conn.commit()
        # c.commit() won't work as c is like a pointer to a cursor that handles queries only.
        # conn handles connection to database.
        print('Transaction Successfully commited: All Data saved.')
    except ValueError as e:
        # Rollback if anything fails
        conn.rollback()
        print("Error!",e,"Transaction rollback done!")
        conn.close()
        return None
    #------------------------------------------------------------------------------------------------------------------------#
    # Displaying the table in console for custom SQL query input from user.
    '''
    print("\nCurrent Incidents Table:")
    print("Date       | Time  | Incident Type | IP Address   | Severity Rating| Target System")
    print("-" * 80)
    c.execute("SELECT * FROM incidents")
    rows = c.fetchall()
    for row in rows:
        # Using proper format to display rows.
        print(f"{row[0]} | {row[1]} | {row[2]:<13} | {row[3]:<12} | {row[4]:<12} | {row[5]}")
    '''
    c.execute("SELECT * FROM incidents")
    rows = c.fetchall()
    column_names = ['date','time','incident_type','ip_address','severity_rating','target_system']
    print(tabulate(rows, headers=column_names, tablefmt="grid"))
    #------------------------------------------------------------------------------------------------------------------------#
    # Getting user input as string only.
    print("\nEnter a SQL SELECT query (e.g., 'SELECT incident_type, COUNT(*) FROM incidents GROUP BY incident_type'):")
    user_query = input("Enter Your Query>> ")
    
    # Passing user input inside try block to handle issue. 
    try:
        if not user_query.strip().lower().startswith("select"):
            raise sq3.Error("Only SELECT queries are allowed.")
        # Validation check performed to avoid SQL Injection! (It's a security project so I made sure that attack on database is avoided :)).
        c.execute(user_query)
        results = c.fetchall()
        '''
        print("\nQuery Results:")
        for result in results:
            print(result)  # Prints each row as a tuple
        
        '''
        # Better Display of user queried result, using tabulate module --->
        print("\nQuery Results:")
        if results:
            # Dynamically generate column names from the cursor description
            query_column_names = [desc[0] for desc in c.description]  # Extract column headers from the query
            print(tabulate(results, headers=query_column_names, tablefmt="grid"))  # Use tabulate for output
        else:
            print("No results found for your query.")
            '''Concept of cursor.description
                The c.description attribute is a tuple
                of tuples that provides metadata about the columns in the result set of the most recent query executed by the cursor.
                Each inner tuple corresponds to one column, and the first item (index 0) of each tuple is the name of the column.
                Hence desc[0] is used.
            '''
    except sq3.Error as e:
        print(f"Error executing query: {e}")
        print("Make sure your query is a valid SELECT statement.")

    # Close the connection
    conn.close()

#----Main----
managed_incidents('incidents.txt')