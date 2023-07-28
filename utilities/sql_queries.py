generation_table = "`rahman-portfolio.pokedex.pokemon_generations`"
pokemon_metaata_table = "`rahman-portfolio.pokedex.pokemon_base_metadata`"


pokemon_by_generations = """
SELECT
  pg.generation_name,
  count(pm.pokemon_id)
FROM """+generation_table+"""  as pg
left join """+pokemon_metaata_table+""" as pm
  on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
group by 
  pg.generation_name
order by
  pg.generation_name 
"""

generation_average_stats = """
SELECT
  pg.generation_name,
  round(avg(pm.pokemon_height),3) as avg_ht,
  round(avg(pm.pokemon_weight),3) as avg_wt,
  round(avg(pokemon_base_hp),3) as avg_hp,
  round(avg(pm.pokemon_base_attack),3) as avg_atk,
  round(avg(pm.pokemon_base_defence),3) as avg_def,
  round(avg(pm.pokemon_base_special_attack),3) as avg_sp_atk,
  round(avg(pm.pokemon_base_special_defence),3) as avg_sp_def
FROM """+generation_table+"""  as pg
left join """+pokemon_metaata_table+""" as pm
  on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
group by 
  pg.generation_name
order by
  pg.generation_name;
"""

weights_check = """
select
    pg.generation_name,
    round(avg(pm.pokemon_weight),3) as avg_wt,
    min(pm.pokemon_weight) as min_wt,
    max(pm.pokemon_weight) as max_wt
FROM """+generation_table+"""  as pg
left join """+pokemon_metaata_table+""" as pm
  on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
group by
    pg.generation_name
order by
    pg.generation_name
"""

whats_up_gen_seven = """
select
pm.pokemon_name,
pm.pokemon_weight
FROM """+generation_table+"""  as pg
left join """+pokemon_metaata_table+""" as pm
  on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
where pg.generation_name = 'Generation 7'
and pm.pokemon_weight = 9999
"""

generation_weight_distros="""
with all_weights as
(
  select distinct
  pokemon_weight
  from `rahman-portfolio.pokedex.pokemon_base_metadata`
),
gen1 as
(
  SELECT
    pm.pokemon_weight,
    count(pm.pokemon_id) as num_pokemon
  FROM `rahman-portfolio.pokedex.pokemon_generations`  as pg
  inner join `rahman-portfolio.pokedex.pokemon_base_metadata` as pm
    on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
  where pg.generation_name = 'Generation 1'
  group by 
    pm.pokemon_weight
  order by
    pm.pokemon_weight asc
),
gen2 as
(
  SELECT
    pm.pokemon_weight,
    count(pm.pokemon_id) as num_pokemon
  FROM `rahman-portfolio.pokedex.pokemon_generations`  as pg
  inner join `rahman-portfolio.pokedex.pokemon_base_metadata` as pm
    on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
  where pg.generation_name = 'Generation 2'
  group by 
    pm.pokemon_weight
  order by
    pm.pokemon_weight asc
),
gen3 as
(
  SELECT
    pm.pokemon_weight,
    count(pm.pokemon_id) as num_pokemon
  FROM `rahman-portfolio.pokedex.pokemon_generations`  as pg
  inner join `rahman-portfolio.pokedex.pokemon_base_metadata` as pm
    on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
  where pg.generation_name = 'Generation 3'
  group by 
    pm.pokemon_weight
  order by
    pm.pokemon_weight asc
),
gen4 as
(
  SELECT
    pm.pokemon_weight,
    count(pm.pokemon_id) as num_pokemon
  FROM `rahman-portfolio.pokedex.pokemon_generations`  as pg
  inner join `rahman-portfolio.pokedex.pokemon_base_metadata` as pm
    on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
  where pg.generation_name = 'Generation 4'
  group by 
    pm.pokemon_weight
  order by
    pm.pokemon_weight asc
),
gen5 as
(
  SELECT
    pm.pokemon_weight,
    count(pm.pokemon_id) as num_pokemon
  FROM `rahman-portfolio.pokedex.pokemon_generations`  as pg
  inner join `rahman-portfolio.pokedex.pokemon_base_metadata` as pm
    on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
  where pg.generation_name = 'Generation 5'
  group by 
    pm.pokemon_weight
  order by
    pm.pokemon_weight asc
),
gen6 as
(
  SELECT
    pm.pokemon_weight,
    count(pm.pokemon_id) as num_pokemon
  FROM `rahman-portfolio.pokedex.pokemon_generations`  as pg
  inner join `rahman-portfolio.pokedex.pokemon_base_metadata` as pm
    on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
  where pg.generation_name = 'Generation 6'
  group by 
    pm.pokemon_weight
  order by
    pm.pokemon_weight asc
),
gen7 as
(
  SELECT
    pm.pokemon_weight,
    count(pm.pokemon_id) as num_pokemon
  FROM `rahman-portfolio.pokedex.pokemon_generations`  as pg
  inner join `rahman-portfolio.pokedex.pokemon_base_metadata` as pm
    on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
  where pg.generation_name = 'Generation 7'
  group by 
    pm.pokemon_weight
  order by
    pm.pokemon_weight asc
),
gen8 as
(
  SELECT
    pm.pokemon_weight,
    count(pm.pokemon_id) as num_pokemon
  FROM `rahman-portfolio.pokedex.pokemon_generations`  as pg
  inner join `rahman-portfolio.pokedex.pokemon_base_metadata` as pm
    on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
  where pg.generation_name = 'Generation 8'
  group by 
    pm.pokemon_weight
  order by
    pm.pokemon_weight asc
),
gen9 as
(
  SELECT
    pm.pokemon_weight,
    count(pm.pokemon_id) as num_pokemon
  FROM `rahman-portfolio.pokedex.pokemon_generations`  as pg
  inner join `rahman-portfolio.pokedex.pokemon_base_metadata` as pm
    on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
  where pg.generation_name = 'Generation 9'
  group by 
    pm.pokemon_weight
  order by
    pm.pokemon_weight asc
),
combined as
(
  select
    aw.pokemon_weight,
    case when g1.num_pokemon is null then 0 else g1.num_pokemon end as num_gen_1,
    case when g2.num_pokemon is null then 0 else g2.num_pokemon end as num_gen_2,
    case when g3.num_pokemon is null then 0 else g3.num_pokemon end as num_gen_3,
    case when g4.num_pokemon is null then 0 else g4.num_pokemon end as num_gen_4,
    case when g5.num_pokemon is null then 0 else g5.num_pokemon end as num_gen_5,
    case when g6.num_pokemon is null then 0 else g6.num_pokemon end as num_gen_6,
    case when g7.num_pokemon is null then 0 else g7.num_pokemon end as num_gen_7,
    case when g8.num_pokemon is null then 0 else g8.num_pokemon end as num_gen_8,
    case when g9.num_pokemon is null then 0 else g9.num_pokemon end as num_gen_9
  from all_weights aw
  left join gen1 g1
    on g1.pokemon_weight = aw.pokemon_weight
  left join gen2 g2
    on g2.pokemon_weight = aw.pokemon_weight
  left join gen3 g3
    on g3.pokemon_weight = aw.pokemon_weight
  left join gen4 g4
    on g4.pokemon_weight = aw.pokemon_weight
  left join gen5 g5
    on g5.pokemon_weight = aw.pokemon_weight
  left join gen6 g6
    on g6.pokemon_weight = aw.pokemon_weight
  left join gen7 g7
    on g7.pokemon_weight = aw.pokemon_weight
  left join gen8 g8
    on g8.pokemon_weight = aw.pokemon_weight
  left join gen9 g9
    on g9.pokemon_weight = aw.pokemon_weight
)
select
*
from combined
order by
    pokemon_weight asc
"""

