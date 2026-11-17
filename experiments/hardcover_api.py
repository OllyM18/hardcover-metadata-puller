import requests

api_url = "https://api.hardcover.app/v1/graphql"

# Trying to find edition by ISBN
body = """
query GetEditionsByISBN {
    editions(where: {isbn_13:{_eq: "9781399622066"}}) {
        id,
        title,
        release_date,

        publisher {
            name
        }
        
        contributions {
            author {
                name
            }
        }

        language {language}
    }
}
"""

response = requests.post(url=api_url, json={"query": body}, headers={"Authorization": ""})

print("Response code: ", response.status_code)
print("response: ", response.content)