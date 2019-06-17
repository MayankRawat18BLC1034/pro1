emp={}
cab={}
empid=1
cabid=1
def func_hr(empid):
    name=input("Enter the name of the emp:")
    salary=int(input("Enter the salary:"))
    inc=int(input("Enter the increment"))
    n_sal=salary+salary*inc
    emp[empid] = dict()
    emp[empid]={"name":name,
                "salary":salary,
                "new salary":n_sal}
    empid+=1
def func_logistics():
    c_route=input("Enter the cab route:")
    c_reg=input("Enter the region:")
    cab[cabid]={"route":c_route,
                "region":c_reg}
                
def func_emp():
    print(emp)
    print(cab)
func_hr(empid)
func_logistics()
func_emp()

    
    
    
    
    
