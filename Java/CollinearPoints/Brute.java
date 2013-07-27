/*************************************************************************
 * Name: Leslie B. Klein
 * Email: leslieklein@comcast.net
 *
 * Compilation:  javac Brute.java
 * Execution: java filename
 * Dependencies: StdDraw.java, Point.java
 *
 * Description: Finds 4 coolinear points, draws and prints them out. 
 * N^4 complexity.
 *
 *************************************************************************/
public class Brute {
    
    private static boolean isCollinear(Point p, Point q, Point r) {
            double pq = p.slopeTo(q);
            double pr = p.slopeTo(r);
            return (pq == pr);    
    }
    
    private static boolean isCollinear(Point p, Point q, Point r, Point s) {
        double pq = p.slopeTo(q);
        double pr = p.slopeTo(r);
        double ps = p.slopeTo(s);
        if (pq == pr && pq == ps) return true;
        return false;
    }
    
    public static void main(String[] args) {
        
        // rescale coordinates and turn on animation mode
        StdDraw.setXscale(0, 32768);
        StdDraw.setYscale(0, 32768);
        StdDraw.show(0);
        
        // read in number of points, N
        String filename = args[0];
        In in = new In(filename);      // input file
        int N = in.readInt();          // number of points
        Point[] a = new Point[N];      // array of Points
        
        for (int i = 0; i < N; i++) {
            int x = in.readInt();
            int y = in.readInt();
            a[i] = new Point(x, y);
            a[i].draw();
        }
    
        for (int p = 0; p < N; p++) {
            for (int q = 0; q < N; q++) {
                if (q == p) continue;
                for (int r = 0; r < N; r++) {
                    if (r == p || r == q) continue;
                    if (!isCollinear(a[p], a[q], a[r])) continue;
                    for (int s = 0; s < N; s++) {
                        if (s == p || s == q || s == r) continue;
                        if (isCollinear(a[p], a[q], a[r], a[s])) {
                           if (a[p].compareTo(a[q]) < 0 
                                   && a[q].compareTo(a[r]) < 0
                                   && a[r].compareTo(a[s]) < 0)
                                // draw line segment
                               { a[p].drawTo(a[s]); 
                                 StdOut.println(a[p] + " -> "
                                                + a[q] + " -> " 
                                                + a[r] + " -> " + a[s]);
                               } 
                        }
                    }
                }
            }
        }
        
        // display to screen all at once
        StdDraw.show(0);
        
    }
    
}
