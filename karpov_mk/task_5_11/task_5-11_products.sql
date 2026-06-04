-- 1
select
	*
from
	products
where
	category = 'Электроника';

-- 2
select
	*
from
	products
where
	category = 'Одежда'
	and name ilike '%женск%';

-- 3
select
	*
from
	products
where
	category in ('Продукты', 'Книги');

-- 4
select
	*
from
	products
where
	category != 'Бытовая техника';

-- 5
select
	*
from
	products
where
	category in ('Электроника', 'Одежда', 'Книги');

-- 6
select
	*
from
	products
where
	(category = 'Электроника'
		and name ilike '%Samsung%')
	or category = 'Бытовая техника';

-- 7 
select
	*
from
	products
where
	(
    category in ('Электроника', 'Одежда', 'Бытовая техника')
		and id between 1 and 15
		and name not ilike '%Samsung%'
)
	or category = 'Книги';