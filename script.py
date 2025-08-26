# Create structured data for Akshay's portfolio based on his resume
import json

# Extract key information from resume
akshay_data = {
    "personal_info": {
        "name": "Akshay Verma",
        "title": "Principal Software Engineer",
        "experience": "10 years",
        "contact": {
            "phone": "+91-9013798681",
            "email": ["akshayverma91@gmail.com", "akshayverma91@hotmail.com"],
            "linkedin": "https://www.linkedin.com/in/akshayverma91/"
        }
    },
    "professional_summary": "Principal Software Engineer with 10 years of experience driving the design, development, and deployment of scalable Web applications, Microservices and Event-driven architectures, and platform engineering.",
    "current_role": {
        "company": "Bhavna Software India Pvt Ltd, Noida",
        "position": "Principal Software Engineer",
        "duration": "26th July 2019 – Present"
    },
    "key_projects": [
        {
            "name": "ConnectWise Project",
            "description": "Spearheaded the development of key features for the ConnectWise platform services, an automated MSP (Managed Service Provider) solution focused on managing workload and productivity and enabling data-driven business operations.",
            "technologies": [".NET Core", "Go", "ReactJS"],
            "impact": "Increased user engagement and improved customer satisfaction"
        },
        {
            "name": "Meridian Link Project",
            "description": "Led key enhancements of the Meridian Link Portal, a web-based application designed to streamline lending and deposit account origination processes for financial institutions.",
            "technologies": ["HTML", "CSS", "JavaScript", "ES6", "ES7", "ReactJS", "C#", "ASP.NET Core", "Golang"]
        }
    ],
    "work_experience": [
        {
            "company": "Bhavna Software India Pvt Ltd, Noida",
            "position": "Principal Software Engineer",
            "duration": "26th July 2019 – Present",
            "key_achievements": [
                "Developed RESTful APIs and Kafka integration with external systems",
                "Mentored junior developers and improved team productivity",
                "Collaborated with clients to analyze requirements and enhance product features"
            ]
        },
        {
            "company": "Conduent, Noida",
            "position": "Senior Software Engineer",
            "duration": "28 May 2018 to 25 July 2019",
            "key_achievements": [
                "Developed and maintained Conduent Workflow Administration System (CWAS) for Bank of America",
                "Optimized database queries and stored procedures in SQL Server 2014"
            ]
        },
        {
            "company": "Expedien eSolution Ltd, Noida",
            "position": "Assistant Consultant ERP",
            "duration": "22 June 2015 to May 2018",
            "key_achievements": [
                "Automated student registration process",
                "Developed modules for HRMS, Employee Portal, Attendance, and Student Management systems"
            ]
        }
    ],
    "education": [
        {
            "degree": "Master - MCA",
            "institution": "GGSIP University, New Delhi",
            "year": "2015"
        },
        {
            "degree": "Bachelor - B.Sc. Physics (H)",
            "institution": "Delhi University",
            "year": "2012"
        }
    ],
    "technical_skills": {
        "programming_languages": ["C#", "Go"],
        "scripting_languages": ["JavaScript (ES6, ES7)"],
        "technologies": [
            "ASP.NET Core", "ASP.NET", "Go", "Web Forms", "ADO.NET", 
            "Entity Framework", "LINQ", "RESTful Web API", "Web Services", 
            "ReactJS", "Swagger", "Graph QL", "Docker", "Kafka", "AWS"
        ],
        "development_tools": [
            "Visual Studio 2022", "VS Code", "Postman", "Git Bash", 
            "Tortoise", "MS SQL Server", "MySQL"
        ],
        "reporting_tool": ["Crystal Reports"],
        "database": ["Microsoft SQL Server"],
        "code_sharing_tools": ["GitHub", "VSS", "TF"],
        "productive_tools": ["GitHub CoPilot", "Gemini AI Studio"]
    },
    "certifications": ["NET Qualified in Computer Science"],
    "side_projects": [
        {
            "name": "Family Tree Medical Tracker",
            "url": "https://188694-e55f7ab2f5514b468d5f643487f3708d-5-latest.app.mgx.dev/",
            "description": "Family tree application to track medical history and early detection of medical problems by analyzing family medical records",
            "features": ["AI Family Assistant", "Interactive family tree visualization", "Medical history tracking"]
        },
        {
            "name": "AstroShakti",
            "url": "https://www.astroshakti.in/",
            "description": "Personal astrology website offering astrological services and insights",
            "focus": "Vedic astrology and spiritual guidance"
        }
    ]
}

# Convert to JSON for easy use
portfolio_data_json = json.dumps(akshay_data, indent=2)
print("Akshay's Portfolio Data Structure:")
print(portfolio_data_json)

# Save to file for reference
with open('akshay_portfolio_data.json', 'w') as f:
    json.dump(akshay_data, f, indent=2)

print("\n✅ Portfolio data structure created and saved to 'akshay_portfolio_data.json'")