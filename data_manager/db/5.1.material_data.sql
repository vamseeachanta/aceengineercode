drop table if exists material;
drop table if exists material_grades;

create table material(
	material_id serial not null,
	material_name varchar(50) not null,
	E float not null,
	density float not null,
	poissonsratio float not null,
	thermal_expansion_coefficient float not null,
	UNIQUE (material_id),
	PRIMARY KEY (material_name)
	);

create table material_grades(
	grade_id serial not null,
	grade_name varchar(50) not null,
	material_id integer not null,
	YS_minimum float not null,
	US_minimum float not null,
	YS_maximum float null,
	US_maximum float null,
	elongtation_2in_minimum float null,
	code_id  varchar(500) null,
	reference  varchar(500) null,
	PRIMARY KEY (grade_name),
	FOREIGN KEY (material_id) REFERENCES material (material_id)
	);

insert into material (material_name, E, density, poissonsratio, thermal_expansion_coefficient) values ('steel-generic', 30000000, 0.2817929, 0.30, 6.5E-6);

insert into material_grades (grade_name, material_id, YS_minimum, US_minimum, YS_maximum, US_maximum, elongtation_2in_minimum, code_id, reference) values ('ASTM A106 Grade A', 1, 30000, 48000, '', '', '', 'https://www.amerpipe.com/steel-pipe-products/carbon-pipe/a106/a106-specifications/');
insert into material_grades (grade_name, material_id, YS_minimum, US_minimum, YS_maximum, US_maximum, elongtation_2in_minimum, code_id, reference) values ('ASTM A106 Grade B', 1, 35000, 60000, '', '', '', 'https://www.amerpipe.com/steel-pipe-products/carbon-pipe/a106/a106-specifications/');
insert into material_grades (grade_name, material_id, YS_minimum, US_minimum, YS_maximum, US_maximum, elongtation_2in_minimum, code_id, reference) values ('ASTM A106 Grade C', 1, 40000, 70000, '', '', '', 'https://www.amerpipe.com/steel-pipe-products/carbon-pipe/a106/a106-specifications/');
insert into material_grades (grade_name, material_id, YS_minimum, US_minimum, YS_maximum, US_maximum, elongtation_2in_minimum, code_id, reference) values ('API 5L X60 PSL1', 1, 60000,  75000, '', '', '', 'API 5L 2004');
insert into material_grades (grade_name, material_id, YS_minimum, US_minimum, YS_maximum, US_maximum, elongtation_2in_minimum, code_id, reference) values ('API 5L X60 PSL2', 1, 60000,  82000, 75000, 110000, '', 'API 5L 2004');
insert into material_grades (grade_name, material_id, YS_minimum, US_minimum, YS_maximum, US_maximum, elongtation_2in_minimum, code_id, reference) values ('API 5L X70 PSL1', 1, 70000,  82000, '', '', '', 'API 5L 2004');
insert into material_grades (grade_name, material_id, YS_minimum, US_minimum, YS_maximum, US_maximum, elongtation_2in_minimum, code_id, reference) values ('API 5L X70 PSL1', 1, 70000,  82000, '', '', '', 'API 5L 2004');
insert into material_grades (grade_name, material_id, YS_minimum, US_minimum, YS_maximum, US_maximum, elongtation_2in_minimum, code_id, reference) values ('API 5L X65 PSL1', 1, 65000,  77000, '', '', '', 'API 5L 2004');
insert into material_grades (grade_name, material_id, YS_minimum, US_minimum, YS_maximum, US_maximum, elongtation_2in_minimum, code_id, reference) values ('API 5L X80 PSL2', 1, 80000,  100000, 90000, 120000, '', 'API 5L 2004');
insert into material_grades (grade_name, material_id, YS_minimum, US_minimum, YS_maximum, US_maximum, elongtation_2in_minimum, code_id, reference) values ('P110', 1, 110000,  125000, '', '', '', 'Assumed');
insert into material_grades (grade_name, material_id, YS_minimum, US_minimum, YS_maximum, US_maximum, elongtation_2in_minimum, code_id, reference) values ('S125', 1, 125000,  140000, '', '', '', 'Assumed');
