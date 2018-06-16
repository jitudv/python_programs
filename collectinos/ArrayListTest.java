import java.util.ArrayList;
import java.util.*;

class ArrayListTest
{
   public static void main(String[] args) {
    ArrayList<String>  list = new ArrayList<>();
    list.add("jitu");  list.add("amit");  list.add("rajesh");  list.add("vikash");
    ArrayList<String> names2 = new ArrayList<>();
    names2.add("sumit");  names2.add("rani");  names2.add("rajat");  names2.add("virendra");
    names2.add("rajesh");
    names2.add("viraj");
    list.addAll(names2);
    System.out.println("size of list  = \t "+list.size());
    list.sort(Comparator.Asseinding);
    int index=0;
    for(String name: list)
    {

        System.out.println("name is at index  \t "+index+"\t and data is  = \t "+name);
        //index=index+1;
        index++;
    }
    System.out.println(" now we are out of  looop ");
    
   }
   

}