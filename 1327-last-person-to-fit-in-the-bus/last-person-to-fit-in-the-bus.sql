# Write your MySQL query statement below
with cte as(
    select *,
    sum(weight)OVER(ORDER BY turn ) as rt
    from Queue
)

select person_name
from cte
where rt<=1000
order by rt desc
limit 1