import pandas as pd
import matplotlib.pyplot as plt

def generate_kpi_report(db_url):
    # Query database
    query = """
    SELECT e.department, AVG(pr.score) as avg_score
    FROM Employees e
    JOIN PerformanceReviews pr ON e.employee_id = pr.employee_id
    GROUP BY e.department
    """
    engine = create_engine(db_url)
    df = pd.read_sql(query, engine)
    
    # Generate plot
    df.plot(kind='bar', x='department', y='avg_score')
    plt.title('Average Performance Score by Department')
    plt.savefig('reports/department_scores.png')
    return df

# Example usage
if __name__ == "__main__":
    generate_kpi_report("postgresql://user:password@localhost:5432/employee_db")