# Ebay Api Auction Finder
A python script that uses the eBay API to search for auctions with specific keywords and find the best deal.

## Dependencies
- requests (for making API requests)
- json (for parsing API responses)
## Usage
First, you'll need to obtain an API key from eBay by following the instructions here.

Clone this repository and navigate to the directory in your terminal.

Install the dependencies by running pip install -r requirements.txt.

Set your API key as an environment variable by running export EBAY_API_KEY=<your_api_key>.

Run the script by entering python ebay_bot.py <keyword>, replacing <keyword> with the item you'd like to search for.

## Example
To search for auctions with the keyword "iphone", run python ebay_bot.py iphone. The script will return a list of auctions sorted by price, with the best deal at the top.
