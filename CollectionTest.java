import java.util.ArrayList;
import java.util.Iterator;
class Employee
{
    String name ;
    int age ;
    float salary;
    String adddress;
    long id;
    public Employee(String name, int age,float salary, String adress,long id)
    {
        this.name=name;
        this.age =age;
        this.adddress =adress;
        this.salary =salary;
        this.id =id;
   
    }
   public Employee()
    {
        // this  is my an empty constructor 
    }
    
}


class CollectionTest
{

    public static void main(String[] args) 
    {
    ArrayList<Employee> emplist = new ArrayList<>();
    emplist.add(new Employee("amit",25, 2525.25f,"khargone",252536l));
    emplist.add(new Employee("rajesh",25, 2525.25f,"badwani",252536l));
    emplist.add(new Employee("sumit",25, 2525.25f,"burhanpur",252536l));
    emplist.add(new Employee("jitu",25, 2525.25f,"indore",252536l));
    emplist.add(new Employee("amit",25, 2525.25f,"khargone",252536l));
    emplist.add(new Employee("amit",25, 2525.25f,"khargone",252536l));
    emplist.add(new Employee("amit",25, 2525.25f,"khargone",252536l));
    emplist.add(new Employee("amit",25, 2525.25f,"khargone",252536l));
    emplist.add(new Employee("amit",25, 2525.25f,"khargone",252536l));
    emplist.add(new Employee("amit",25, 2525.25f,"khargone",252536l));
    emplist.add(new Employee("amit",25, 2525.25f,"khargone",252536l));
    emplist.add(new Employee("amit",25, 2525.25f,"khargone",252536l));
    emplist.add(new Employee("amit",25, 2525.25f,"khargone",252536l));

    Iterator itr = emplist.iterator();
    while(itr.hasNext())
    {
    Employee emp  =(Employee)itr.next();
    System.out.println("name of  =\t"+emp.name+"\t age of =\t "+emp.age+"\t salary =\t "+emp.salary+"\t address of  =\t"+emp.adddress+"\t id of =\t "+emp.id);

    }
    System.out.println(" now  we are in main ");
         
    }
}