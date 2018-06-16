import java.util.Scanner;
import java.io.*;
class charTest
{
    public static void main(String[] args) throws IOException 
    {
    
    StringBuffer buf  = new StringBuffer();
    try{    Scanner sc = new Scanner(System.in);
    FileReader fin    =  new FileReader("/home/jays/Desktop/python_programms/first.py");    
    int i ;
    while((i = fin.read()) != -1)
    {
     buf.append(((char)i));
    }
    System.out.println("\n this si my file Write ");

    FileWriter fout  = new FileWriter("/home/jays/Desktop/python_programms/first.py");
    System.out.println("Enter data what do you want to write ");
    String data = sc.nextLine();
    buf.append(data);
    fout.write((buf.toString()));
    buf = null;
    fout.close();
}
catch( Exception  e)
{
    System.out.println(e.getMessage());
}
    }
}