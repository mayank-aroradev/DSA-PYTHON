# Write your MySQL query statement below
SELECT id,
CASE
    when p_id IS null then 'Root'
    when id IN (SELECT p_id from Tree) then 'Inner'
    ELSE 'Leaf' 
END AS type 
from Tree
