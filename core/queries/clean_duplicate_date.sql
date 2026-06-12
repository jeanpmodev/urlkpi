DELETE FROM dash_errormanagement
WHERE id NOT IN (
    SELECT MIN(id) 
    FROM dash_errormanagement 
    GROUP BY DATE(error_datetime)
);
