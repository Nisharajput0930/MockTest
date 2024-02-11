use demo;

-- Write a sql query to retrieve the top 3 highest-mark_achiever students from the a table, along with their marks.

SELECT st_id, stu_name, marks_achieved
FROM stud
ORDER BY marks_achieved DESC
LIMIT 3;

--  Divide a student table having their marks into 4 equal marks groups (quartiles) and show their details.

SELECT stu_name, marks_achieved,
NTILE(4) OVER (ORDER BY marks_achieved) AS quartile
FROM stud;