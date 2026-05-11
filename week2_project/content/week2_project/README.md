Week 2 — API Testing Framework with Pytest - Converting the Week 1 API testing script into a pytest framework which has assertions.

Folder structure in colab:
week2_project/
│── api_client.py        # Handles API requests
│── validators.py        # Validates status codes and response schema
│── logger.py            # Logs test results using Python logging
│── tests/
│    └── test_api.py     # Pytest test cases


How to run :
Navigate to directory : %cd /content/week2_project

Runing:
!pytest -v tests/test_api.py


Logging:
Results are saved in test_results.log with timestamps, test names, and PASS/FAIL status.
