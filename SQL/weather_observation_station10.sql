/*
** Query distinct cities not ending with vowels
*/

SELECT DISTINCT CITY FROM STATION WHERE CITY RLIKE '(?<![aeiou])$';
