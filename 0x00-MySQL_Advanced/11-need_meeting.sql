-- A sql script that creats a view need_meeting that lists all
-- all students that have a score under 80(strict) and no las_meeting
-- or more than a month from the current date
-- option2 last_meeting IS NULL OR `date` <= '2022-11-14';
CREATE VIEW need_meeting
AS SELECT name FROM students
WHERE score < 80 AND last_meeting IS NULL OR last_meeting < DATE(CURDATE() - INTERVAL 1 MONTH);

