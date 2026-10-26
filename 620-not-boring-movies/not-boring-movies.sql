# Write your MySQL query statement below

select id , movie , description , rating 
from Cinema

where id % 2 and description!='boring'
order by rating desc;