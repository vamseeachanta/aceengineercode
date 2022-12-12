CREATE TABLE XOM.FFTAnalysis
(
	FFTAnalysisId BIGINT     IDENTITY(1,1)     NOT NULL,
    RiserId                      BIGINT          NOT NULL,
    SchemaName                   VARCHAR (10)    NOT NULL,
    TableName                    VARCHAR (50)    NOT NULL,
    ColumnName                   VARCHAR (50)    NOT NULL,
    ColumnDataType               VARCHAR (50)    NOT NULL,
    StartTime                    DATETIME2       NULL,
    EndTime                      DATETIME2       NULL,
    RMSUnfiltered                FLOAT           NULL,
    RMSFiltered                  FLOAT           NULL,
    FFTUnfiltered                VARCHAR (1000)           NULL,
    FFTFiltered                  VARCHAR (1000)           NULL,
    FFTAverage                   VARCHAR (1000)           NULL,
    FrequenciesOfInterest        VARCHAR (1000)           NULL,

    CreatedDateTime      DATETIME2       NOT NULL CONSTRAINT DF_FFTAnalysis_CreatedDateTime DEFAULT(SYSDATETIME()),
    CreatedBy            VARCHAR (30)    NULL,
    LastModifiedDateTime DATETIME2       NOT NULL CONSTRAINT DF_FFTAnalysis_LastModifiedDateTime DEFAULT(SYSDATETIME()),
    LastModifiedBy       VARCHAR (30)    NULL,
    DeletedAt            DATETIME2       NULL,

    CONSTRAINT PK_FFTAnalysis PRIMARY KEY CLUSTERED (FFTAnalysisId, RiserId, SchemaName, TableName, ColumnName),
    CONSTRAINT FK_FFTAnalysis_RiserId FOREIGN KEY(RiserId) REFERENCES XOM.Risers (RiserId),
);
