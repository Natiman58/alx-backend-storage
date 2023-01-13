-- A sql script that creates a stored procedure
-- that computes and stores the average score of a student
-- Note average score can be a decimal

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    user_id INT NOT NULL 
)
BEGIN
    UPDATE users
    SET average_score=(SELECT AVG(score) FROM corrections WHERE corrections.user_id=user_id) WHERE id=user_id;
END //
DELIMITER ;

