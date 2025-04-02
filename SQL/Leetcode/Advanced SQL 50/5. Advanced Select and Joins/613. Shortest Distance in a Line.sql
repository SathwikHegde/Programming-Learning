Table: Point

+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
+-------------+------+
In SQL, x is the primary key column for this table.
Each row of this table indicates the position of a point on the X-axis.
 

Find the shortest distance between any two points from the Point table.

The result format is in the following example.

 

Example 1:

Input: 
Point table:
+----+
| x  |
+----+
| -1 |
| 0  |
| 2  |
+----+
Output: 
+----------+
| shortest |
+----------+
| 1        |
+----------+
Explanation: The shortest distance is between points -1 and 0 which is |(-1) - 0| = 1.
 

Follow up: How could you optimize your solution if the Point table is ordered in ascending order?


SQL Schema:-
Create Table If Not Exists Point (x int not null)
Truncate table Point
insert into Point (x) values ('-1')
insert into Point (x) values ('0')
insert into Point (x) values ('2')


# Write your MySQL query statement below

WITH al AS
(
SELECT 
    p1.x AS x1, 
    p2.x AS x2,
    ABS(p1.x - p2.x) AS distance
FROM point p1, point p2
WHERE p1.x!= p2.x )
SELECT 
    MIN(distance) AS shortest
FROM al 