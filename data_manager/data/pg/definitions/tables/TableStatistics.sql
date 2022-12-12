CREATE TABLE XOM.TableStatistics
(
	TableStatisticsId BIGINT     IDENTITY(1,1)     NOT NULL,
    RiserId                      BIGINT          NOT NULL,
    SchemaName                   VARCHAR (10)    NOT NULL,
    TableName                    VARCHAR (50)    NOT NULL,
    ColumnName                   VARCHAR (50)    NOT NULL,
    ColumnDataType               VARCHAR (50)    NOT NULL,
    StatisticsClassId            BIGINT          NOT NULL,
    StartTime                    DATETIME2       NULL,
    EndTime                      DATETIME2       NULL,
    TableRows                    FLOAT           NOT NULL,
    Minimum                      VARCHAR (50)    NULL,
    Maximum                      VARCHAR (50)    NULL,
    Average                      VARCHAR (50)    NULL,
    RMS                          VARCHAR (50)    NULL,
    StandardDeviation            VARCHAR (50)    NULL,

    CreatedDateTime      DATETIME2       NOT NULL CONSTRAINT DF_TableStatistics_CreatedDateTime DEFAULT(SYSDATETIME()),
    CreatedBy            VARCHAR (30)    NULL,
    LastModifiedDateTime DATETIME2       NOT NULL CONSTRAINT DF_TableStatistics_LastModifiedDateTime DEFAULT(SYSDATETIME()),
    LastModifiedBy       VARCHAR (30)    NULL,
    DeletedAt            DATETIME2       NULL,

    CONSTRAINT PK_TableStatistics PRIMARY KEY CLUSTERED (TableStatisticsId, RiserId, SchemaName, TableName, ColumnName),
    CONSTRAINT FK_TableStatistics_RiserId FOREIGN KEY(RiserId) REFERENCES XOM.Risers (RiserId),
    CONSTRAINT FK_TableStatistics_StatisticsClassId FOREIGN KEY(StatisticsClassId) REFERENCES XOM.StatisticsClass (StatisticsClassId)
);
