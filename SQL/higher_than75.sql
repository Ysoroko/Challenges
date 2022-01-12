/*
** Select names of students who have a mark higher than 75 and sort them:
** 1) by the last three characters
** 2) by their id
*/

SELECT NAME FROM STUDENTS WHERE Marks > 75 ORDER BY RIGHT(NAME, 3), ID ASC;
