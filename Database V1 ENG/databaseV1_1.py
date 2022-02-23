#***************************************************************************

from myMariaDB import *
from printSplash import *

#***************************************************************************
verificator()
logging.basicConfig(filename="logs.logs", encoding='utf-8', level= logging.INFO)

#***************************************************************************

log_program_started()

#***************************************************************************

printSplash()

#***************************************************************************

connect()

#***************************************************************************

#Here we will define the querys that we want to use
#Query 1

query1 = """select distinct
concat ( employees.last_name , ", " , first_name ) as "Employee Last, First Name",
birth_date as "Birth Date",
employees.emp_no,
dept_name as "Department Name",
sum(salaries.salary) as "Salary Total"
from employees , salaries , departments , dept_emp
where employees.emp_no = salaries.emp_no
and departments.dept_no = dept_emp.dept_no
and dept_emp.emp_no = employees.emp_no
and employees.emp_no like '2667_'
group by 1 , 2 , 3 , 4 
order by birth_date desc
limit 500;"""

#Query 2

query2 = """select
employees.emp_no as "Employee Number",
employees.first_name as "First Name",
employees.last_name as "Last Name",
employees.birth_date as "Birth Date",
salaries.salary as "Salary"
from employees , salaries
where employees.emp_no like '2667_'
and employees.emp_no = salaries.emp_no
limit 500; """

#Query 3

query3 = """select 
concat ( employees.last_name , ", " , employees.first_name ) as "Employee Name",
employees.birth_date as "Birth Date",
employees.emp_no,
departments.dept_name as "Department Name",
sum(salaries.salary) as "Salary Total"
from employees , salaries , departments , dept_emp
where employees.emp_no = salaries.emp_no
and departments.dept_no = dept_emp.dept_no
and dept_emp.emp_no = employees.emp_no
and employees.emp_no like  ('4999%')
group by 1 , 2 , 3 , 4 
order by emp_no desc
limit 50;"""

#***************************************************************************

#Here we define the headers for the query_tabel() function


header1 = ['Name', 'Birthday Date', 'Employee no.', 'Job', 'Salary']
header2 = ['Employee no.', 'First Name', 'Last Name', 'Birthday Date', 'Salary']
header3 = ['Employee Name', 'Birth Date', 'emp_no', 'Department name','Salary Total']

#***************************************************************************

#We execute the function tabel() for query1/2/3 with their headers

print("\n*************************Query table nº1*************************\n")
query_table(query1, header1)
print("\n*************************Query table nº2*************************\n")
query_table(query2, header2)
print("\n*************************Query table nº3*************************\n")
query_table(query3, header3)

#***************************************************************************


disconnect()

#***************************************************************************

log_program_ended()

#***************************************************************************
