CREATE TABLE digitaltiwnfeed.Vessels (
    vessel_id          serial,
    vessel_type        VARCHAR (30)  NOT NULL,
    construction_type  VARCHAR (30)  NOT NULL,
    vessel_name        VARCHAR (30)  NOT NULL,
    CONSTRAINT    pk_Vessels    PRIMARY key (vessel_id)
);

