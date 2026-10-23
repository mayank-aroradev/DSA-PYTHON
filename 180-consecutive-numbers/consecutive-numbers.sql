# Write your MySQL query statement below

with Rankedlogs as(
    select num,
        lead(num,1) over (order by id) as nextnum,
        lead(num,2) over (order by id) as next_nextnum
    from logs
)
select distinct num as ConsecutiveNums 
from Rankedlogs 
where num=nextnum and nextnum=next_nextnum