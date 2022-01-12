/*
** Query distinct cities starting with a vowel and ending with a vowel
*/

SELECT DISTINCT CITY FROM STATION WHERE CITY RLIKE '^[aeiou]' AND CITY RLIKE '[aeiou]$';
