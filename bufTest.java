
import java.io.*;

import org.omg.CORBA.Any;
import org.omg.CORBA.Object;
import org.omg.CORBA.TypeCode;
import org.omg.CORBA_2_3.portable.InputStream;
class bufTest
{
    public static void main(String[] args) throws IOException
    {
    FileReader fin  = new FileReader("/home/jays/Desktop/python_programms/first.py");
    BufferedReader  buf = new BufferedReader(fin);
    System.out.print(buf.readLine());
    System.out.println("\n  Enter  line of string ");
 } 
}


