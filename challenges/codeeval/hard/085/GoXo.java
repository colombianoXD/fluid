//import java.io.*;
import java.io.File;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public final class Main {

    private Main() { }
    public static void main(final String[] args) throws IOException {
    File filename = new File(args[0]);
    BufferedReader reader = new BufferedReader(new FileReader(filename));
    String line;
    final int bNum = 3;
    final int cNum = 4;
    final int rNUM = 5;

    while ((line = reader.readLine()) != null) {
        String[] parts = line.split(",");
        ArrayList<Integer> m = new ArrayList<Integer>();

        int n = Integer.parseInt(parts[0]);
        int k = Integer.parseInt(parts[1]);
        int a = Integer.parseInt(parts[2]);
        int b = Integer.parseInt(parts[bNum]);
        int c = Integer.parseInt(parts[cNum]);
        int r = Integer.parseInt(parts[rNum]);

        m.add(a);
        for (int i = 1; i < k; i++) {
            m.add(((b * m.get(i - 1)) + c) % r);
        }

        for (int j = k; j < n; j++) {

            List<Integer> mSub = new ArrayList<Integer>(m.subList(j - k, j));
            int min = 0;
            while (mSub.contains(min)) {
               min++;
            }
            m.add(min);
        }
        System.out.println(m.get(n - 1));
        }
    }
}
