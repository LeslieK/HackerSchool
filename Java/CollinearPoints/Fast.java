/*************************************************************************
 * Name: Leslie B. Klein
 * Email: leslieklein@comcast.net
 *
 * Compilation:  javac Fast.java
 * Execution:
 * Dependencies: StdDraw.java, Point.java
 *
 * Description: Finds 4 or more coolinear points, draws and prints them out. 
 * N^2 log N complexity.
 *
 *************************************************************************/
import java.util.Arrays;

public class Fast {
    
    private static boolean isDuplicate(Point[] collinear, Point apoint) {
        for (int w = 0; w < collinear.length; w++) {
           if (collinear[w].compareTo(apoint) < 0) 
               return true; 
        }
        return false;
    }
        
    public static void main(String[] args) {
        
        // rescale coordinates and turn on animation mode
        //StdDraw.setXscale(0, 32768);
        //StdDraw.setYscale(0, 32768);
        //StdDraw.show(0);
        
        // read in number of points, N
        String filename = args[0];
        In in = new In(filename);      // input file
        int N = in.readInt();          // number of points
        Point[] a = new Point[N];      // array of Points
        Point[] aux = new Point[N];    // used for sorting
        
        for (int i = 0; i < N; i++) {
            int x = in.readInt();
            int y = in.readInt();
            a[i] = new Point(x, y);
            //a[i].draw();
        }
        // sort in natural order; needed to get rid of permutations
        Arrays.sort(a);
        
        // copy a[] to aux[] to preserve original order
        for (int i = 0; i < N; i++) {
            aux[i] = a[i];
        }
        
        for (int i = 0; i < N; i++) {
            Point p = a[i];
            Arrays.sort(aux, 0, a.length, p.SLOPE_ORDER);

            // check for runs of at least 3
            int runlength = 1;
            int lo = 0;
            int hi = 0;
            int j = 1;
            while (j < N) {
                  while (j + 1 < N && p.slopeTo(aux[j]) == p.slopeTo(aux[j+1])) 
                  {
                       runlength++; 
                       j++;
                  }

                    if (runlength > 2) {
                        lo = j - runlength + 1;
                        hi = j;
                        
                        // create array to store collinear points
                        Point[] collinear = new Point[runlength + 1];
                        // include p
                        collinear[0] = aux[0];
                        int c = 1;
                        // include points collinear with p
                        for (int w = lo; w < hi + 1; w++) {
                            collinear[c] = aux[w];
                            c++;
                        }

                        // check for duplicates
                        if (isDuplicate(collinear, aux[0])) {
                            runlength = 1;
                            continue;
                        }
                         
                        // draw lines
                        Arrays.sort(collinear, 0, collinear.length);
                        //collinear[0].drawTo(collinear[collinear.length - 1]);
                        //StdDraw.show(0);
                        
                        // per line: print out points on line
                        for (int w = 0; w < collinear.length - 1; w++) {
                            StdOut.print(collinear[w] + " -> ");
                        }
                        StdOut.println(collinear[collinear.length-1]);
                    }
                    runlength = 1;
                    j++;
                }
                
            }
        }  
    }
