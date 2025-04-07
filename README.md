# 📌 eBay Product Bidder

🔍 A Python program that integrates with the eBay API to search for auctions containing specific keywords, filter out irrelevant items, and display the most favorable deals.

## ✨ Description

This project is designed to help users efficiently find and bid on desirable eBay auctions. It utilizes the eBay API to fetch auction data, filters it based on user-defined criteria, and provides a sorted list of top deals. The program can also be extended with features like real-time updates and notifications for items with limited time left.

## 🚀 Features

- **Keyword Search**: Query eBay API using specific keywords.
- **Price Filtering**: Filter auctions by price range to find the best deals.
- **Real-Time Updates**: Optionally receive notifications for auctions with less than 30 minutes left.
- **User-Friendly Web Interface**: Manage your bidding list through a Flask web application.

## 🛠️ Installation

To set up this project, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/gag3301v/eBay-Bidder.git
   cd eBay-Bidder
   ```

2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## 📦 Usage

### Running the Script

To run the script, execute:

```sh
python search_auctions.py
```

This will start fetching and displaying the best deals based on your specified keywords and price range.

### Using the Web Interface

1. **Run Flask Server**:
   ```sh
   python app.py
   ```

2. **Access the Web Interface**:
   Open a web browser and navigate to `http://127.0.0.1:5000/ebaybidder`.

## 🔧 Configuration

- **Environment Variables**: Set your eBay API credentials in an `.env` file.
  ```plaintext
  EBAY_APP_ID=your_app_id
  EBAY_DEV_ID=your_dev_id
  EBAY_CERT_ID=your_cert_id
  EBAY_AUTH_TOKEN=your_auth_token
  ```

## 🧪 Tests

To run tests, use:

```sh
python -m unittest discover tests/
```

Ensure you have the necessary test files in a `tests` directory.

## 📁 Project Structure

```
eBay-Bidder/
├── app.py
├── main.py
├── search_auctions.py
├── requirements.txt
└── .env.example
```

- **app.py**: Main Flask application file.
- **main.py**: Contains the `Search` class for eBay item searches.
- **search_auctions.py**: Script to fetch and display auction data.
- **requirements.txt**: Lists project dependencies.
- **.env.example**: Example configuration file for environment variables.

## 🙌 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note:** This README provides a template that can be customized further based on specific project requirements and features.