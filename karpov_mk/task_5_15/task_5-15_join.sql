select
	p.name as "название товара",
	pr.price as "цену"
from
	products p
join prices pr on
	p.id = pr.product_id;