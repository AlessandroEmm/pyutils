import sqlite3
import sys
import tools

class dbsqlite(object):
    #Constructor
    def __init__(self, databaseName):
        try:
            self.connection = sqlite3.connect(databaseName, check_same_thread = False)
            print("[DEBUG] sqlManager instance connected to " + databaseName)
        except:
            print("[ERROR] Could not connect to database " + databaseName + "(" + str(sys.exc_info()) + ")")
 
    #Destructor
    def __del__(self):
        try:
            self.connection.close()
        except:
            print("[ERROR] Could not close database connection (" + str(sys.exc_info()) + ")")
 

    #Execute query """
    def execute(self, executionString):
        self.cursor = self.connection.cursor() # just a secured call to self.connection.cursor() 
        #print "[DEBUG] Executing " + executionString
        if self.cursor is not None:
            try:
                print(exec)
                self.cursor.execute(executionString)
            except:
                print("[ERROR] Could not execute cursor " + executionString + " (" + str(sys.exc_info()) + ")")

    # Commit Change
    def commit(self):
        if self.connection is not None:
            try:
                self.connection.commit()
            except:
                print("[ERROR] Could not push changes to database (" + str(sys.exc_info()) + ")")

    # Create a table in database

    def update(self, table, where, columnValue):
        executionString = "UPDATE " + table + " SET "  + tools.dictToStr(columnValue, " = ", " , ") 
        if where is not None:
            executionString += " WHERE " + tools.dictToStr(where, "=", "and") + ";"
            print(executionString)
        self.execute(executionString)
     
    # Insert object (array) into database)
    def insertInto(self, table, columnValue):
        executionString = "INSERT INTO " + table + " VALUES" + tools.dictToStr(columnValue, "=", ",") 
        self.execute(executionString)
     
     
    # Select and fetch data
    def select(self, tableName, whereClause='', fields=None):
        seperator = ","
        if fields is None:
          executionString = "SELECT * FROM " + tableName + whereClause
        else:
            executionString = "SELECT " +  seperator.join(fields) + " FROM " + tableName + whereClause
        self.execute(executionString)
        try:
            return self.cursor.fetchall()
        except:
            print("[ERROR] Could not fetch data (" + str(sys.exc_info()) + ")")
            return None

