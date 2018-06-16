import java.io.*;
import java.util.Scanner;
public class fileread implements Serializable 
{
    public static void main(String[] args) throws IOException
     {
        FileInputStream fin = new FileInputStream("/home/jays/Desktop/python_programms/first.py");
        int j;
        StringBuffer old = new StringBuffer();
        while((j=fin.read()) != -1)
        {
            old.append((char)j);
        }
        if(old != null)
        {
            System.out.println("yes you have file data ");
            System.out.print(old);
        }
        System.out.println("");
        FileOutputStream fout=new FileOutputStream("/home/jays/Desktop/python_programms/first.py");
        if(fout != null)
        {
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter text ");
            String msg =new String();
            msg = sc.nextLine();
            byte i[]=msg.getBytes();
            fout.write(i);
        }
        else 
        {
        System.out.println("your file does not found ");
        }
     }
    
}