/*
** Select distinct cities ending with a vowel
** Regex '[aeiou]$':
** $: end of the string
** [aeiou]: any of these characters
*/

SELECT DISTINCT CITY FROM STATION WHERE CITY RLIKE '[aeiou]$';
