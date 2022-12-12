CREATE TABLE dbo.ApplicationRuns
(
	ApplicationRunsId BIGINT      IDENTITY(1,1)    NOT NULL,
    ApplicationId                 BIGINT    NOT NULL,
    ProjectId                     BIGINT    NOT NULL,
    RunName                       VARCHAR (20)    NOT NULL,
    RunStatus                     BIT       NOT NULL CONSTRAINT DF_ApplicationRuns_RunStatus  DEFAULT ((0)),
    DefaultInputFile              VARCHAR (500)    NULL,
    CustomInputFile               VARCHAR (500)    NULL,
    CustomInputs                  VARCHAR (MAX)    NULL,
    AnalysisTime                  DATETIME2         NULL,
    RunTimeInSeconds              FLOAT             NULL,

    CreatedDateTime        DATETIME2       NOT NULL CONSTRAINT DF_ApplicationRuns_CreatedDateTime DEFAULT(SYSDATETIME()),
    CreatedBy              VARCHAR (30)    NOT NULL CONSTRAINT DF_ApplicationRuns_CreatedBy  DEFAULT ('AceEngineer'),
    LastModifiedDateTime   DATETIME2       NOT NULL CONSTRAINT DF_ApplicationRuns_LastModifiedDateTime DEFAULT(SYSDATETIME()),
    LastModifiedBy         VARCHAR (30)    NOT NULL CONSTRAINT DF_ApplicationRuns_LastModifiedBy  DEFAULT ('AceEngineer'),
    DeletedAt              DATETIME2       NULL,


    CONSTRAINT [PK_ApplicationRuns] PRIMARY KEY CLUSTERED ([ApplicationRunsId] DESC),
    CONSTRAINT [FK_ApplicationRuns_Application] FOREIGN KEY ([ApplicationId]) REFERENCES [dbo].[Application] ([ApplicationId]),
    CONSTRAINT [FK_ApplicationRuns_Project] FOREIGN KEY ([ProjectId]) REFERENCES [dbo].[Project] ([ProjectId])

);
