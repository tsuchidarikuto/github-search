import requests
import json
from typing import List, Dict, Any
import os
import pandas as pd
from datetime import datetime

"""
GitHub User Search Application

This application searches GitHub users based on a query and saves the results to CSV files.

Search Query Syntax:
- Basic operators:
  * OR: Match either condition (e.g., "python OR javascript")
  * AND: Match both conditions (e.g., "python AND developer")
  * NOT: Exclude matches (e.g., "python NOT java")
- Exact match with quotes:
  * "python developer": Exact phrase match
  * python developer: Partial match
- Qualifiers:
  * in:bio: Search in user's bio
  * in:name: Search in username
  * followers:>1000: Users with more than 1000 followers
  * location:japan: Users in Japan

Example queries:
- "python OR javascript": Python or JavaScript developers
- "python AND javascript": Developers who use both Python and JavaScript
- "python NOT java": Python developers who don't use Java
- "python in:bio followers:>1000": Python developers with 1000+ followers
- "python location:japan": Python developers in Japan

"""

# Search configuration
SEARCH_QUERY = '"AI Agent"'  # Modify this line to change the search query
MAX_RESULTS = 100  # Maximum number of users to retrieve (1-100)

class SimpleGitHubSearcher:
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def search_users(self, query: str, first: int = 100) -> List[Dict[str, Any]]:
        """
        Search users using GraphQL API
        """
        graphql_query = """
        query($query: String!, $first: Int!) {
            search(query: $query, type: USER, first: $first) {
                nodes {
                    ... on User {
                        login
                        name
                        bio
                        location
                        followers {
                            totalCount
                        }
                    }
                }
            }
        }
        """
        
        variables = {
            "query": query,
            "first": first
        }
        
        response = requests.post(
            "https://api.github.com/graphql",
            headers=self.headers,
            json={"query": graphql_query, "variables": variables}
        )
        
        if response.status_code == 200:
            response_data = response.json()
            
            # デバッグ情報を出力
            print("\nAPI Response:")
            print(json.dumps(response_data, indent=2))
            
            if "errors" in response_data:
                raise Exception(f"GraphQL errors: {response_data['errors']}")
            
            if "data" not in response_data or "search" not in response_data["data"]:
                raise Exception("Invalid response structure")
                
            return response_data["data"]["search"]["nodes"]
        else:
            raise Exception(f"GraphQL query failed: {response.status_code} - {response.text}")

def save_to_csv(users: List[Dict[str, Any]], query: str):
    """
    Save search results to CSV file
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = "/app/output"
    filename = f"github_users_{timestamp}.csv"
    filepath = os.path.join(output_dir, filename)
    
    # Convert data to DataFrame
    df = pd.DataFrame([
        {
            'Username': user.get('login', ''),
            'Display Name': user.get('name', ''),
            'Bio': user.get('bio', ''),
            'Location': user.get('location', ''),
            'Followers': user.get('followers', {}).get('totalCount', 0) if user.get('followers') else 0
        }
        for user in users
    ])
    
    # Save to CSV
    df.to_csv(filepath, index=False, encoding='utf-8')
    
    return filepath

def main():
    # Get GitHub token from environment variable
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

    if not GITHUB_TOKEN:
        print("Error: GITHUB_TOKEN environment variable is not set.")
        print("Please set GITHUB_TOKEN in your .env file.")
        return
    
    print("GitHub User Search System")
    print(f"Search Query: {SEARCH_QUERY}")
    print(f"Maximum Results: {MAX_RESULTS}")
    print("\nStarting search...")
    
    # Execute search
    searcher = SimpleGitHubSearcher(GITHUB_TOKEN)
    try:
        users = searcher.search_users(SEARCH_QUERY, first=MAX_RESULTS)
        
        if not users:
            print("\nNo users found matching the search criteria.")
            return
            
        # Display results
        print(f"\nSearch Results ({len(users)} users):")
        print("=" * 80)
        for user in users:
            print(f"Username: {user.get('login', 'N/A')}")
            print(f"Display Name: {user.get('name', 'N/A')}")
            if user.get('bio'):
                print(f"Bio: {user['bio']}")
            if user.get('location'):
                print(f"Location: {user['location']}")
            if user.get('followers'):
                print(f"Followers: {user['followers'].get('totalCount', 0)}")
            print("-" * 80)
        
        # Save to CSV
        filename = save_to_csv(users, SEARCH_QUERY)
        print(f"\nResults saved to {filename}")
            
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main() 