import java.io.*;
import java.io.FileOutputStream;
class home
{
  public static void main(String[] args) 
  {
    FileInputStream fin =  new FileInputStream("first.pys");
     
     if(fin != null)
     {
      int i ;
      while((i= fin.read()) != -1)
      {
      StringBuffer buf = new StringBuffer((char)i);
      }
     }
 }
}