drop table if exists app_pipe_results;

create table app_pipe_results(
	result_id serial not null,
	PRIMARY KEY (result_id),

	app_id INTEGER not null,
	FOREIGN KEY (app_id) REFERENCES applications (applications_id),
    code_id INTEGER not null,
	FOREIGN KEY (code_id) REFERENCES reference_codes (ref_code_id),

    minimum_wall_thickness float not null,
    inputs jsonb not null,
    outputs jsonb not null

	);
