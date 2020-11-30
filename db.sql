
DROP TABLE IF EXISTS pings;
CREATE TABLE pings (
    ts TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    host TEXT,
    is_alive BOOLEAN,
    duration FLOAT
);
