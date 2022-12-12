CREATE TABLE dbo.Project
(
	ProjectId                BIGINT      IDENTITY(1,1)    NOT NULL,
    ProjectName               VARCHAR (100)    NOT NULL,
    Description               VARCHAR (1000)    NULL,
    ClientId                 BIGINT    NOT NULL,

    CreatedDateTime        DATETIME2       NOT NULL CONSTRAINT DF_Project_CreatedDateTime DEFAULT(SYSDATETIME()),
    CreatedBy              VARCHAR (30)    NULL,
    LastModifiedDateTime   DATETIME2       NOT NULL CONSTRAINT DF_Project_LastModifiedDateTime DEFAULT(SYSDATETIME()),
    LastModifiedBy         VARCHAR (30)    NULL,
    DeletedAt              DATETIME2       NULL,

    CONSTRAINT [PK_Project] PRIMARY KEY CLUSTERED ([ProjectId] ASC),
    CONSTRAINT [PK_Project_1] UNIQUE NONCLUSTERED (ProjectName, ClientId),
    CONSTRAINT [FK_Project_Client] FOREIGN KEY ([ClientId]) REFERENCES [dbo].[Client] ([ClientId])

);
