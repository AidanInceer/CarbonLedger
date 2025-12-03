# CarbonLedger

A Python project combining a Machine Learning engine (placeholder) with a Django web application for tracking carbon footprint transactions.

## Project Structure

- **`src/ml_project/`**: Lightweight ML engine (placeholder for future development)
- **`src/web_app/`**: Django web application for transaction tracking
- **`tests/`**: Unit tests
- **`data/`**: Data files (ignored by git)
- **`models/`**: Trained models (ignored by git)
- **`notebooks/`**: Jupyter notebooks

## Setup

### 1. Install `uv`
```bash
pip install uv
```

### 2. Install dependencies
```bash
uv sync
```

### 3. Set up the database (Django)
```bash
cd src/web_app
uv run python manage.py migrate
```

### 4. Load sample data
```bash
uv run python manage.py loaddata sample_data
```

This loads 10 sample transactions across different categories (beverages, food, merchandise).

### 5. Run the Django server
```bash
uv run python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the application.

## Running the ML Engine

```bash
uv run python src/ml_project/main.py
```

## Testing

```bash
uv run pytest
```

## Linting

```bash
uv run ruff check .
uv run ruff check . --fix  # Auto-fix issues
```

## Roadmap

### Phase 1: Core Project Functionality

- [ ] **1.1 Excel File Upload**: Implement ability to upload an Excel file and automatically populate the transactions tab (upload to the database)
- [ ] **1.2 Customizable Reporting**: Add customizable reporting features (e.g., bar charts, custom visualizations)
- [ ] **1.3 Model Page**: Create a new page for Model (rename the customization/settings tab in projects)
- [ ] **1.4 Account and Team Management**: Implement proper account and team management functionality

### Phase 2: Model Implementation

Model implementation to assign carbon estimates. General steps required:

- [ ] **2.1 Data Schema Design**: Define schema for carbon emission factors and transaction-to-emission mappings
- [ ] **2.2 Emission Factor Database**: Build/integrate database of emission factors by category, product, or activity
- [ ] **2.3 Calculation Engine**: Develop calculation logic to estimate carbon footprint based on transaction data and emission factors
- [ ] **2.4 Model Integration**: Integrate the carbon estimation model with the transaction workflow
- [ ] **2.5 Validation & Calibration**: Validate model outputs against known benchmarks and calibrate as needed
- [ ] **2.6 UI for Carbon Estimates**: Display carbon estimates alongside transactions in the UI

### Phase 3: Enhanced Account Features & Advanced Reporting

- [ ] **3.1 Profile Picture Upload**: Add ability for users to upload and manage profile pictures
- [ ] **3.2 Two-Factor Authentication (2FA)**: Implement 2FA for login security *(low priority, much later)*
- [ ] **3.3 Detailed Reporting**: Expand reporting capabilities with more granular analytics and insights

### Phase 4: Productionization

- [ ] **4.1 Unit and Integration Tests**: Develop comprehensive test suite for all application components
- [ ] **4.2 Framework Evaluation**: Evaluate whether to move away from Django (consider scalability, performance, team expertise)
- [ ] **4.3 CI/CD Pipeline**: Set up proper CI/CD pipeline for the web application
- [ ] **4.4 CI/CD Documentation**: Add important CI/CD files (e.g., CODEOWNERS, branch protection policies)
- [ ] **4.5 Database Abstraction**: Implement separation of concerns and plug-and-play architecture for database layer

### Phase 5: Deep Work & MLOps

- [ ] **5.1 External Data Integrations**: Integrate with external data sources for enhanced functionality
- [ ] **5.2 Live Model Implementation**: Deploy live carbon estimation model in production
- [ ] **5.3 MLOps Pipeline**: Establish MLOps practices (model versioning, monitoring, retraining, deployment automation)
