select
	product_id,
	COUNT(*) as suppliers_count
from
	suppliers
group by
	product_id;