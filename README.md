# HR-Dataset Team-Horcruxes

## Team Members
- Aaditya Patil
- John Wesly D
- Apurv Raj
- Manisha Itha

## Project Overview
This project focuses on the analysis of HR datasets to gain insights into hiring trends, candidate behavior, and to suggest improvements for business processes.

## Data Cleaning
### Methods Used
- Initial data analysis to identify and handle missing values, duplicates, and outliers.
- Transformation of data formats for consistency.

### Before and After Data Cleaning
- Provided a comparison of data before and after cleaning to highlight improvements.

## Data Visualization
Visual representations of the cleaned data to identify patterns and trends.

## Relational Schema
A detailed relational schema was designed to illustrate the relationships between various entities within the HR dataset:
- **Location** is related to **Postal_Code**.
- **Region** is related to **Location** through **Region_Location_Mapping**.
- **Domicile** is referenced in **HR_Hiring_Details**.
- **Interview** is related to **Candidate_Ref**.
- **HR_Hiring_Details** contains references to **Location_ID**, **Postal_Code**, **Candidate_Ref**, **LOB_Id**, and **Domicile_ID**.
- **Joining_Status** is related to **Candidate_Ref**.
- **LOB** is referenced in **HR_Hiring_Details**.

## UML Diagram
A UML diagram illustrating the system’s architecture and data flow.

## Queries and Outputs
### Examples:
- Count of candidates who accepted offers and agreed to relocate.
- Candidates willing to join with a 25% hike, relocation, and bonus.
- Count of joined vs. declined candidates by source.

## Flask Application
A web application built using Flask to:
- Search candidate details based on their reference number.
- Display relevant information about candidates.

## AWS Deployment
Deployed the Flask application on AWS:
- Enabled searching for candidates.
- Displayed search results effectively.
- Created s3 Bucket then uploaded csv file in the bucket.
- Created role in Iam role service and provided permissions.
- Then migrated in EC2 instance.
- then configured aws with access key and secured access key in cloudshell.
- then created flask application there.

## Power BI Dashboard
Developed a Power BI dashboard to visualize key metrics and insights derived from the HR dataset.

## Business Improvement Recommendations
### 1. Diversity and Inclusion
- **Current Insight**: Significant gender gap with 82.74% male hires and 17.26% female hires.
- **Recommendation**: Implement targeted recruitment programs to attract more female candidates and diversify the workforce.

### 2. Retention Strategy
- **Current Insight**: 18.7% of candidates did not join despite being hired.
- **Recommendation**: Investigate reasons behind candidates not joining and improve the onboarding process and offer acceptability.

### 3. Geographical Distribution
- **Current Insight**: Hiring is concentrated in Chennai, Bangalore, and Hyderabad.
- **Recommendation**: Explore and expand hiring to other regions to tap into diverse talent pools and reduce dependency on specific locations.

### 4. LOB Focus
- **Current Insight**: Most hires are concentrated in INFRA and ERS.
- **Recommendation**: Assess the growth and hiring needs of underrepresented LOBs like Healthcare and MMS to ensure balanced development across all areas.

### 5. Interview Trends
- **Current Insight**: Decline in total interviews year-over-year.
- **Recommendation**: Reevaluate the interview process and candidate sourcing strategies to ensure a steady pipeline of talent.

## Conclusion
This project provided a comprehensive analysis of the HR dataset, revealing critical insights and providing actionable recommendations to improve hiring processes, diversity, and retention strategies. The development of a Flask application and Power BI dashboard facilitated effective data visualization and decision-making support.

