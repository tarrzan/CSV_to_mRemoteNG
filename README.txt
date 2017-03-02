Version 1.0 Release 3/1/2017


Format for CSV:
	FileName="template.csv" Currently hardcoded future functionality will be able to choose file
	Headers= FolderName|Ip Address|Enviroment|UserField|Ip Address|Enviroment|UserField|Ip Address|Enviroment|UserField
	Headers are required as the breakit2.py pops the first line out of the file and throws it out
	Add many connections under one folder by adding more  Ip Address|Enviroment|UserField in groups of 3

	
Output:
	Sorts "FolderName" folders into directories A-Z and then each connection gets added to the "FolderName" as "FolderName" + "Enviroment" as the name.

	
