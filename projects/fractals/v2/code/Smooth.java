import java.io.*;

public class Smooth {
    static int width = 200;
    static int height = 100;
    
    static float[] red = new float[width * height];
    static float[] green = new float[width * height];
    static float[] blue = new float[width * height];    

    static void set(int x, int y, float r, float g, float b) {
        int i = x + y * width;
        red[i] = r;
        green[i] = g;
        blue[i] = b;
    }

    static int colourToInt(float c) {
        return (int)(c * 255);
    }

    static void write(String fileName) throws FileNotFoundException {
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

    public static void main(String[] args) throws FileNotFoundException {
        // Set the pixels
        for(int x = 0; x < width; ++x) {
            for(int y = 0; y < height; ++y) {
                set(x,y, x/(float)width,0,y/(float)height);
            }
        }
        // Write out the file
        write("smooth.ppm");
    }
}