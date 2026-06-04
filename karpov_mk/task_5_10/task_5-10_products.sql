-- 1
select
	*
from
	products;

-- 2
select
	name,
	category
from
	products;

-- 3
select
	distinct category
from
	products;

-- 4 
select
	*
from
	products
order by
	name asc;

-- 5
select
	*
from
	products
order by
	name desc;

-- 6
select
	*
from
	products
limit 10;

-- 7
select
	*
from
	products
limit 10 offset 10;

-- 8
select
	*
from
	products
order by
	RANDOM()
limit 5;

-- 9 
select
	category
from
	products
order by
	category asc;

-- 10
select
	*
from
	products
order by
	category asc,
	name asc;