-- A sql script that creates a stored procedure
-- that computes and stores the average score of a student
-- Note average score can be a decimal

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    user_id FLOAT NOT NULL 
)
BEGIN 
    SELECT `average_score` from users WHERE average_score=score
    THEN
    AVG(score)
END //
DELIMITER ;
