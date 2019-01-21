import java.io.*;
public class FileOutputTest {
    public static void main(String[] args) throws FileNotFoundException {
        PrintStream ps = new PrintStream("hello.txt");
        ps.println("Hello, File!");
        ps.close();
    }
}
