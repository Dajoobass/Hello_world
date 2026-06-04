-- 1
select
	*
from
	prices
order by
	price desc
limit 5;

-- 2
select
	*
from
	prices
order by
	created_at desc
limit 10;

--3
select
	*
from
	prices
order by
	price asc
limit 10;

-- 4
select
	*
from
	prices
order by
	price desc 
offset 20;