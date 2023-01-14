-- A sql script that creats a view need_meeting that lists all
-- all students that have a score under 80(strict) and no las_meeting
-- or more than a month
CREATE VIEW need_meeting
AS SELECT name FROM students
WHERE score < 80 AND last_meeting IS NULL OR last_meeting <= '2022-11-14';

