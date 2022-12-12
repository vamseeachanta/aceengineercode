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
	SMYS float not null,
	SMUS float null,
	reference  varchar(500) not null,
	PRIMARY KEY (grade_name),
	FOREIGN KEY (material_id) REFERENCES material (material_id)
	);


create function calculate_code_id() returns trigger as $$
begin
	if NEW.inside_diameter is null then
		NEW.inside_diameter := (NEW.outer_diameter - (NEW.wall_thickness * 2 /1000) );
	end if;
	return new;
end;
$$ language plpgsql;

create trigger trig_insert_pipe_metrics_insidediameter
before insert
on pipe_metrics
for each row
execute procedure calculate_inside_diameter();

