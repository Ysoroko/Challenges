/*
** Query distinct cities not starting with a vowel
*/

SELECT DISTINCT CITY FROM STATION WHERE CITY RLIKE '^(?![aeiou])';
