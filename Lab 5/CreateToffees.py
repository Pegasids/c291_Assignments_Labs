#c291-23rd feb-python
# Note: Python does not have an auto commit. Thus, commit at the end of each statement is important.
# python3 createToffees.py
# File from introduction to cx_oracle
 
 
 
import sys
import cx_Oracle # the package used for accessing Oracle in Python
import getpass # the package for getting password from user without displaying it
 
 
 
def createTable():
    
    # get username
    user = input("Username [%s]: " % getpass.getuser())
    if not user:
   		 user=getpass.getuser()
    
    # get password
    pw = getpass.getpass()
 
    # The URL we are connnecting to
    conString=''+user+'/' + pw +'@gwynne.cs.ualberta.ca:1521/CRS'
    
    # SQL statement to execute
    createStr = ("create table TOFFEES "
    "(T_NAME VARCHAR(32), SUP_ID INTEGER, PRICE FLOAT, SALES INTEGER, TOTAL INTEGER)")
    
    try:
   	 # Establish a connection in Python
   	 connection = cx_Oracle.connect(conString)
 
   	 # create a cursor  
   	 curs = connection.cursor()
   	 curs.execute(createStr)
   	 
   	 data = [('Quadbury', 101, 7.99, 0, 0)]
 
   	 cursInsert = connection.cursor()
   	 cursInsert.bindarraysize = 1
   	 cursInsert.setinputsizes(32, int, float, int, int)
   	 cursInsert.executemany("INSERT INTO TOFFEES(T_NAME, SUP_ID, PRICE, SALES, TOTAL) "
                                	"VALUES (:1, :2, :3, :4, :5)", data);
   	 connection.commit()
   	 
   	 # executing a query
   	 curs.execute("SELECT * from TOFFEES")
   	 # get all data and print it
   	 rows = curs.fetchall()
   	 for row in rows:
   		 print(row)
   	 
   	 # close the connection
   	 curs.close()
   	 cursInsert.close()
   	 connection.close()
 
    except cx_Oracle.DatabaseError as exc:
   	 error, = exc.args
   	 print( sys.stderr, "Oracle code:", error.code)
   	 print( sys.stderr, "Oracle message:", error.message)
   	 
if __name__ == "__main__":
    createTable()

