/*************************************************************************
 * Name: Leslie B. Klein
 * Email: leslieklein@comcast.net
 *
 * Compilation:  javac Point.java
 * Execution:
 * Dependencies: StdDraw.java
 *
 * Description: An immutable data type for points in the plane.
 *
 *************************************************************************/

import java.util.Comparator;

public class Point implements Comparable<Point> {

    // compare points by slope
    public final Comparator<Point> SLOPE_ORDER = new SlopeOrder();       

    private final int x;                              // x coordinate
    private final int y;                              // y coordinate

    // create the point (x, y)
    public Point(int x, int y) {
        /* DO NOT MODIFY */
        this.x = x;
        this.y = y;
    }
    
    // Comparator<Point> class
    private class SlopeOrder implements Comparator<Point>
    {
        public int compare(Point p1, Point p2) 
        {
            double m1 = new Point(x, y).slopeTo(p1);
            double m2 = new Point(x, y).slopeTo(p2);
            return new Double(m1).compareTo(new Double(m2));
        }
    }

    // plot this point to standard drawing
    public void draw() {
        /* DO NOT MODIFY */
        StdDraw.point(x, y);
    }

    // draw line between this point and that point to standard drawing
    public void drawTo(Point that) {
        /* DO NOT MODIFY */
        StdDraw.line(this.x, this.y, that.x, that.y);
    }

    // slope between this point and that point
    public double slopeTo(Point that) {
        /* YOUR CODE HERE */
        int dy = this.y - that.y;
        int dx = this.x - that.x;
        
        if (this.y == that.y 
                && this.x == that.x) 
            return Double.NEGATIVE_INFINITY;   // degenerate points
        if (this.x == that.x) 
            return Double.POSITIVE_INFINITY;   // vertical 
        if (this.y == that.y) { 
            return 0.0;                        // horizontal
        }
        return (dy / (double) dx);
    }

    // is this point lexicographically smaller than that one?
    // comparing y-coordinates and breaking ties by x-coordinates
    public int compareTo(Point that) {
        /* YOUR CODE HERE */
   if (this.y < that.y || (this.y == that.y && this.x < that.x)) return -1;
   else if (this.y > that.y || (this.y == that.y && this.x > that.x)) return 1;
   else return 0;
   }

    // return string representation of this point
    public String toString() {
        /* DO NOT MODIFY */
        return "(" + x + ", " + y + ")";
    }
    
    

    // unit test
    public static void main(String[] args) {
        
        // rescale coordinates and turn on animation mode
        StdDraw.setXscale(0, 32768);
        StdDraw.setYscale(0, 32768);
        StdDraw.show(0);
        
        // read in number of points, N
//        String filename = args[0];
//        In in = new In(filename);      // input file
//        int N = in.readInt();          // number of points
//        Point[] a = new Point[N];      // array of Points
        
        int N = StdIn.readInt();
        Point[] a = new Point[N];
        
        for (int i = 0; i < N; i++) {
//            int x = in.readInt();
//            int y = in.readInt();
            int x = StdIn.readInt();
            int y = StdIn.readInt();
            a[i] = new Point(x, y);
//            a[i].draw();
        }
        
        StdOut.println(a[0] + " " + a[1] + " " + a[0].compareTo(a[1]));
        
    }
}
