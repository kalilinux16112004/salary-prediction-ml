Salary Prediction App - Employee Monthly Income Predictor

Welcome!
Thank you for downloading the Salary Prediction App! This is a simple, user-friendly web app built with Python and Streamlit. It helps predict employees' monthly salaries based on details like age, job role, experience, and more. You can predict for one employee at a time or upload a whole CSV file for bulk predictions.

The app uses machine learning models (like Linear Regression) to make predictions. No coding skills needed – just follow these easy steps to set it up and run it. We'll guide you through everything one step at a time.

What You'll Need (Prerequisites)
Before you start, make sure you have these:
1. A Windows computer (this app is tested on Windows; it might work on others, but we recommend Windows).
2. Internet connection (for installing Python tools the first time).
3. Python installed – This is a free programming tool. We recommend version 3.12.9 for best results.
   - If you don't have it, download it from the official website: https://www.python.org/downloads/
   - During installation, check the box that says "Add Python to PATH" – this is important!
4. The project files – You should have a folder with these files:
   - app3.py (the main app file)
   - req.txt (list of tools the app needs)
   - code.ipynb (a Jupyter notebook to train the models – it might be named 'code' without extension, but it's a .ipynb file)
   - Any other files like sample CSVs for testing.

If anything is missing, double-check your download.

Step-by-Step Installation Guide
Follow these steps carefully. We'll use simple commands in a window called PowerShell (it's like a command prompt on your computer).

Step 1: Install Python
- Go to https://www.python.org/downloads/
- Download the latest version (we suggest 3.12.9).
- Run the installer.
- Important: Check "Add Python to PATH" during setup.
- Finish the installation and restart your computer if asked.

To check if Python is installed:
- Press Windows key + S, search for "cmd", and open Command Prompt.
- Type python --version and press Enter. It should show something like "Python 3.12.9". If not, reinstall.

Step 2: Set Up the Project Folder
- Open your project folder (where app3.py is).
- Hold Shift key + Right-click inside the folder (not on a file).
- Choose "Open PowerShell window here" (or "Open in Terminal" if that's what you see).

A blue window (PowerShell) will open.

Step 3: Set Execution Policy
This allows PowerShell to run scripts safely.

In the PowerShell window, type this and press Enter:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

- It might ask for confirmation. Type A (for Yes to all) and press Enter.

Step 4: Create a Virtual Environment
This is like a safe space for the app's tools, so it doesn't mess with other things on your computer.

In the PowerShell window, type this and press Enter:
python -m venv env

- You'll see a new folder called "env" appear in your project folder. That's normal!

Step 5: Activate the Virtual Environment
Type this and press Enter:
env\Scripts\activate

- Your PowerShell prompt should now start with "(env)" – that means it's activated.
- If you close the window, you'll need to reopen PowerShell in the folder and run this activation command again.

Step 6: Install Required Tools
The app needs some extra Python tools (like libraries). They're listed in "req.txt".

Copy and paste this whole command into PowerShell and press Enter:
Get-Content req.txt | ForEach-Object {
    try {
        pip install $_
    }
    catch {
        Write-Warning "⚠️ Failed to install $_ — skipping."
    }
}

- This will install everything one by one. It might take a few minutes.
- If you see warnings (yellow text) about failing to install something, that's okay – the app might still work. But if many fail, check your internet or try again.
- Note: "pip" is Python's tool installer – it comes with Python.

Step 7: Train the Models (Run the Jupyter Notebook)
The app needs trained models to make predictions. These are created by running a Jupyter notebook.

- First, make sure Jupyter is installed (it should be from the requirements in req.txt).
- In the same PowerShell window (with env activated), type this and press Enter:
jupyter notebook

- A web browser will open with Jupyter interface.
- Find and click on the file named 'code' (or code.ipynb).
- In the notebook, click "Kernel" > "Restart & Run All" (or click the "Run All" button if available).
- Wait for it to finish running all cells. This will create files like linear_model.joblib, lasso_model.joblib, etc., in your folder.
- These are the model files. Once done, you can close the Jupyter tab and browser.
- Back in PowerShell, press Ctrl + C to stop the Jupyter server.

Running the Application
Now you're ready to launch the app!

Step 1: Start the App
In the same PowerShell window (with the virtual environment activated), type this and press Enter:
streamlit run app3.py

- Your web browser will automatically open with the app (it looks like a website).
- If it doesn't open, look in PowerShell for a message like "You can now view your Streamlit app in your browser." and copy the link (like http://localhost:8501) into your browser.

Step 2: Using the App
The app is called "Employee Monthly Income Prediction App". Here's how to use it:

1. Sidebar Options:
   - Choose "Prediction Mode": Single Employee Prediction or Bulk Prediction (CSV Upload).
   - Choose a "Model": Like Linear Regression (default is fine for starters).

2. For Single Employee Prediction:
   - In the sidebar, enter details like Department, Age, Job Role, etc., using sliders and dropdowns.
   - Click "Predict Salary" at the bottom.
   - See the predicted monthly income displayed.

3. For Bulk Prediction (CSV Upload):
   - Upload a CSV file with employee data (same format as your training data – columns like Age, Department, etc.).
   - The app will show previews, some charts (like income distribution), and add a "Predicted_Monthly_Income" column.
   - Download the updated CSV with predictions.

4. Stop the App:
   - In PowerShell, press Ctrl + C to stop the server when done.

Tips for Best Results
- Model Choice: Try different models (Linear, Lasso, etc.) to see which gives better predictions.
- CSV Format: For bulk, make sure your CSV has the right columns matching the training data (like Age, DistanceFromHome, etc.).
- Data Accuracy: Enter realistic values for better predictions.
- Multiple Runs: If you close the app, just run streamlit run app3.py again in PowerShell.

Troubleshooting (If Something Goes Wrong)
- Python not found: Make sure you added it to PATH during install. Restart your computer.
- Installation fails: Check internet. Run the install command again.
- Jupyter not opening: Make sure 'jupyter' is in req.txt and installed. If not, add "pip install jupyter" manually.
- Models not created: Ensure the notebook runs without errors. Check for missing data files if needed.
- App not loading: Make sure the .joblib files are in the folder. Rerun the notebook.
- Warnings during install: If the app won't run, note the error and search online (e.g., "pip install error [package name]").
- Slow performance: Close other programs.

If you need help, feel free to ask in online forums like Reddit (r/learnpython) with your error message.

About the Project
This app uses Python libraries like Streamlit for the interface, Pandas for data handling, and Scikit-learn for models. It predicts salaries based on employee features.

Enjoy predicting salaries! 💰 If you like it, share your feedback at training@craw.in
If any issues you can ping me at:-
LinkedIn - Shivam Bamania (Craw Cybersecurity)