-- 1
select
	category,
	COUNT(*) as total_products
from
	products
group by
	category;

-- 2
select
	category,
	COUNT(*) as total_products
from
	products
group by
	category
order by
	total_products desc;