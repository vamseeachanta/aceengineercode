CREATE TABLE XOM.Risers
(
	RiserId BIGINT      IDENTITY(1,1)    NOT NULL,
    RiserType            VARCHAR (30)       NOT NULL,
    Vessel               VARCHAR (30)       NOT NULL,

    CreatedDateTime      DATETIME2       NOT NULL CONSTRAINT DF_Risers_CreatedDateTime DEFAULT(SYSDATETIME()),
    CreatedBy            VARCHAR (30)    NULL,
    LastModifiedDateTime DATETIME2       NOT NULL CONSTRAINT DF_Risers_LastModifiedDateTime DEFAULT(SYSDATETIME()),
    LastModifiedBy       VARCHAR (30)    NULL,
    DeletedAt            DATETIME2       NULL,

    CONSTRAINT PK_Risers PRIMARY KEY CLUSTERED (RiserId ASC)
);
GO

-- long-term should cross reference vessels and should have assets as general class