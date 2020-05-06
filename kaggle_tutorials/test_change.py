answers_query = """
                SELECT a.id, a.body, a.owner_user_id
                FROM `bigquery-public-data.stackoverflow.posts_questions` AS q
                INNER JOIN `bigquery-public-data.stackoverflow.posts_answers` AS a
                    ON q.id = a.parent_id
                WHERE q.tags LIKE '%bigquery%'
                """
# Set up the query
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
 # Your code goes here
answers_query_job = client.query(answers_query, job_config=safe_config)
# API request - run the query, and return a pandas DataFrame
answers_results = answers_query_job.to_dataframe()
# Your code goes here
