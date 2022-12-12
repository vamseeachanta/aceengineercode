CREATE EXTENSION hstore;

drop table if exists location;
drop type if exists loading_type;
drop table if exists reference_codes;
drop table if exists applications;

create table location(
	location_id serial not null,
	latitude float null,
	longitude float null,
	description varchar(100) null,
	business_area varchar(100) null,
	PRIMARY KEY (latitude, longitude)
);

create type loading_type as enum ('Extreme','long-term');

create table reference_codes(
	ref_code_id serial not null,
	UNIQUE (ref_code_id),

	ref_code varchar(50) not null,
	release_year SMALLINT not null,
	release_date DATE null,

	PRIMARY KEY (ref_code, release_date)
	);

create table applications(
	applications_id serial not null,
	UNIQUE (applications_id),

	app_name varchar(50) not null,
	description varchar(1000) not null,
	release_version float not null,
	release_date DATE not null,
    default_inputs jsonb not null,

	PRIMARY KEY (app_name , release_version)
	);

