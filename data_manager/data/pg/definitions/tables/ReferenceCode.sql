CREATE TABLE dbo.ReferenceCode
(
	ReferenceCodeId BIGINT      IDENTITY(1,1)    NOT NULL,
    ReferenceCode          VARCHAR (100)        NOT NULL,
    Description            VARCHAR (100)        NULL,
    ReleaseYear            INT                  NULL,
    ReleaseDate            DATETIME2            NOT NULL,

    CreatedDateTime        DATETIME2       NOT NULL CONSTRAINT DF_ReferenceCode_CreatedDateTime DEFAULT(SYSDATETIME()),
    CreatedBy              VARCHAR (30)    NULL,
    LastModifiedDateTime   DATETIME2       NOT NULL CONSTRAINT DF_ReferenceCode_LastModifiedDateTime DEFAULT(SYSDATETIME()),
    LastModifiedBy         VARCHAR (30)    NULL,
    DeletedAt              DATETIME2       NULL,

    CONSTRAINT PK_ReferenceCode PRIMARY KEY CLUSTERED (ReferenceCode, ReleaseDate)
);
