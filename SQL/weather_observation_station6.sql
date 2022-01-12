/*
** Select all distinct cities which start with vowels
** RLIKE allows to use a regular expression
** '^[aeiou]': starts with "a/e/i/o/u"
*/

SELECT DISTINCT CITY FROM STATION WHERE CITY RLIKE '^[aeiou]';
