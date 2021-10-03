ALTER TABLE player_bios
ADD COLUMN aux_column numeric;

UPDATE player_bios
SET aux_column = 12*split_part(height,'-',1)::integer + split_part(height,'-',2)::integer;

ALTER TABLE player_bios
DROP COLUMN height;

ALTER TABLE player_bios
RENAME COLUMN aux_column TO height;