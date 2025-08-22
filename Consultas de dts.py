# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 01:01:00 2020

@author: Emmanuel
"""
# imports
import os
from lxml import etree


# set sql output directory
sql_out = r"C:\temp\dtsxsql"
if not os.path.isdir(sql_out):
    os.makedirs(sql_out)

# dtsx files
dtsx_path = r'C:\Users\Emmanuel\Documents\SSIS - INFORMACIONAL_INT\SSIS - INFORMACIONAL_INT'
ssis_dtsx = dtsx_path + r'\ImportFile_FST014.dtsx'


tree = etree.parse(ssis_dtsx)
root = tree.getroot()

# collect unique element tags in dtsx
ele_set = set()
for ele in root.xpath(".//*"):
    ele_set.add(ele.tag)    
print(ele_set)
print(len(ele_set))


# extract sql code in source statements and write to *.sql files 
total_bytes = 0
package_name = root.attrib['{www.microsoft.com/SqlServer/Dts}ObjectName'].replace(" ","")
for cnt, ele in enumerate(root.xpath(".//*")):
  if ele.tag == "{www.microsoft.com/SqlServer/Dts}Executable":
    attr = ele.attrib
    for child0 in ele:
      if child0.tag == "{www.microsoft.com/SqlServer/Dts}ObjectData":
        for child1 in child0:
          sql_comment = attr["{www.microsoft.com/SqlServer/Dts}ObjectName"].strip()
          if child1.tag == "{www.microsoft.com/sqlserver/dts/tasks/sqltask}SqlTaskData":
            dtsx_sql = child1.attrib["{www.microsoft.com/sqlserver/dts/tasks/sqltask}SqlStatementSource"]
            dtsx_sql = "-- " + sql_comment + "\n" + dtsx_sql
            sql_file = sql_out + "\\" + package_name + str(cnt) + ".sql"
            total_bytes += len(dtsx_sql)
            print((len(dtsx_sql), sql_comment, sql_file))
            with open(sql_file, "w") as file:
              file.write(dtsx_sql)
print(('total sql code bytes',total_bytes))


