import java.io.*;

public class Heart {
    static int width = 5;
    static int height = 4;
    
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
        set(1,0, 1,0,0);
        set(3,0, 1,0,0);
        
        set(0,1, 1,0,0);
        set(1,1, 1,0,0);
        set(2,1, 1,0,0);
        set(3,1, 1,0,0);
        set(4,1, 1,0,0);
        
        set(1,2, 1,0,0);
        set(2,2, 1,0,0);
        set(3,2, 1,0,0);
        
        set(2,3, 1,0,0);
        
        // Write out the file
        write("heart-from-java.ppm");
    }
}