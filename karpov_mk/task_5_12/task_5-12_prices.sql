-- 1
select
	product_id,
	COUNT(*) as prices_count
from
	prices
group by
	product_id;

-- 2
select
	product_id,
	ROUND(AVG(price), 2) as average_price
from
	prices
group by
	product_id;

-- 3.
select
	product_id,
	MIN(price) as min_price
from
	prices
group by
	product_id;

-- 4
select
	product_id,
	MAX(price) as max_price
from
	prices
group by
	product_id;