CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
        SELECT 
          salary
        FROM
          (SELECT salary, DENSE_RANK() OVER(ORDER BY salary DESC) as salaryRank FROM Employee) as rankedEmployee
        WHERE 
          salaryRank = N
        LIMIT 1
  );
END