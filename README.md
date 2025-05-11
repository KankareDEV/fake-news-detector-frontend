# Fake News Detector Frontend

This is a simple web-based interface that lets users test news articles against a deployed AWS machine learning model.

### 🌐 Live Demo

Paste any article or sentence and click "Check". The app will tell you if the news seems **real** or **fake**.

### 🧱 Full Tech Stack

#### 🔗 Frontend
- HTML + CSS + JavaScript (Vanilla)
- CORS-enabled fetch request to API Gateway

#### ⚙️ Backend
- **Amazon API Gateway** (REST API) – receives requests from frontend
- **AWS Lambda** – processes input, invokes ML model, and returns prediction
- **AWS SageMaker** – multi-model endpoint serving the Fake News Classifier

#### 📦 Storage & Logging
- **AWS S3** – optionally stores inputs (if implemented)
- **AWS CloudWatch** – logs all Lambda invocations and runtime diagnostics

#### 🔐 Security
- **AWS IAM** – manages role-based access between Lambda, SageMaker, and S3


### 🛠 How It Works

1. User enters text
2. JavaScript sends POST request to API Gateway
3. API Gateway triggers a Lambda function
4. Lambda invokes the SageMaker endpoint with the input
5. SageMaker returns a prediction (0 = Fake, 1 = Real)
6. The result is shown on the page

### 🔧 Example API Request

```json
POST /prod/predict
{
  "texts": ["This is a sample news article."]
}
