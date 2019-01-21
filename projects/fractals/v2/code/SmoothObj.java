import java.io.*;

public class SmoothObj {

    public static void main(String[] args) throws FileNotFoundException {
        Image img = new Image();
        img.width = 200;
        img.height = 100;
        
        // Set the pixels
        for(int x = 0; x < img.width; ++x) {
            for(int y = 0; y < img.height; ++y) {
                img.set(x,y, x/(float)img.width,0,y/(float)img.height);
            }
        }
        // Write out the file
        img.write("smooth.ppm");
    }
}
