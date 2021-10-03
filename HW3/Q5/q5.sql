ALTER TABLE player_bios
ADD COLUMN position text;

UPDATE player_bios
SET position = (SELECT position from new_table WHERE player_bios.id = new_table.player); 

select firstname, lastname, position from player_bios
where id <= 5;