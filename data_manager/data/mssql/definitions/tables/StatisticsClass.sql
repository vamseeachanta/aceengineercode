CREATE TABLE XOM.StatisticsClass
(
	StatisticsClassId BIGINT      IDENTITY(1,1)    NOT NULL,
    StatisticsClassType           VARCHAR (30)     NOT NULL,

    CreatedDateTime      DATETIME2       NOT NULL CONSTRAINT DF_StatisticsClass_CreatedDateTime DEFAULT(SYSDATETIME()),
    CreatedBy            VARCHAR (30)    NULL,
    LastModifiedDateTime DATETIME2       NOT NULL CONSTRAINT DF_StatisticsClass_LastModifiedDateTime DEFAULT(SYSDATETIME()),
    LastModifiedBy       VARCHAR (30)    NULL,
    DeletedAt            DATETIME2       NULL,

    CONSTRAINT PK_StatisticsClass PRIMARY KEY CLUSTERED (StatisticsClassId ASC)
);
GO

-- long-term should cross reference vessels and should have assets as general class