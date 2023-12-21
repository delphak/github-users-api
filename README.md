# github-users-api
This Python script allows you to scrape GitHub users' data using the GitHub API. It retrieves a list of GitHub users, filters them based on specific criteria (e.g., not site admins, a certain number of followers), and logs the relevant information to a CSV file.

## Notes
The script uses a random since parameter to start retrieving users from a random ID. Adjust the range or set a specific value based on your requirements.
The script includes a delay of 0.72 seconds between API requests to comply with GitHub API rate limits.
### Caution:
Be mindful of GitHub API usage limits. Exceeding these limits may result in temporary or permanent restrictions on your account. Make sure to adhere to GitHub's rate limits.
