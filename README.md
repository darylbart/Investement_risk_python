### <span style="color:#000000">📈 Investment Risk Appetite Determination Tool</span>

### <span style="color:#4CAF50">🔍 Summary</span>
1. [Overview](#overview)
2. [How it Works](#how-it-works)
3. [Usage](#usage)
4. [Questions and Weights](#questions-and-weights)
5. [Future Features Roadmap](#future-features-roadmap)
6. [Code Structure](#code-structure)
7. [Assisted by](#assisted-by)

#### <span style="color:#4CAF50">1. 📚 Overview</span>

The **Investment Risk Appetite Determination Tool** is an interactive Python application designed to help users understand their investment risk appetite. By answering a curated set of questions, the tool calculates a personalized risk profile, shedding light on the user's investment preferences and risk tolerance.

#### <span style="color:#4CAF50">2. ⚙️ How it Works</span>

1. Users start by specifying the number of questions they'd like to answer (ranging from 5 to 20).
2. The application then presents carefully crafted questions to the user, each with a predefined weight, reflecting its significance in determining the overall risk profile.
3. Users provide their responses on a scale of 1 to 5 for each question.
4. The tool performs a weighted average calculation based on the user's responses, ultimately determining their risk appetite through an average score.

#### <span style="color:#4CAF50">3. 🛠️ Usage</span>

Follow these steps to get started:

1. **Clone this repository to your local machine.**
2. **Install the required dependencies** using `pip install -r requirements.txt`.
3. **Run the application** using `python3 app.py`.
4. **Open a web browser and navigate to [http://localhost:5000](http://localhost:5000)** to access and utilize the tool.

#### <span style="color:#4CAF50">4. ❓ Questions and Weights</span>

The questions are meticulously curated to assess the user's investment preferences and risk tolerance. Each question is associated with a weight, symbolizing its importance in the calculation of the user's risk profile. For a complete list of questions and their respective weights, consult the [questions.json](questions.json) file.

#### <span style="color:#4CAF50">5. 🚀 Future Features Roadmap</span>

- **Interactive Visualization**: We plan to incorporate interactive charts, providing users with a visual representation of their risk profile and investment preferences.
- **Machine Learning Integration**: Our vision involves implementing machine learning algorithms to enhance risk assessment accuracy based on user responses.
- **Customizable Weighting**: Future updates will enable users to tailor question weights according to their personal preferences.

#### <span style="color:#4CAF50">6. 🏗️ Code Structure</span>

The application is structured around the following components:

- [**app.py**](./app.py): This file houses the Flask web application, managing user interactions and risk assessment.
- [**risk_determination.py**](./risk_determination.py): Contains the logic to determine the user's risk appetite based on their responses.
- [**questions_loader.py**](./questions_loader.py): Randomizes questions and weights from a JSON file.
- [**templates/**](./templates/): Holds HTML templates that shape the user interface.


#### <span style="color:#4CAF50">7. 🤖 Assisted by</span>
**CHATGPT** 🤖 Leveraging the power of **AI**. 🧠
