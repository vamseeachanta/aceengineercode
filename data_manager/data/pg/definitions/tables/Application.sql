CREATE TABLE dbo.Application
(
	ApplicationId BIGINT      IDENTITY(1,1)    NOT NULL,
    ApplicationName           VARCHAR (50)    NOT NULL,
    Description               VARCHAR (1000)    NULL,
    ReleaseVersion            float    NOT NULL,
    ReleaseDate               DATETIME2    NOT NULL,
    ApplicationInputFile      VARCHAR (500)    NULL,
    ApplicationDefaultInputs  VARCHAR (MAX)    NULL,

    CreatedDateTime        DATETIME2       NOT NULL CONSTRAINT DF_Application_CreatedDateTime DEFAULT(SYSDATETIME()),
    CreatedBy              VARCHAR (30)    NULL,
    LastModifiedDateTime   DATETIME2       NOT NULL CONSTRAINT DF_Application_LastModifiedDateTime DEFAULT(SYSDATETIME()),
    LastModifiedBy         VARCHAR (30)    NULL,
    DeletedAt              DATETIME2       NULL,

    CONSTRAINT [PK_Application] PRIMARY KEY CLUSTERED (ApplicationId ASC),
    CONSTRAINT [PK_Application_1] UNIQUE NONCLUSTERED (ApplicationName, ReleaseVersion)

);
