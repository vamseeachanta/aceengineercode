SET IDENTITY_INSERT XOM.StatisticsClass ON

--If data already exists, then update the records. Otherwise, insert new records. An "upsert"
MERGE XOM.StatisticsClass WITH(HOLDLOCK) sc
USING (
    SELECT 1, 'Entire Table'
    UNION ALL SELECT 2, 'Time Range'

) AS SOURCE(StatisticsClassId, StatisticsClassType) ON (sc.StatisticsClassId = SOURCE.StatisticsClassId)
WHEN MATCHED THEN UPDATE SET StatisticsClassType = SOURCE.StatisticsClassType
WHEN NOT MATCHED THEN INSERT (StatisticsClassId, StatisticsClassType) VALUES (SOURCE.StatisticsClassId, SOURCE.StatisticsClassType);

SET IDENTITY_INSERT XOM.StatisticsClass OFF
