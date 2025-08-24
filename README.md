📌 Social Media Fraudulent Checker






📖 Overview

The Social Media Fraudulent Checker is an algorithm-based project designed to detect suspicious or fraudulent accounts on social media platforms.

It analyzes a user's followers and followings using graph theory concepts such as the clustering coefficient, helping to identify whether the connections of an account appear genuine or artificially manipulated (bots, fake accounts, or spam networks).

This tool can be extended for:

Identifying bot networks

Detecting fake engagement (fake likes/followers)

Improving account credibility analysis for social media audits

🚀 Features

✔️ Calculates clustering coefficient of social graphs
✔️ Checks authenticity of followers/followings
✔️ Highlights accounts with suspicious connection patterns
✔️ Modular and extensible for future fraud detection algorithms
✔️ Lightweight and easy to integrate into larger social media monitoring systems

🏗️ How It Works

Input: Provide the social media account’s follower and following graph/network.

Algorithm:

Constructs a graph where nodes represent accounts and edges represent relationships.

Calculates the clustering coefficient for the network.

Compares it against thresholds/heuristics to detect anomalies.

Output: Flags accounts as genuine or potentially fraudulent.

⚙️ Tech Stack

Language: Python 🐍

Libraries Used:

networkx → Graph and clustering coefficient calculation

pandas → Data handling

matplotlib → Visualization (optional, for graphs)

📂 Project Structure
📦 social-media-fraudulent-checker
 ┣ 📜 main.py            # Main execution file
 ┣ 📜 requirements.txt   # Dependencies
 ┣ 📜 README.md          # Documentation
 ┣ 📂 data/              # Sample datasets
 ┗ 📂 utils/             # Helper functions

▶️ Installation & Usage
1️⃣ Clone the Repository
git clone https://github.com/Pushkar-03/social-media-fraudulent-checker.git
cd social-media-fraudulent-checker

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Project
python main.py

📊 Example Output

Genuine Accounts → Higher clustering coefficient, consistent network structure

Fraudulent Accounts → Very low clustering coefficient, scattered or bot-like patterns

(You can include a screenshot/graph here if available)

🔮 Future Enhancements

✅ Support for real-time API integration with platforms (Twitter, Instagram, etc.)

✅ Machine learning models for fraud classification

✅ Visualization dashboards for fraud detection insights

🤝 Contributing

Contributions are welcome! If you’d like to add new features or improve existing functionality:

Fork the repo

Create a feature branch

Commit your changes

Submit a pull request 🚀

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Pushkar ✨

GitHub

LinkedIn
 (optional)