def generation_weight_data(generation_string):
    query = """
    SELECT
    pm.pokemon_weight
  FROM `rahman-portfolio.pokedex.pokemon_generations`  as pg
  inner join `rahman-portfolio.pokedex.pokemon_base_metadata` as pm
    on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
  where pg.generation_name = '"""+generation_string+"""'"""

    return query

heights_check = """
select
    pg.generation_name,
    round(avg(pm.pokemon_height),3) as avg_ht,
    min(pm.pokemon_height) as min_ht,
    max(pm.pokemon_height) as max_ht
FROM """+generation_table+"""  as pg
left join """+pokemon_metaata_table+""" as pm
  on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
group by
    pg.generation_name
order by
    pg.generation_name
"""

generation_height_distros="""
with all_heights as
(
  select distinct
  pokemon_height
  from `rahman-portfolio.pokedex.pokemon_base_metadata`
),
gen1 as
(
  SELECT
    pm.pokemon_height,
    count(pm.pokemon_id) as num_pokemon
  FROM `rahman-portfolio.pokedex.pokemon_generations`  as pg
  inner join `rahman-portfolio.pokedex.pokemon_base_metadata` as pm
    on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
  where pg.generation_name = 'Generation 1'
  group by 
    pm.pokemon_height
  order by
    pm.pokemon_height asc
),
gen2 as
(
  SELECT
    pm.pokemon_height,
    count(pm.pokemon_id) as num_pokemon
  FROM `rahman-portfolio.pokedex.pokemon_generations`  as pg
  inner join `rahman-portfolio.pokedex.pokemon_base_metadata` as pm
    on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
  where pg.generation_name = 'Generation 2'
  group by 
    pm.pokemon_height
  order by
    pm.pokemon_height asc
),
gen3 as
(
  SELECT
    pm.pokemon_height,
    count(pm.pokemon_id) as num_pokemon
  FROM `rahman-portfolio.pokedex.pokemon_generations`  as pg
  inner join `rahman-portfolio.pokedex.pokemon_base_metadata` as pm
    on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
  where pg.generation_name = 'Generation 3'
  group by 
    pm.pokemon_height
  order by
    pm.pokemon_height asc
),
gen4 as
(
  SELECT
    pm.pokemon_height,
    count(pm.pokemon_id) as num_pokemon
  FROM `rahman-portfolio.pokedex.pokemon_generations`  as pg
  inner join `rahman-portfolio.pokedex.pokemon_base_metadata` as pm
    on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
  where pg.generation_name = 'Generation 4'
  group by 
    pm.pokemon_height
  order by
    pm.pokemon_height asc
),
gen5 as
(
  SELECT
    pm.pokemon_height,
    count(pm.pokemon_id) as num_pokemon
  FROM `rahman-portfolio.pokedex.pokemon_generations`  as pg
  inner join `rahman-portfolio.pokedex.pokemon_base_metadata` as pm
    on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
  where pg.generation_name = 'Generation 5'
  group by 
    pm.pokemon_height
  order by
    pm.pokemon_height asc
),
gen6 as
(
  SELECT
    pm.pokemon_height,
    count(pm.pokemon_id) as num_pokemon
  FROM `rahman-portfolio.pokedex.pokemon_generations`  as pg
  inner join `rahman-portfolio.pokedex.pokemon_base_metadata` as pm
    on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
  where pg.generation_name = 'Generation 6'
  group by 
    pm.pokemon_height
  order by
    pm.pokemon_height asc
),
gen7 as
(
  SELECT
    pm.pokemon_height,
    count(pm.pokemon_id) as num_pokemon
  FROM `rahman-portfolio.pokedex.pokemon_generations`  as pg
  inner join `rahman-portfolio.pokedex.pokemon_base_metadata` as pm
    on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
  where pg.generation_name = 'Generation 7'
  group by 
    pm.pokemon_height
  order by
    pm.pokemon_height asc
),
gen8 as
(
  SELECT
    pm.pokemon_height,
    count(pm.pokemon_id) as num_pokemon
  FROM `rahman-portfolio.pokedex.pokemon_generations`  as pg
  inner join `rahman-portfolio.pokedex.pokemon_base_metadata` as pm
    on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
  where pg.generation_name = 'Generation 8'
  group by 
    pm.pokemon_height
  order by
    pm.pokemon_height asc
),
gen9 as
(
  SELECT
    pm.pokemon_height,
    count(pm.pokemon_id) as num_pokemon
  FROM `rahman-portfolio.pokedex.pokemon_generations`  as pg
  inner join `rahman-portfolio.pokedex.pokemon_base_metadata` as pm
    on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
  where pg.generation_name = 'Generation 9'
  group by 
    pm.pokemon_height
  order by
    pm.pokemon_height asc
),
combined as
(
  select
    aw.pokemon_height,
    case when g1.num_pokemon is null then 0 else g1.num_pokemon end as num_gen_1,
    case when g2.num_pokemon is null then 0 else g2.num_pokemon end as num_gen_2,
    case when g3.num_pokemon is null then 0 else g3.num_pokemon end as num_gen_3,
    case when g4.num_pokemon is null then 0 else g4.num_pokemon end as num_gen_4,
    case when g5.num_pokemon is null then 0 else g5.num_pokemon end as num_gen_5,
    case when g6.num_pokemon is null then 0 else g6.num_pokemon end as num_gen_6,
    case when g7.num_pokemon is null then 0 else g7.num_pokemon end as num_gen_7,
    case when g8.num_pokemon is null then 0 else g8.num_pokemon end as num_gen_8,
    case when g9.num_pokemon is null then 0 else g9.num_pokemon end as num_gen_9
  from all_heights aw
  left join gen1 g1
    on g1.pokemon_height = aw.pokemon_height
  left join gen2 g2
    on g2.pokemon_height = aw.pokemon_height
  left join gen3 g3
    on g3.pokemon_height = aw.pokemon_height
  left join gen4 g4
    on g4.pokemon_height = aw.pokemon_height
  left join gen5 g5
    on g5.pokemon_height = aw.pokemon_height
  left join gen6 g6
    on g6.pokemon_height = aw.pokemon_height
  left join gen7 g7
    on g7.pokemon_height = aw.pokemon_height
  left join gen8 g8
    on g8.pokemon_height = aw.pokemon_height
  left join gen9 g9
    on g9.pokemon_height = aw.pokemon_height
)
select
*
from combined
order by
    pokemon_height asc
"""

def generation_height_data(generation_string):
    query = """
    SELECT
    pm.pokemon_height
  FROM `rahman-portfolio.pokedex.pokemon_generations`  as pg
  inner join `rahman-portfolio.pokedex.pokemon_base_metadata` as pm
    on pm.pokemon_id between pg.start_pokemon_num and pg.ending_pokemon_num
  where pg.generation_name = '"""+generation_string+"""'"""

    return query