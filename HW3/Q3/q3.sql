CREATE TYPE DivisionType AS ENUM('Atlantic', 'Central', 'Southeast', 'Northwest', 'Pacific', 'Southwest');
CREATE TYPE ConferenceType AS ENUM('Eastern', 'Western');
create table teams(
id text PRIMARY KEY CHECK (char_length(id) = 3),
location text,
name text,
division DivisionType,
conference ConferenceType);