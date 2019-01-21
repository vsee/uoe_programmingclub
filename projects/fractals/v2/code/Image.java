import java.io.*;

public class Image {
    public int width = 200;
    public int height = 100;
    
    public float[] red = new float[width * height];
    public float[] green = new float[width * height];
    public float[] blue = new float[width * height];    

    public void set(int x, int y, float r, float g, float b) {
        int i = x + y * width;
        red[i] = r;
        green[i] = g;
        blue[i] = b;
    }

    public int colourToInt(float c) {
        return (int)(c * 255);
    }

    public void write(String fileName) throws FileNotFoundException {
        PrintStream ps = new PrintStream(fileName);
        ps.println("P3");
        ps.println(width + " " + height);
        ps.println(255);
        
        for(int i = 0; i < width * height; ++i) {
            ps.print(colourToInt(red[i]) + " ");
            ps.print(colourToInt(green[i]) + " ");
            ps.print(colourToInt(blue[i]) + " ");
        }
        
        ps.close();
    }
}