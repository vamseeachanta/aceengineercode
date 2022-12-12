CREATE TABLE dbo.Client
(
	ClientId                  BIGINT      IDENTITY(1,1)    NOT NULL,
    Company                      VARCHAR (100)    NOT NULL,
    KeyBusinessAreas          VARCHAR (1000)    NULL,
    Contact                   VARCHAR (100)    NOT NULL,
    Email                     VARCHAR (100)    NOT NULL,

    CreatedDateTime        DATETIME2       NOT NULL CONSTRAINT DF_Client_CreatedDateTime DEFAULT(SYSDATETIME()),
    CreatedBy              VARCHAR (30)    NULL,
    LastModifiedDateTime   DATETIME2       NOT NULL CONSTRAINT DF_Client_LastModifiedDateTime DEFAULT(SYSDATETIME()),
    LastModifiedBy         VARCHAR (30)    NULL,
    DeletedAt              DATETIME2       NULL,

    CONSTRAINT [PK_Client] PRIMARY KEY CLUSTERED ([ClientId] ASC),
    CONSTRAINT [PK_Client_1] UNIQUE NONCLUSTERED (Company, Contact)
);
