# Write your MySQL query statement below

select w1.id
from weather w1
join weather w2
ON w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)
where w1.temperature > w2.temperature;