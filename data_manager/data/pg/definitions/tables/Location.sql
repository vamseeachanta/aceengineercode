CREATE TABLE dbo.Location
(
	LocationId BIGINT      IDENTITY(1,1)    NOT NULL,
    Latitude               FLOAT       NULL,
    Longitude              FLOAT        NULL,
    Location               VARCHAR (100)    NOT NULL,
    BusinessArea           VARCHAR (100)    NULL,

    CreatedDateTime      DATETIME2       NOT NULL CONSTRAINT DF_Location_CreatedDateTime DEFAULT(SYSDATETIME()),
    CreatedBy            VARCHAR (30)    NULL,
    LastModifiedDateTime DATETIME2       NOT NULL CONSTRAINT DF_Location_LastModifiedDateTime DEFAULT(SYSDATETIME()),
    LastModifiedBy       VARCHAR (30)    NULL,
    DeletedAt            DATETIME2       NULL,

    CONSTRAINT PK_Location PRIMARY KEY CLUSTERED (Location)
);
