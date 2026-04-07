# 📊 Student Result Analytics Platform

A comprehensive web-based analytics platform for students to upload, analyze, and visualize their academic performance data with machine learning insights and interactive dashboards.

## 🚀 Features

### Core Functionality
- **Secure Authentication**: User registration and login with SHA256 password hashing
- **File Upload Support**: Process CSV and PDF student result files with automatic text extraction
- **Interactive Dashboard**: Real-time analytics with multiple chart types (bar, line, histogram, pie, scatter plots)
- **Academic Analytics**: SGPA trends, subject-wise performance analysis, semester comparisons
- **Machine Learning Insights**: 
  - K-means clustering for performance grouping
  - Linear regression for SGPA prediction
  - PCA for dimensionality reduction
  - Performance pattern recognition

### Advanced Features
- **Multi-Database Support**: PostgreSQL, MongoDB, and JSON file storage
- **PDF Report Generation**: Export academic reports with charts and analysis
- **Data History Management**: Track academic progress across multiple semesters
- **Responsive Design**: Mobile-friendly interface with professional styling
- **Real-time Visualizations**: Interactive Plotly charts with hover effects

## 🛠️ Tech Stack

### Frontend
- **Streamlit** - Web application framework
- **Plotly** - Interactive data visualization
- **HTML/CSS** - Custom styling and responsive design

### Backend
- **Python 3.11+** - Core programming language
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning algorithms

### Database
- **PostgreSQL** - Primary production database
- **MongoDB** - Alternative NoSQL database support
- **JSON Files** - Development and testing storage

### File Processing
- **PDFplumber** - PDF text extraction
- **ReportLab** - PDF report generation
- **CSV Processing** - Built-in pandas support

### Security & Authentication
- **Hashlib** - SHA256 password hashing
- **Session Management** - Streamlit session state
- **Input Validation** - File upload security

## 📋 Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Optional: PostgreSQL or MongoDB for production use

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/S37F/ReSuLt-Analyzer-ML.git
cd ReSuLt-Analyzer-ML
```

### 2. Install Dependencies
```bash
pip install streamlit pandas numpy plotly scikit-learn statsmodels pdfplumber reportlab psycopg2-binary pymongo sqlalchemy
```

### 3. Run the Application
```bash
streamlit run app.py
```

### 4. Access the App
Open your browser and navigate to `http://localhost:8501`

## 🔧 Configuration

### Database Setup (Optional)

#### PostgreSQL
```bash
# Set environment variables
export DATABASE_URL="postgresql://username:password@localhost:5432/dbname"
```

#### MongoDB
```bash
# Set environment variables
export MONGODB_URL="mongodb://localhost:27017/student_analytics"
```

#### File-based Storage (Default)
No configuration required - uses local JSON files for development.

## 📁 Project Structure

```
student-analytics-platform/
├── app.py                    # Main Streamlit application
├── auth.py                   # Authentication system
├── database.py               # Multi-database manager
├── analytics.py              # Performance analytics engine
├── visualizations.py         # Chart generation
├── ml_models.py             # Machine learning models
├── utils.py                 # File processing utilities
├── .streamlit/
│   └── config.toml          # Streamlit configuration
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
└── setup_instructions.md    # Detailed setup guide
```

## 📊 Usage

### 1. User Registration
- Create a new account with username and password
- Secure authentication with password hashing

### 2. Data Upload
- Upload CSV files with academic results
- Process PDF mark sheets with automatic text extraction
- Support for multiple semester data

### 3. Analytics Dashboard
- View SGPA trends across semesters
- Analyze subject-wise performance
- Compare academic progress over time

### 4. Machine Learning Insights
- Discover performance patterns with clustering
- Get SGPA predictions based on current performance
- Visualize data relationships with PCA

### 5. Report Generation
- Export comprehensive PDF reports
- Include charts, statistics, and insights
- Professional formatting for academic records

## 🏗️ Architecture

### Frontend Architecture
- **Streamlit Framework**: Interactive web interface
- **Modular Components**: Separate tabs for different features
- **Responsive Design**: Works on desktop and mobile devices

### Backend Architecture
- **Database Abstraction**: Unified interface for multiple database types
- **Modular Analytics**: Separate modules for different analysis types
- **Session Management**: Secure user session handling

### Data Flow
1. User authentication and session creation
2. File upload and processing
3. Data validation and storage
4. Analytics computation
5. Visualization generation
6. Report export

## 🔒 Security Features

- **Password Hashing**: SHA256 encryption for user passwords
- **Session Management**: Secure user session handling
- **Input Validation**: File upload security checks
- **Data Isolation**: User-specific data separation
- **Error Handling**: Comprehensive error management

## 🚀 Deployment

### Local Development
```bash
streamlit run app.py --server.port 8501
```

### Production Deployment
1. **Heroku**: Use provided `Procfile` and requirements
2. **Docker**: Container deployment with multi-stage builds
3. **Cloud Platforms**: AWS, GCP, Azure compatible
4. **Replit**: Ready for Replit deployment

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Issues & Support

- **Bug Reports**: Use GitHub Issues
- **Feature Requests**: Create an issue with the enhancement label
- **Documentation**: Check the README and setup instructions
- **Community**: Discussions tab for questions and ideas

## 🏆 Key Highlights

- **Production Ready**: Comprehensive error handling and logging
- **Scalable Architecture**: Supports multiple database backends
- **Professional Documentation**: Complete setup and usage guides
- **Machine Learning Integration**: Advanced analytics capabilities
- **Responsive Design**: Works across all device sizes
- **Security Focused**: Industry-standard security practices

## 📈 Performance

- **Fast Loading**: Optimized data processing
- **Efficient Storage**: Compressed data serialization
- **Caching**: Session-based data caching
- **Responsive UI**: Real-time chart updates

## 🔮 Future Enhancements

- [ ] Real-time collaboration features
- [ ] Advanced ML models (Neural Networks, Random Forest)
- [ ] Integration with university APIs
- [ ] Mobile app companion
- [ ] Advanced reporting templates
- [ ] Batch data processing
- [ ] API endpoints for external integrations

---

**Built with ❤️ for students to better understand and analyze their academic performance.**

*Star ⭐ this repository if you find it helpful!*