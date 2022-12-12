SET IDENTITY_INSERT XOM.Risers ON

--If data already exists, then update the records. Otherwise, insert new records. An "upsert"
MERGE XOM.Risers WITH(HOLDLOCK) r
USING (
    SELECT 1, 'Drilling', 'Noble Bob Douglas'
--    UNION ALL SELECT 2, 'TOP', 'Trajectory Optimization', 'Trajectory Optimization', 'MANUAL', 2

) AS SOURCE(RiserId, RiserType, Vessel) ON (r.RiserId = SOURCE.RiserId)
WHEN MATCHED THEN UPDATE SET RiserType = SOURCE.RiserType, Vessel = SOURCE.Vessel
WHEN NOT MATCHED THEN INSERT (RiserId, RiserType, Vessel) VALUES (SOURCE.RiserId, SOURCE.RiserType, SOURCE.Vessel);

SET IDENTITY_INSERT XOM.Risers OFF
