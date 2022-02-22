#***************************************************************************
#Fazemos import do nosso módulo - myMariaDB
#Fazemos import do printSplash que permite apagar a consola

from myMariaDB import *
from printSplash import *

#***************************************************************************
verificador()
logging.basicConfig(filename="logs.logs", encoding='utf-8', level= logging.INFO)

#***************************************************************************

log_program_started()

#***************************************************************************
#Corremos a função printSplash() para limpar a consola
printSplash()

#***************************************************************************

#Corremos a função connect() para estabelecer a ligação com a base de dados
connect()

#***************************************************************************

#Definimos as querys que iremos utilizar na função tabela()
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

#Definimos as headers que iremos utilizar na função tabela()
#Estes contêm o título de cada coluna
header1 = ['Name', 'Birthday Date', 'Employee no.', 'Job', 'Salary']
header2 = ['Employee no.', 'First Name', 'Last Name', 'Birthday Date', 'Salary']
header3 = ['Employee Name', 'Birth Date', 'emp_no', 'Department name','Salary Total']

#***************************************************************************

#Executamos a função tabela para query1 e query2 com os respetivos headers
print("\n*************************Tabela da query nº1*************************\n")
query_table(query1, header1)
print("\n*************************Tabela da query nº2*************************\n")
query_table(query2, header2)
print("\n*************************Tabela da query nº3*************************\n")
query_table(query3, header3)

#***************************************************************************

#Excutamos a função disconnect que permite terminar a conexão com a base de dados
disconnect()

#***************************************************************************

log_program_ended()

#***************************************************************************
