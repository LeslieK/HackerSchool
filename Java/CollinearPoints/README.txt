Collinear Points Problem (Algorithms I, Princeton, Spring 2013)
I wrote all the code except code indicated as "DO NOT MODIFY".

Problem Statement:
Given N points, (x, y), find 4 or more collinear points.
The collinear points should be listed in increasing natural order
and should only be listed once.
**The challenge is how to remove duplicate groups of collinear points.**

The brute force approach is N^4 complexity. (java Brute "input50.txt")
Write a program to solve this with N^2 log N complexity.

Points p0, p1, and p2 are collinear if the slope from p0 to p1 
is the same as the slope from p0 to p2.
if p0.slopeTo(p1) == p0.slopeTo(p2) then p0, p1, p2 are collinear.

My solution:
For each reference point, I sort the points in SLOPE_ORDER.
N points x N log N (merge sort) = N^2 log N complexity.

1. choose reference point in natural order, p0 **This is the key to removing dups**
2. find 3 or more collinear points with respect to p0
3. if any of the collinear points is less than p0 then collinear points are duplicates
4. continue searching for more collinear points with respect to p0
5. repeat with next reference point

Compilation: javac Fast.java
Execution: java Fast "input50.txt"

Brute.java: brute force implemenation (dependency: Point.java)
Fast.java: fast implementation        (dependency: Point.java)
Point.java: Point class; defines Comparator<Point> SLOPE_ORDER





