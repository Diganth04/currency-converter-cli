# Currency Converter CLI

A simple and efficient command-line currency converter built using Python and FreeCurrencyAPI.
This tool allows users to convert currency values in real-time with secure API key handling.

---

## Features

* Convert currency between multiple countries
* Convert any custom amount
* Supports multiple currencies (USD, INR, EUR, GBP, JPY, etc.)
* Secure API key using `.env`
* Fast and lightweight CLI tool
* Error handling for invalid inputs

---

## Tech Stack

* Python
* Requests
* python-dotenv

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/currency-converter-cli.git
cd currency-converter-cli
```

### 2. Install dependencies

```bash
pip install requests python-dotenv
```

### 3. Create `.env` file

Create a file named `.env` in the root folder and add:

```env
API_KEY=your_api_key_here
```

Do not share this file or push it to GitHub.

---

## Usage

Run the program:

```bash
python currency.py
```

---

## Example

```
Enter base currency (q for quit): INR
Enter amount: 100

100 INR equals:

USD: 1.20
EUR: 1.10
GBP: 0.95
JPY: 160.25
```

---

## How It Works

1. User enters:

   * Base currency (e.g., INR)
   * Amount (e.g., 100)
2. Program fetches exchange rates from API
3. Multiplies rates with amount
4. Displays converted values

---

## Error Handling

* Invalid currency input is handled safely
* Invalid amount prompts retry
* API errors are handled gracefully

---

## Project Structure

```
currency-converter-cli/
│
├── currency.py        # Main application
├── .env               # API key (ignored in Git)
├── .gitignore         # Ignore sensitive files
└── README.md          # Project documentation
```

---

## Future Improvements

* Convert to a specific currency (one-to-one conversion)
* Add currency names and symbols
* Add historical trends or graphs
* Build a web interface (Flask or React)
* Add autocomplete for currency codes

---

## Author

Diganth
Aspiring Full-Stack Developer
