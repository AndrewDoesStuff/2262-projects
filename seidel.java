public class seidel {
    public static double[] GaussSeidel(double[] x, double[][] a, double [] b) {
        for(int i = 0; i < a.length; i++) {
            double temp = b[i];
            for(int j = 0; j < a.length; j++) {
                if(i != j) { 
                    temp -= a[i][j] * x[j];
                }
            x[i] = temp / a[i][i];
            }
        }
        return x;
    }
    public static double convergenceTest(double[] x) {
        double total = 0; 
        for(int i = 0; i < x.length; i++) {
            total += Math.pow(x[i], 2);
        }
        return Math.sqrt(total);
    }
    public static void main(String[] args) {
        double[][] a = {
            {4, -1, 0, -1, 0, 0},
            {-1, 4, -1, 0, -1, 0},
            {0, -1, 4, 0 , 0, -1},
            {-1, 0 , 0, 4, -1, 0},
            {0, -1, 0, -1, 4, -1},
            {0, 0, -1, 0, -1, 4}
        };
        double[] b = {0, 5, 0, 6, -2, 6};
        double[] x = new double[b.length];
        double currDiff = 0;
        double lastDiff = 0;
        System.out.printf("%-15s", "k");
        for(int i = 0; i < a[1].length; i++) { // Considering they are square, each has to be the same so using 1 is fine
            System.out.printf("%-15s", "x" + i);
            if(i == a[1].length - 1) { // find the end and then writing a new line.
                System.out.printf("%-15s", "Diff");
                System.out.printf("\n");
            }
        }        
        for(int i = 0; i < 12; i++) {
            System.out.printf("%-15d", i);
            for(int j = 0; j < x.length; j++) {
                System.out.printf("%-15.4f", x[j]);
            }
            if(currDiff != 0) {
                System.out.printf("%-15.4f", (lastDiff - currDiff));
            }
            System.out.printf("\n");
            x = GaussSeidel(x, a, b);
            lastDiff = currDiff;
            currDiff = convergenceTest(x);
        }
    }
}