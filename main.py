from prettytable import PrettyTable 
  
# Specify the Column Names while initializing the Table 
myTable = PrettyTable(["", "List", "Array", "Tuple"]) 
  
# Add rows 
myTable.add_row(["Is it mutable? ", "Yes", "Yes", "No"]) 
myTable.add_row(["Can we change the size after creation? ", "Yes", "Yes", "No"]) 
myTable.add_row(["Can items in the list be changed? ", "Yes", "Yes", "No"]) 
myTable.add_row(["How many different types of data can be stored ", "All", "Yes", "Only same type"])
  
print(myTable)