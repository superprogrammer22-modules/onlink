# Reporting Issues for ONLINK

Thank you for taking the time to report an issue or suggest an enhancement for the **ONLINK: Operational Network Linkage Interface Navigator Kit**. Your feedback is crucial for improving the package!

Before submitting an issue, please check the existing issues to see if your problem has already been reported.

## 🐛 Bug Reports

If you encounter an error or unexpected behavior, please provide as much detail as possible to help us quickly reproduce and fix the bug.

### Required Information for Bug Reports:

1.  **Summary:** A concise title describing the issue (e.g., "The `Read()` function fails on Wikipedia URLs").
2.  **ONLINK Version:** The version of the package you are using (`0.1.0`).
3.  **Python Environment:**
    * Python version (e.g., `3.10.12`).
    * Operating System (e.g., `Windows 11`, `Ubuntu 22.04`, `macOS Ventura`).
4.  **Steps to Reproduce:**
    * Provide the exact code snippet (ideally a minimal reproducible example) that triggers the error.
    * If the issue involves `Read()`, `Fetch()`, or `Open()`, **always include the exact URL** you are attempting to use.
5.  **Expected Behavior:** A clear description of what you expected the code to do.
6.  **Actual Behavior:** The actual result, including the full Python traceback/error message if one occurred.

### Special Notes:

* **Networking Issues (`Read`, `Fetch`, `Load`):** If a function fails to retrieve content or images, it might be due to changes in the target website's structure or aggressive anti-bot measures. Please confirm if the URL is accessible in a standard web browser before reporting.
* **Image/Vision Issues (`Load`, `Fetch`, `Show`):** Since ONLINK uses `cv2` (OpenCV), some issues can be platform-specific. Please ensure you detail your OS and Python environment fully.

---

## ✨ Feature Requests

We welcome ideas for new functionality! When suggesting a feature, please consider:

1.  **What problem are you trying to solve?** Describe the scenario or workflow that the new feature would address.
2.  **The Proposed Solution:** Describe how you envision the new function or parameter working (e.g., "Add a `max_retries` parameter to `Read()` to handle temporary network failures").
3.  **Why should this be included in ONLINK?** Explain how this feature aligns with the package's goal of simplified network linkage and navigation.

---

## 💻 Submitting Code Changes (Pull Requests)

While this file is focused on reporting, if you wish to contribute a fix or a feature directly:

1.  Please open an issue first to discuss the bug or feature with the maintainers.
2.  Follow the standard GitHub Fork and Pull Request workflow.
3.  Ensure your code adheres to a standard Python style (e.g., PEP 8).
4.  Write clear, descriptive commit messages.

Thank you again for your support of ONLINK!