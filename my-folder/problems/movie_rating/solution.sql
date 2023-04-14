# Write your MySQL query statement below
WITH JoinedTable AS(
    SELECT r.*, m.title, u.name FROM 
        MovieRating as r 
        INNER JOIN 
            Movies as m 
            ON m.movie_id = r.movie_id 
        INNER JOIN 
            Users as u 
            ON u.user_id = r.user_id
)

SELECT 
    name as results
FROM
    (SELECT
        name,
        COUNT(*) as num_reviews
    FROM
       JoinedTable
    GROUP BY 
        name
    ORDER BY
        num_reviews DESC, name ASC
    LIMIT 1 
    ) as TopUser
UNION ALL
SELECT
    title as results
FROM
    (
        SELECT
            title,
            AVG(rating) as total_rating
        FROM
            JoinedTable
        WHERE
            created_at BETWEEN '2020-02-01' AND '2020-02-29'
        GROUP BY
            title
        ORDER BY
            total_rating DESC, title ASC
        LIMIT 1
    ) as TopMovie
